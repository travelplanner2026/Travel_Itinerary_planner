"""
Integration tests for Streamlit Web Application using Streamlit AppTest.
Verifies UI controls, execution without runtime exceptions, and output rendering.
"""

import os
from pathlib import Path
from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).parent.parent / "app.py")


def test_streamlit_app_loads_and_runs():
    """Verify app.py initializes and renders without unhandled exceptions."""
    at = AppTest.from_file(APP_PATH, default_timeout=30)
    at.run()

    # App should have no uncaught exception alerts
    assert not at.exception, f"App threw exception: {at.exception}"

    # Verify key UI components are present
    assert len(at.tabs) == 4
    assert len(at.sidebar.selectbox) >= 3


def test_streamlit_app_budget_change():
    """Verify changing budget updates state cleanly."""
    at = AppTest.from_file(APP_PATH, default_timeout=30)
    at.run()

    if len(at.sidebar.number_input) >= 3:
        at.sidebar.number_input[2].set_value(25000).run()
        assert not at.exception


def test_streamlit_app_state_selection_updates_destinations():
    """Verify selecting a different Indian state updates the destinations dropdown cleanly."""
    at = AppTest.from_file(APP_PATH, default_timeout=30)
    at.run()

    # First selectbox is State dropdown containing all 28 states
    state_box = at.sidebar.selectbox[0]
    assert len(state_box.options) == 28
    assert "Kerala" in state_box.options
    assert "West Bengal" in state_box.options

    # Select Kerala
    state_box.select("Kerala").run()
    assert not at.exception

    # Second selectbox is Destination dropdown filtered to Kerala destinations
    dest_box = at.sidebar.selectbox[1]
    assert any("Kochi" in opt or "Munnar" in opt for opt in dest_box.options)



def test_internal_config_not_displayed():
    """Verify standard daily fixed overheads configuration is not displayed to the user."""
    at = AppTest.from_file(APP_PATH, default_timeout=30)
    at.run()

    # Verify no st.json element is rendered for standard overheads
    assert len(at.json) == 0

    # Verify configuration header and internal keys are not in markdown elements
    for md in at.markdown:
        assert "Standard Daily Fixed Overheads" not in md.value
        assert "safety_buffer_pct" not in md.value

