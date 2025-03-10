import sys
import serial  # Import serial for Arduino communication
from PyQt5.QtWidgets import QApplication, QMainWindow
from first_output import Ui_MainWindow  # Import the generated UI file

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI
        
        # Set up serial communication with Arduino
        self.arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Change port if needed
        
        # Connect button click event to function
        self.main_connect.clicked.connect(self.send_serial_command)  # Replace 'setButton' with your actual button object name

    def send_serial_command(self):
        """Send a serial command to Arduino when button is clicked."""
        command = "SET_COMMAND\n"  # Change this to whatever you want to send
        self.arduino.write(command.encode())  # Send the command as bytes
        print(f"Sent: {command}")  # Debug print

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
