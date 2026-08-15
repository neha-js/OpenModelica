"""Main application window for the Two Connected Tanks GUI."""

from pathlib import Path

from PyQt6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from core.simulation_runner import SimulationRunner
from core.validators import validate_executable_inputs


class MainWindow(QMainWindow):
    """Main user interface for selecting an executable and passing time arguments."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Connected Tanks")
        self.resize(500, 260)

        self.simulation_runner: SimulationRunner | None = None
        self.executable_path: str | None = None

        central = QWidget()
        layout = QVBoxLayout()

        self.application_input = QLineEdit()
        self.application_input.setPlaceholderText("Select executable...")
        self.application_input.setReadOnly(True)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.on_browse_clicked)

        executable_row = QHBoxLayout()
        executable_row.addWidget(self.application_input)
        executable_row.addWidget(browse_button)

        self.start_time_input = QLineEdit("0")
        self.stop_time_input = QLineEdit("10")

        fields = [
            ("Application to launch", executable_row),
            ("Start time", self.start_time_input),
            ("Stop time", self.stop_time_input),
        ]

        for label_text, field in fields:
            label = QLabel(label_text)
            layout.addWidget(label)
            if isinstance(field, QHBoxLayout):
                layout.addLayout(field)
            else:
                layout.addWidget(field)

        self.run_button = QPushButton("Run Simulation")
        self.run_button.clicked.connect(self.on_run_clicked)
        layout.addWidget(self.run_button)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def on_browse_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select executable",
            str(Path.home()),
            "Executable Files (*);;All Files (*.*)",
        )
        if file_path:
            self.executable_path = file_path
            self.application_input.setText(file_path)

    def on_run_clicked(self):
        executable_path = self.executable_path or self.application_input.text().strip()
        if not executable_path:
            QMessageBox.critical(self, "Executable Missing", "Please choose the executable to launch.")
            return

        try:
            inputs = validate_executable_inputs(
                executable_path,
                self.start_time_input.text(),
                self.stop_time_input.text(),
            )
        except ValueError as exc:
            QMessageBox.critical(self, "Invalid Input", str(exc))
            return

        self.simulation_runner = SimulationRunner(inputs["executable_path"])
        started = self.simulation_runner.run(str(inputs["start_time"]), str(inputs["stop_time"]))

        if not started:
            QMessageBox.critical(
                self,
                "Simulation Failed",
                "Unable to start the selected simulation executable.",
            )
            return

        QMessageBox.information(
            self,
            "Simulation Started",
            f"Started executable: {Path(inputs['executable_path']).name} with start={inputs['start_time']} and stop={inputs['stop_time']}",
        )
