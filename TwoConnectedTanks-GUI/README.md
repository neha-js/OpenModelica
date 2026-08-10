# TwoConnectedTanks-GUI

A PyQt-based GUI for running a Two Connected Tanks simulation built from an OpenModelica executable.

## Project structure

```text
TwoConnectedTanks-GUI/
├── README.md
├── requirements.txt
├── .gitignore
├── executable/              # Place the OMEdit build output here
│   └── README.md
├── src/
│   ├── main.py               # Application entry point
│   ├── core/
│   │   ├── validators.py     # Input validation (no Qt dependency)
│   │   └── simulation_runner.py  # QProcess wrapper that runs the executable
│   └── gui/
│       └── main_window.py    # QMainWindow: layout, widgets, signal wiring
└── tests/
    └── test_validators.py    # Unit tests for the validation rules
```

## Setup

```bash
cd TwoConnectedTanks-GUI
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

## Notes

- Keep Qt-specific code in the GUI layer.
- Keep validation logic in the `core` package so it remains easy to test.
- Place the compiled OpenModelica executable in `executable/`.
