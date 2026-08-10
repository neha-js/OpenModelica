import pytest

from src.core.validators import validate_numeric_field, validate_tank_inputs


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
