"""
Unit Tests for Travel Itinerary Planning Agent.
Tests Constraint Satisfaction, Heuristic Knapsack, and Input Validation.
"""

import pytest
from core.planner import TravelPlanningAgent, PlanningValidationError
from data.destinations_data import (
    SAMPLE_DESTINATIONS,
    ALL_28_INDIAN_STATES,
    STATE_DESTINATIONS_MAP,
    validate_all_28_states_present,
)


def test_all_28_states_presence_and_coverage():
    """Verify that all 28 Indian states are present, have at least one destination, and pass validation."""
    assert len(ALL_28_INDIAN_STATES) == 28, f"Expected 28 states, found {len(ALL_28_INDIAN_STATES)}"
    
    validation_result = validate_all_28_states_present()
    assert validation_result["status"] == "VALID"
    assert validation_result["total_states"] == 28
    assert validation_result["total_destinations"] >= 28

    # Ensure every single state in the list has at least one destination
    for state in ALL_28_INDIAN_STATES:
        dests = STATE_DESTINATIONS_MAP.get(state, [])
        assert len(dests) >= 1, f"State '{state}' has no destinations configured!"

    # Verify existing benchmark destinations are preserved under correct states
    assert "Jaipur, Rajasthan" in STATE_DESTINATIONS_MAP["Rajasthan"]
    assert "Goa (North & South)" in STATE_DESTINATIONS_MAP["Goa"]
    assert "Manali, Himachal Pradesh" in STATE_DESTINATIONS_MAP["Himachal Pradesh"]
    assert "Varanasi, Uttar Pradesh" in STATE_DESTINATIONS_MAP["Uttar Pradesh"]
    assert "Agra, Uttar Pradesh" in STATE_DESTINATIONS_MAP["Uttar Pradesh"]
    assert "Kochi, Kerala" in STATE_DESTINATIONS_MAP["Kerala"]


def test_destination_from_every_state_can_be_planned():
    """Verify that at least one destination from each of the 28 states plans successfully."""
    for state in ALL_28_INDIAN_STATES:
        dests = STATE_DESTINATIONS_MAP[state]
        assert len(dests) > 0
        sample_dest = dests[0]
        agent = TravelPlanningAgent(
            destination_name=sample_dest,
            budget=15000,
            num_days=2,
            hours_per_day=7.0
        )
        plan = agent.plan()
        assert len(plan["days_plan"]) == 2
        assert plan["constraint_status"] in ["OPTIMAL_NEAR_CAPACITY", "FEASIBLE_WITH_SURPLUS", "BUDGET_EXCEEDED"]



def test_successful_plan_generation():
    """Verify standard valid inputs produce a valid multi-day itinerary."""
    agent = TravelPlanningAgent(
        destination_name="Jaipur, Rajasthan",
        budget=15000,
        num_days=3,
        hours_per_day=8.0,
        pace="Moderate"
    )
    result = agent.plan()

    assert result["destination"] == "Jaipur, Rajasthan"
    assert len(result["days_plan"]) == 3
    assert result["financial_summary"]["user_budget"] == 15000
    assert result["financial_summary"]["total_estimated_cost"] > 0
    assert "reasoning_logs" in result
    assert len(result["reasoning_logs"]) > 5


def test_time_constraint_per_day():
    """Ensure no day exceeds the user-configured daily available hours limit."""
    daily_hours = 6.0
    agent = TravelPlanningAgent(
        destination_name="Goa (North & South)",
        budget=20000,
        num_days=3,
        hours_per_day=daily_hours,
        pace="Moderate"
    )
    result = agent.plan()

    for day in result["days_plan"]:
        # Total active time should not exceed daily hours (with slight tolerance for rounding)
        assert day["total_active_hours"] <= daily_hours + 0.3
        # Sightseeing + transit should equal active time
        assert abs((day["sightseeing_hours"] + day["transit_hours"]) - day["total_active_hours"]) < 0.05


def test_attraction_uniqueness():
    """Ensure no attraction is visited more than once across multiple days."""
    agent = TravelPlanningAgent(
        destination_name="Jaipur, Rajasthan",
        budget=25000,
        num_days=3,
        hours_per_day=9.0
    )
    result = agent.plan()

    visited_ids = []
    for day in result["days_plan"]:
        for activity in day["schedule"]:
            visited_ids.append(activity["id"])

    assert len(visited_ids) == len(set(visited_ids)), "Duplicate attraction detected across days!"


def test_input_validation_errors():
    """Verify edge cases and invalid inputs raise descriptive PlanningValidationErrors."""
    # Negative budget
    with pytest.raises(PlanningValidationError, match="positive number"):
        TravelPlanningAgent("Jaipur, Rajasthan", budget=-100, num_days=2, hours_per_day=8.0)

    # Budget too low
    with pytest.raises(PlanningValidationError, match="unrealistically low"):
        TravelPlanningAgent("Jaipur, Rajasthan", budget=200, num_days=2, hours_per_day=8.0)

    # Invalid days (< 1)
    with pytest.raises(PlanningValidationError, match="between 1 and 10"):
        TravelPlanningAgent("Jaipur, Rajasthan", budget=10000, num_days=0, hours_per_day=8.0)

    # Excess days (> 10)
    with pytest.raises(PlanningValidationError, match="between 1 and 10"):
        TravelPlanningAgent("Jaipur, Rajasthan", budget=10000, num_days=15, hours_per_day=8.0)

    # Hours too low (< 3)
    with pytest.raises(PlanningValidationError, match="between 3.0 and 14.0"):
        TravelPlanningAgent("Jaipur, Rajasthan", budget=10000, num_days=2, hours_per_day=2.0)

    # Unknown destination
    with pytest.raises(PlanningValidationError, match="not in the benchmark database"):
        TravelPlanningAgent("Atlantis", budget=10000, num_days=2, hours_per_day=8.0)


def test_all_sample_destinations_run():
    """Verify all 6 benchmark destinations plan successfully."""
    for dest_name in SAMPLE_DESTINATIONS.keys():
        agent = TravelPlanningAgent(
            destination_name=dest_name,
            budget=12000,
            num_days=2,
            hours_per_day=7.0
        )
        plan = agent.plan()
        assert len(plan["days_plan"]) == 2
        assert plan["constraint_status"] in ["OPTIMAL_NEAR_CAPACITY", "FEASIBLE_WITH_SURPLUS", "BUDGET_EXCEEDED"]


def test_budget_exceeded_detection():
    """Verify that when budget is smaller than fixed costs, the agent detects and flags it."""
    agent = TravelPlanningAgent(
        destination_name="Manali, Himachal Pradesh",
        budget=1000,  # Very low for 3 days with hotels & food
        num_days=3,
        hours_per_day=7.0,
        accommodation_tier="Budget Guesthouse / 2-Star"
    )
    result = agent.plan()
    assert result["is_within_budget"] is False
    assert result["constraint_status"] == "BUDGET_EXCEEDED"
    assert result["financial_summary"]["budget_variance"] < 0
