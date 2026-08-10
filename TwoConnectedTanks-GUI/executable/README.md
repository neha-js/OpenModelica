# Executable folder

Place the built OpenModelica executable (or the final OMEdit binary) in this directory.

The application expects a runnable binary here, and the code in `src/core/simulation_runner.py` will launch it through `QProcess`.
