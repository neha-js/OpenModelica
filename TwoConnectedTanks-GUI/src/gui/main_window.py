"""Main application window for the Two Connected Tanks GUI."""

from pathlib import Path

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from core.validators import validate_tank_inputs
from core.simulation_runner import SimulationRunner


class MainWindow(QMainWindow):
    """Main user interface for the simulation inputs."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Connected Tanks")
        self.resize(420, 320)

        self.simulation_runner: SimulationRunner | None = None

        central = QWidget()
        layout = QVBoxLayout()

        self.initial_level_input = QLineEdit("1.5")
        self.inflow_rate_input = QLineEdit("0.25")
        self.tank_area_input = QLineEdit("2.0")
        self.valve_resistance_input = QLineEdit("1.0")

        fields = [
            ("Initial level", self.initial_level_input),
            ("Inflow rate", self.inflow_rate_input),
            ("Tank area", self.tank_area_input),
            ("Valve resistance", self.valve_resistance_input),
        ]

        for label_text, field in fields:
            label = QLabel(label_text)
            layout.addWidget(label)
            layout.addWidget(field)

        self.run_button = QPushButton("Run Simulation")
        self.run_button.clicked.connect(self.on_run_clicked)
        layout.addWidget(self.run_button)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def _locate_executable(self) -> Path | None:
        executable_dir = Path(__file__).resolve().parents[2] / "executable"
        if not executable_dir.exists() or not executable_dir.is_dir():
            return None

        candidates = [
            path for path in executable_dir.iterdir()
            if path.is_file() and path.name.lower() != "readme.md"
        ]

        if not candidates:
            return None

        for candidate in candidates:
            if candidate.suffix.lower() == ".exe":
                return candidate

        return candidates[0]

    def on_run_clicked(self):
        try:
            inputs = validate_tank_inputs(
                self.initial_level_input.text(),
                self.inflow_rate_input.text(),
                self.tank_area_input.text(),
                self.valve_resistance_input.text(),
            )
        except ValueError as exc:
            QMessageBox.critical(self, "Invalid Input", str(exc))
            return

        executable_path = self._locate_executable()
        if executable_path is None:
            QMessageBox.critical(
                self,
                "Executable Missing",
                "No runnable executable was found in the executable/ folder.",
            )
            return

        self.simulation_runner = SimulationRunner(executable_path)
        started = self.simulation_runner.run(
            str(inputs["initial_level"]),
            str(inputs["inflow_rate"]),
            str(inputs["tank_area"]),
            str(inputs["valve_resistance"]),
        )

        if not started:
            QMessageBox.critical(
                self,
                "Simulation Failed",
                "Unable to start the simulation executable.",
            )
            return

        QMessageBox.information(
            self,
            "Simulation Started",
            f"Simulation launched with executable: {executable_path.name}",
        )
