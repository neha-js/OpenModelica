# TwoConnectedTanks-GUI

A PyQt6-based GUI for running a Two Connected Tanks simulation built from an OpenModelica executable.

## Technology stack

- Python 3.6+
- PyQt6
- OpenModelica

## Project structure

TwoConnectedTanks-GUI/
├── README.md
├── requirements.txt
├── .gitignore
├── executable/
│   └── README.md
├── src/
│   ├── main.py
│   ├── core/
│   │   ├── validators.py
│   │   └── simulation_runner.py
│   └── gui/
│       └── main_window.py
└── tests/
    └── test_validators.py

```bash
cd TwoConnectedTanks-GUI
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or .\.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

## App behavior

The GUI now provides the workflow described in the assignment:

- Application to launch: file selector for the compiled OpenModelica executable
- Start time: integer value
- Stop time: integer value
- Run button: launches the selected executable with the start and stop values as arguments

## Tests

```bash
python -m pytest -q
```

## Notes

- Keep Qt-specific code in the GUI layer.
- Keep validation logic in the `core` package so it remains easy to test.
- The executable must be built in OpenModelica/OMEdit and selected in the app using the file browser.
- The app validates that the selected file exists and that the stop time is greater than the start time.
