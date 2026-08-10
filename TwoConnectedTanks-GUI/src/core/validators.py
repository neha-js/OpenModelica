"""Validation helpers for the Two Connected Tanks GUI."""

import math


def validate_numeric_field(value: str, field_name: str) -> float:
    """Return a finite float or raise a ValueError with a clear message."""
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be a valid number.") from exc

    if not math.isfinite(parsed):
        raise ValueError(f"{field_name} must be finite.")

    return parsed


def validate_tank_inputs(
    initial_level: str,
    inflow_rate: str,
    tank_area: str,
    valve_resistance: str,
) -> dict:
    """Validate the GUI input values for the two-tank model."""
    values = {
        "initial_level": validate_numeric_field(initial_level, "Initial level"),
        "inflow_rate": validate_numeric_field(inflow_rate, "Inflow rate"),
        "tank_area": validate_numeric_field(tank_area, "Tank area"),
        "valve_resistance": validate_numeric_field(valve_resistance, "Valve resistance"),
    }

    for key, value in values.items():
        if value <= 0:
            label = key.replace("_", " ").title()
            raise ValueError(f"{label} must be greater than zero.")

    return values
