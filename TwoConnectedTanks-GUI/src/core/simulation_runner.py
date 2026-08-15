"""Wrapper for running the OpenModelica executable."""

from __future__ import annotations

from pathlib import Path

from PyQt6.QtCore import QProcess


class SimulationRunner:
    """Runs the compiled simulation executable via QProcess."""

    def __init__(self, executable_path: str | Path):
        self._process = QProcess()
        self.executable_path = str(executable_path)

    def run(self, *args: str) -> bool:
        """Launch the simulation executable with optional command-line args."""
        if self.is_running():
            return False

        self._process.start(self.executable_path, list(args))
        return self._process.waitForStarted(1000)

    def is_running(self) -> bool:
        return self._process.state() != QProcess.ProcessState.NotRunning

    def terminate(self) -> None:
        self._process.terminate()
