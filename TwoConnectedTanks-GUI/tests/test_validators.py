from pathlib import Path

import pytest

from src.core.validators import (
    validate_executable_inputs,
    validate_numeric_field,
    validate_tank_inputs,
    validate_time_field,
)


def test_validate_numeric_field_accepts_number():
    assert validate_numeric_field("3.5", "Test") == 3.5


def test_validate_numeric_field_rejects_invalid_value():
    with pytest.raises(ValueError, match="must be a valid number"):
        validate_numeric_field("abc", "Test")


def test_validate_tank_inputs_accepts_valid_values():
    values = validate_tank_inputs("1.0", "0.5", "2.0", "4.0")
    assert values["initial_level"] == 1.0
    assert values["inflow_rate"] == 0.5
    assert values["tank_area"] == 2.0
    assert values["valve_resistance"] == 4.0


def test_validate_tank_inputs_rejects_non_positive_values():
    with pytest.raises(ValueError, match="greater than zero"):
        validate_tank_inputs("0", "0.5", "2.0", "4.0")


def test_validate_time_field_accepts_integer_time():
    assert validate_time_field("10", "Start time") == 10


def test_validate_executable_inputs_accepts_valid_path_and_times(tmp_path):
    executable = tmp_path / "two_tanks_model.exe"
    executable.write_text("binary")

    values = validate_executable_inputs(str(executable), "10", "20")
    assert values["executable_path"] == str(executable)
    assert values["start_time"] == 10
    assert values["stop_time"] == 20


def test_validate_executable_inputs_rejects_invalid_time_range(tmp_path):
    executable = tmp_path / "two_tanks_model.exe"
    executable.write_text("binary")

    with pytest.raises(ValueError, match="Stop time must be greater than start time"):
        validate_executable_inputs(str(executable), "20", "10")
