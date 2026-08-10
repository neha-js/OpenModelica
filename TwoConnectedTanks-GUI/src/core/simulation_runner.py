"""Wrapper for running the OpenModelica executable."""

from __future__ import annotations

from pathlib import Path

from PyQt5.QtCore import QProcess


class SimulationRunner:
    """Runs the compiled simulation executable via QProcess."""

    def __init__(self, executable_path: str | Path):
        self._process = QProcess()
        self.executable_path = str(executable_path)

    def run(self, *args: str) -> None:
        """Launch the simulation executable with optional command-line args."""
        self._process.start(self.executable_path, list(args))

    def is_running(self) -> bool:
        return self._process.state() != QProcess.NotRunning

    def terminate(self) -> None:
        self._process.terminate()
