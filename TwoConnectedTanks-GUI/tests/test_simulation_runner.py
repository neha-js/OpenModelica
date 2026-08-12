from pathlib import Path

import pytest

from src.core.simulation_runner import SimulationRunner


def test_simulation_runner_run_on_nonexistent_executable(monkeypatch, tmp_path):
    nonexistent_executable = tmp_path / "missing.exe"
    runner = SimulationRunner(str(nonexistent_executable))

    assert runner.run("1", "2") is False
    assert runner.is_running() is False


@pytest.mark.skipif(True, reason="Requires QProcess integration and a real executable")
def test_simulation_runner_run_with_executable(tmp_path):
    # This test is a placeholder because QProcess requires a real executable.
    executable = tmp_path / "dummy.exe"
    executable.write_text("")
    runner = SimulationRunner(str(executable))

    assert runner.run("1", "2") is False
