# TwoConnectedTanks-GUI

A PyQt-based GUI for running a Two Connected Tanks simulation built from an OpenModelica executable.

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
# or .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

## Tests

```bash
python -m pytest -q
```

## Notes

- Keep Qt-specific code in the GUI layer.
- Keep validation logic in the `core` package so it remains easy to test.
- Place the compiled OpenModelica executable in `executable/`.
- The GUI looks for a runnable executable in `executable/` and reports a clear error if none is found.
