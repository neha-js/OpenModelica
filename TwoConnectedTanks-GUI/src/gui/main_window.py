"""Main application window for the Two Connected Tanks GUI."""

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from core.validators import validate_tank_inputs


class MainWindow(QMainWindow):
    """Main user interface for the simulation inputs."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Connected Tanks")
        self.resize(420, 320)

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

        run_button = QPushButton("Run Simulation")
        run_button.clicked.connect(self.on_run_clicked)
        layout.addWidget(run_button)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def on_run_clicked(self):
        try:
            validate_tank_inputs(
                self.initial_level_input.text(),
                self.inflow_rate_input.text(),
                self.tank_area_input.text(),
                self.valve_resistance_input.text(),
            )
        except ValueError as exc:
            QMessageBox.critical(self, "Invalid Input", str(exc))
            return

        QMessageBox.information(self, "Simulation", "Inputs are valid and ready to run.")
