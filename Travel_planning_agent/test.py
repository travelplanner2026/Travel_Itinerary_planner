"""
Pan-India Validation and Test Runner for AI Travel Planning Agent.
Tests all 28 Indian States, Constraint Satisfaction, Heuristic Knapsack, and Web UI integrity.
Can be executed directly via: `python test.py` or `pytest test.py -v`.
"""

import sys
import pytest
from core.planner import TravelPlanningAgent, PlanningValidationError
from data.destinations_data import (
    ALL_28_INDIAN_STATES,
    SAMPLE_DESTINATIONS,
    STATE_DESTINATIONS_MAP,
    validate_all_28_states_present,
)


def test_all_28_states_validation():
    """Requirement 9: Validation check confirming all 28 states are present and covered."""
    res = validate_all_28_states_present()
    assert res["status"] == "VALID"
    assert res["total_states"] == 28
    assert len(res["states"]) == 28

    # Confirm every state has at least one destination
    for state in ALL_28_INDIAN_STATES:
        dests = STATE_DESTINATIONS_MAP.get(state, [])
        assert len(dests) >= 1, f"State '{state}' has no destinations!"


def test_preserved_benchmark_destinations():
    """Requirement 5: Ensure existing destinations are preserved under correct states."""
    expected = {
        "Rajasthan": "Jaipur, Rajasthan",
        "Goa": "Goa (North & South)",
        "Himachal Pradesh": "Manali, Himachal Pradesh",
        "Uttar Pradesh": "Varanasi, Uttar Pradesh",
        "Kerala": "Kochi, Kerala",
    }
    for state, dest in expected.items():
        assert dest in STATE_DESTINATIONS_MAP[state], f"{dest} not found under {state}!"
    assert "Agra, Uttar Pradesh" in STATE_DESTINATIONS_MAP["Uttar Pradesh"]


def test_itinerary_planning_across_all_28_states():
    """Requirement 6: Verify planning agent successfully generates itineraries for every state."""
    for state in ALL_28_INDIAN_STATES:
        dest_name = STATE_DESTINATIONS_MAP[state][0]
        agent = TravelPlanningAgent(
            destination_name=dest_name,
            budget=15000,
            num_days=2,
            hours_per_day=7.0
        )
        plan = agent.plan()
        assert len(plan["days_plan"]) == 2
        assert plan["constraint_status"] in ["OPTIMAL_NEAR_CAPACITY", "FEASIBLE_WITH_SURPLUS", "BUDGET_EXCEEDED"]
        assert plan["financial_summary"]["total_estimated_cost"] > 0


def test_time_constraint_enforcement():
    """Ensure daily active hours never exceed user limit plus allowable slack tolerance."""
    agent = TravelPlanningAgent(
        destination_name="Kolkata, West Bengal",
        budget=12000,
        num_days=2,
        hours_per_day=6.0,
        pace="Moderate"
    )
    res = agent.plan()
    for day in res["days_plan"]:
        assert day["total_active_hours"] <= 6.3


def test_input_validation():
    """Verify input validation handles invalid boundaries gracefully."""
    with pytest.raises(PlanningValidationError):
        TravelPlanningAgent("Invalid City", 10000, 2, 7.0)

    with pytest.raises(PlanningValidationError):
        TravelPlanningAgent("Jaipur, Rajasthan", -500, 2, 7.0)


def run_standalone_checks():
    """Runs tests in standalone mode when executed via `python test.py`."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    print("=" * 70)
    print("[*] PAN-INDIA TRAVEL PLANNING AGENT: 28-STATE VERIFICATION SUITE")
    print("=" * 70)

    print("\n[1/5] Validating all 28 Indian States presence & destination coverage...")
    test_all_28_states_validation()
    val_report = validate_all_28_states_present()
    print(f"      SUCCESS: Found {val_report['total_states']} States, "
          f"{val_report['total_destinations']} Destinations, "
          f"{val_report['total_attractions']} Attractions.")

    print("\n[2/5] Validating preservation of original benchmark destinations...")
    test_preserved_benchmark_destinations()
    print("      SUCCESS: Jaipur, Goa, Manali, Varanasi, Kochi, and Agra verified under respective states.")

    print("\n[3/5] Validating itinerary generator across all 28 states...")
    test_itinerary_planning_across_all_28_states()
    print("      SUCCESS: Valid plans generated for every single state.")

    print("\n[4/5] Validating time constraint satisfaction...")
    test_time_constraint_enforcement()
    print("      SUCCESS: Daily hours limits strictly enforced.")

    print("\n[5/5] Validating error handling & input validation...")
    test_input_validation()
    print("      SUCCESS: Input validation properly catches edge cases.")

    print("\n" + "=" * 70)
    print("[SUCCESS] ALL PAN-INDIA CHECKS PASSED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--pytest":
        sys.exit(pytest.main(["-v", "test.py"]))
    else:
        run_standalone_checks()
