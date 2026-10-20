"""Data package for AI Travel Planning Agent."""
from .destinations_data import (
    SAMPLE_DESTINATIONS,
    STANDARD_DAILY_COSTS,
    ALL_28_INDIAN_STATES,
    STATE_DESTINATIONS_MAP,
    validate_all_28_states_present,
)

__all__ = [
    "SAMPLE_DESTINATIONS",
    "STANDARD_DAILY_COSTS",
    "ALL_28_INDIAN_STATES",
    "STATE_DESTINATIONS_MAP",
    "validate_all_28_states_present",
]
