"""
AI Travel Itinerary Planning Agent Core Engine.
Implements a Constraint Satisfaction and Heuristic Knapsack Planning Algorithm
under strict Budget and Time Constraints.
"""

from typing import Dict, List, Any, Optional, Tuple
import copy
from data.destinations_data import SAMPLE_DESTINATIONS, STANDARD_DAILY_COSTS


class PlanningValidationError(Exception):
    """Raised when user input fails domain validation."""
    pass


class TravelPlanningAgent:
    """
    AI Agent that solves the Multi-Day Constrained Itinerary Planning Problem.
    Uses multi-attribute utility ranking, geographic zone clustering,
    greedy knapsack bin packing, and constraint validation.
    """

    def __init__(
        self,
        destination_name: str,
        budget: float,
        num_days: int,
        hours_per_day: float,
        pace: str = "Moderate",
        selected_categories: Optional[List[str]] = None,
        food_tier: str = "Moderate (Casual Cafes & Dhabas)",
        accommodation_tier: str = "Budget Guesthouse / 2-Star",
        include_buffer: bool = True
    ):
        self.destination_name = destination_name
        self.budget = float(budget)
        self.num_days = int(num_days)
        self.hours_per_day = float(hours_per_day)
        self.pace = pace
        self.selected_categories = selected_categories or []
        self.food_tier = food_tier
        self.accommodation_tier = accommodation_tier
        self.include_buffer = include_buffer

        self.destination_data = SAMPLE_DESTINATIONS.get(destination_name)
        self.reasoning_logs: List[str] = []
        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """Performs input validation and bounds checking."""
        if not self.destination_data:
            raise PlanningValidationError(
                f"Destination '{self.destination_name}' is not in the benchmark database."
            )
        if self.budget <= 0:
            raise PlanningValidationError("Budget must be a positive number in ₹ (Rupees).")
        if self.budget < 500:
            raise PlanningValidationError(
                "Budget is unrealistically low (₹500 minimum required for basic local day transit and food)."
            )
        if not (1 <= self.num_days <= 10):
            raise PlanningValidationError("Number of days must be between 1 and 10.")
        if not (3.0 <= self.hours_per_day <= 14.0):
            raise PlanningValidationError(
                "Available daily sightseeing hours must be between 3.0 and 14.0 hours."
            )

    def log(self, message: str) -> None:
        """Appends step to transparent agent decision audit trail."""
        self.reasoning_logs.append(message)

    def _calculate_utility(self, attraction: Dict[str, Any]) -> float:
        """
        Computes multi-attribute utility score for an attraction:
        U = w_r * (Rating / 5.0) + w_cat * (Category Match) - w_cost * (Fee / Budget) + w_eff * (Rating / Duration)
        """
        rating_score = (attraction.get("rating", 4.0) / 5.0) * 45.0  # up to 45 pts
        
        # Category preference bonus
        category_bonus = 0.0
        if self.selected_categories:
            if attraction.get("category") in self.selected_categories:
                category_bonus = 30.0
            else:
                category_bonus = 5.0
        else:
            category_bonus = 20.0  # neutral if user has no specific filter

        # Cost penalty (normalized against budget)
        fee = attraction.get("entry_fee", 0)
        cost_penalty = (fee / max(self.budget, 1000.0)) * 25.0

        # Time efficiency bonus (high rating per hour spent)
        duration = max(attraction.get("duration_hours", 1.0), 0.5)
        efficiency = (attraction.get("rating", 4.0) / duration) * 3.0

        total_utility = rating_score + category_bonus - cost_penalty + efficiency
        return round(total_utility, 2)

    def _group_attractions_by_zone(
        self, attractions: List[Dict[str, Any]]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Groups attractions into geographic clusters to minimize intra-day travel transit."""
        zones: Dict[str, List[Dict[str, Any]]] = {}
        for attr in attractions:
            zone = attr.get("zone", "General")
            if zone not in zones:
                zones[zone] = []
            zones[zone].append(attr)
        return zones

    def plan(self) -> Dict[str, Any]:
        """
        Main Constraint Satisfaction & Knapsack Planning Routine.
        Returns:
            Structured itinerary, financial constraint report, time utilization report,
            and step-by-step reasoning logs.
        """
        self.reasoning_logs = []
        self.log(f"Initiated AI Planning Agent for {self.destination_name}.")
        self.log(
            f"User constraints: Budget = ₹{self.budget:,.2f}, Days = {self.num_days}, "
            f"Available Time = {self.hours_per_day} hrs/day, Pace = {self.pace}."
        )

        # Baseline fixed cost calculation
        daily_food_rate = STANDARD_DAILY_COSTS["food"].get(self.food_tier, 600)
        daily_hotel_rate = STANDARD_DAILY_COSTS["accommodation"].get(self.accommodation_tier, 0)
        total_food_cost = daily_food_rate * self.num_days
        total_stay_cost = daily_hotel_rate * max(0, self.num_days - 1)  # nights = days - 1 or days
        if self.accommodation_tier != "Skip Lodging (Already booked / Day Trip)":
            total_stay_cost = daily_hotel_rate * self.num_days

        fixed_overhead = total_food_cost + total_stay_cost
        self.log(
            f"Estimated fixed costs: Food (₹{daily_food_rate}/day * {self.num_days}d = ₹{total_food_cost}), "
            f"Lodging (₹{daily_hotel_rate}/day * {self.num_days}d = ₹{total_stay_cost})."
        )

        remaining_budget_for_activities = self.budget - fixed_overhead
        if remaining_budget_for_activities < 0:
            self.log(
                f"[WARNING] Fixed overhead (₹{fixed_overhead:,.2f}) already exceeds total budget (₹{self.budget:,.2f}). "
                "Agent will flag budget violation and proceed with free/low-cost recommendations."
            )

        # Pace buffer adjustment
        # Relaxed pace: reserve 20% slack time; Intensive: 5% slack time; Moderate: 10%
        slack_pct = 0.20 if self.pace == "Relaxed" else (0.05 if self.pace == "Intensive" else 0.10)
        effective_daily_hours = self.hours_per_day * (1.0 - slack_pct)
        self.log(
            f"Pace factor '{self.pace}' applied: {slack_pct*100:.0f}% buffer reserved. "
            f"Effective sightseeing time budget: {effective_daily_hours:.2f} hrs/day."
        )

        # Retrieve and rank attractions
        all_attractions = copy.deepcopy(self.destination_data["attractions"])
        for attr in all_attractions:
            attr["utility_score"] = self._calculate_utility(attr)

        # Sort all attractions by utility score descending
        all_attractions.sort(key=lambda x: x["utility_score"], reverse=True)
        self.log(f"Calculated heuristic utility for {len(all_attractions)} candidate attractions.")

        # Group by geographic zone
        zones = self._group_attractions_by_zone(all_attractions)
        zone_keys = list(zones.keys())
        self.log(f"Identified {len(zone_keys)} geographic zones: {', '.join(zone_keys)}.")

        # Sort zones by aggregate utility of their attractions
        zone_scores = {
            z: sum(a["utility_score"] for a in attrs) for z, attrs in zones.items()
        }
        sorted_zones = sorted(zone_scores.keys(), key=lambda z: zone_scores[z], reverse=True)

        # Plan day-by-day
        days_plan: List[Dict[str, Any]] = []
        visited_ids = set()
        cumulative_sightseeing_fee = 0.0
        cumulative_transit_cost = 0.0
        cumulative_active_hours = 0.0

        same_zone_transit_cost = self.destination_data["avg_intra_zone_transit_cost"]
        cross_zone_transit_cost = self.destination_data["avg_inter_zone_transit_cost"]
        same_zone_transit_time = self.destination_data["transit_time_same_zone_hr"]
        cross_zone_transit_time = self.destination_data["transit_time_cross_zone_hr"]

        for day_num in range(1, self.num_days + 1):
            day_schedule: List[Dict[str, Any]] = []
            day_hours_spent = 0.0
            day_transit_spent = 0.0
            day_fees_spent = 0.0
            last_zone: Optional[str] = None

            # Primary zone for this day (round-robin among highest utility zones)
            primary_zone = sorted_zones[(day_num - 1) % len(sorted_zones)]
            self.log(f"--- Day {day_num}: Assigning primary focus zone '{primary_zone}' ---")

            # First attempt to pack attractions from primary zone
            candidate_pool = [a for a in zones[primary_zone] if a["id"] not in visited_ids]
            
            # If primary zone has few spots remaining, append from other zones sorted by utility
            if len(candidate_pool) < 2:
                for z in sorted_zones:
                    if z != primary_zone:
                        candidate_pool.extend([a for a in zones[z] if a["id"] not in visited_ids])

            # Slot packing loop
            for attr in candidate_pool:
                if attr["id"] in visited_ids:
                    continue

                duration = attr["duration_hours"]
                fee = attr["entry_fee"]
                attr_zone = attr["zone"]

                # Transit calculation from previous spot in the day
                if last_zone is None:
                    transit_time = same_zone_transit_time * 0.7  # Initial hop from hotel
                    transit_cost = same_zone_transit_cost * 0.7
                elif last_zone == attr_zone:
                    transit_time = same_zone_transit_time
                    transit_cost = same_zone_transit_cost
                else:
                    transit_time = cross_zone_transit_time
                    transit_cost = cross_zone_transit_cost

                # Constraint check: Time
                projected_day_time = day_hours_spent + transit_time + duration
                if projected_day_time > effective_daily_hours + 0.2:  # allow 12m tolerance
                    self.log(
                        f"Day {day_num}: Skipped '{attr['name']}' (Requires {duration}h + {transit_time:.2f}h transit; "
                        f"would exceed daily limit {effective_daily_hours:.2f}h)."
                    )
                    continue

                # Projected cost check (attractions + transit + fixed daily overhead)
                projected_total_cost = (
                    cumulative_sightseeing_fee + day_fees_spent + fee +
                    cumulative_transit_cost + day_transit_spent + transit_cost +
                    fixed_overhead
                )

                # If budget is strictly violated by this activity, check if we can skip it
                if projected_total_cost > self.budget and fee > 0:
                    self.log(
                        f"Day {day_num}: Skipped '{attr['name']}' due to budget limit "
                        f"(Fee: ₹{fee}, projected total ₹{projected_total_cost:,.0f} > Budget ₹{self.budget:,.0f})."
                    )
                    continue

                # Schedule attraction into slot
                slot_name = self._assign_time_slot(day_hours_spent, effective_daily_hours)
                item = {
                    "id": attr["id"],
                    "name": attr["name"],
                    "category": attr["category"],
                    "zone": attr["zone"],
                    "duration_hours": duration,
                    "entry_fee": fee,
                    "rating": attr["rating"],
                    "time_slot": slot_name,
                    "transit_time_to_reach": round(transit_time, 2),
                    "transit_cost_to_reach": round(transit_cost, 0),
                    "description": attr["description"],
                    "pro_tip": attr["pro_tip"]
                }
                day_schedule.append(item)
                visited_ids.add(attr["id"])

                day_hours_spent += (duration + transit_time)
                day_transit_spent += transit_cost
                day_fees_spent += fee
                last_zone = attr_zone

                self.log(
                    f"Day {day_num} [{slot_name}]: Added '{attr['name']}' "
                    f"(Time: {duration}h, Fee: ₹{fee}, Transit: {transit_time:.2f}h/₹{transit_cost:.0f})."
                )

                # Cap max 3-4 major attractions per day for quality experience
                if len(day_schedule) >= 4:
                    self.log(f"Day {day_num}: Reached comfortable maximum density (4 major activities).")
                    break

            cumulative_sightseeing_fee += day_fees_spent
            cumulative_transit_cost += day_transit_spent
            cumulative_active_hours += day_hours_spent

            slack_time = max(0.0, self.hours_per_day - day_hours_spent)
            days_plan.append({
                "day_number": day_num,
                "primary_zone": primary_zone,
                "schedule": day_schedule,
                "sightseeing_hours": round(sum(i["duration_hours"] for i in day_schedule), 2),
                "transit_hours": round(sum(i["transit_time_to_reach"] for i in day_schedule), 2),
                "total_active_hours": round(day_hours_spent, 2),
                "slack_hours": round(slack_time, 2),
                "daily_attractions_fee": day_fees_spent,
                "daily_transit_cost": day_transit_spent,
                "daily_food_cost": daily_food_rate,
                "daily_lodging_cost": daily_hotel_rate,
                "daily_total_cost": day_fees_spent + day_transit_spent + daily_food_rate + daily_hotel_rate
            })

        # Final Financial Compilation
        subtotal_costs = cumulative_sightseeing_fee + cumulative_transit_cost + fixed_overhead
        safety_buffer = (subtotal_costs * STANDARD_DAILY_COSTS["safety_buffer_pct"]) if self.include_buffer else 0.0
        final_total_estimated_cost = subtotal_costs + safety_buffer
        budget_variance = self.budget - final_total_estimated_cost

        # Constraint Status Verification
        if budget_variance >= 0:
            if budget_variance / self.budget <= 0.10:
                constraint_status = "OPTIMAL_NEAR_CAPACITY"
                status_message = "All constraints satisfied! Itinerary maximizes utility close to budget threshold."
            else:
                constraint_status = "FEASIBLE_WITH_SURPLUS"
                status_message = f"Budget constraint met with a comfortable surplus of ₹{budget_variance:,.2f}."
        else:
            constraint_status = "BUDGET_EXCEEDED"
            status_message = (
                f"Estimated cost exceeds budget by ₹{abs(budget_variance):,.2f}. "
                "Consider adjusting lodging/food tier or extending budget."
            )

        self.log(f"Final Planning Summary: Status = {constraint_status}, Total Cost = ₹{final_total_estimated_cost:,.2f}.")

        return {
            "destination": self.destination_name,
            "city_tagline": self.destination_data["tagline"],
            "city_description": self.destination_data["description"],
            "constraint_status": constraint_status,
            "status_message": status_message,
            "is_within_budget": budget_variance >= 0,
            "financial_summary": {
                "user_budget": self.budget,
                "total_estimated_cost": round(final_total_estimated_cost, 2),
                "budget_variance": round(budget_variance, 2),
                "sightseeing_fees": round(cumulative_sightseeing_fee, 2),
                "transit_costs": round(cumulative_transit_cost, 2),
                "food_costs": round(total_food_cost, 2),
                "lodging_costs": round(total_stay_cost, 2),
                "safety_buffer": round(safety_buffer, 2),
                "pct_budget_utilized": round((final_total_estimated_cost / self.budget) * 100, 1)
            },
            "time_summary": {
                "total_available_hours": round(self.hours_per_day * self.num_days, 2),
                "total_active_hours": round(cumulative_active_hours, 2),
                "avg_hours_per_day": round(cumulative_active_hours / max(1, self.num_days), 2),
                "total_attractions_visited": len(visited_ids),
                "total_attractions_available": len(self.destination_data["attractions"])
            },
            "days_plan": days_plan,
            "reasoning_logs": self.reasoning_logs
        }

    def _assign_time_slot(self, current_day_hours: float, max_day_hours: float) -> str:
        """Assigns sensible human-readable time slots based on daily progress."""
        progress_ratio = current_day_hours / max(1.0, max_day_hours)
        if progress_ratio < 0.35:
            return "Morning (09:00 AM - 12:30 PM)"
        elif progress_ratio < 0.70:
            return "Afternoon (01:30 PM - 05:00 PM)"
        else:
            return "Evening (05:30 PM - 08:30 PM)"
