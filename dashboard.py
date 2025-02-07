# File: dashboard.py
import sys
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self, threat_detector):
        super().__init__()
        self.setWindowTitle("Cybersecurity Threat Detection and Response Dashboard")
        self.threat_detector = threat_detector
        
        # Set up the central widget and layout.
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QtWidgets.QVBoxLayout(self.main_widget)
        
        # Create a matplotlib figure and canvas to display the chart.
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        # Create a text area (QTextEdit) to serve as the log.
        self.log_area = QtWidgets.QTextEdit()
        self.log_area.setReadOnly(True)  # Users should not modify log text.
        self.layout.addWidget(self.log_area)
        
        # Data storage for plotting.
        self.x_data = []  # Time steps (or sequential count).
        self.y_data = []  # Packet sizes.
        
        # Set up the plot: create an axis and an initial empty line.
        self.ax = self.figure.add_subplot(111)
        self.line, = self.ax.plot([], [], 'b-')  # Blue line for normal data.
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Packet Size")
        self.ax.set_title("Real-time Packet Size Monitoring")
        
        # Set up a QTimer to update the dashboard every 1000 milliseconds (1 second).
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_dashboard)
        self.timer.start(1000)
        
        # Internal counter to simulate time.
        self.time_counter = 0

    def update_dashboard(self):
        """
        Called every second by the QTimer.
        It simulates a new data point, checks for threats,
        updates the plot, and logs the result.
        """
        try:
            # Simulate a new data point.
            data_point = self.threat_detector.simulate_data_point()
            packet_size = data_point[0]
            is_anomaly = self.threat_detector.detect_threat(data_point)
            
            # Update time counter and store new data for plotting.
            self.time_counter += 1
            self.x_data.append(self.time_counter)
            self.y_data.append(packet_size)
            
            # Keep only the most recent 50 data points.
            if len(self.x_data) > 50:
                self.x_data = self.x_data[-50:]
                self.y_data = self.y_data[-50:]
            
            # Update the plot line.
            self.line.set_data(self.x_data, self.y_data)
            self.ax.relim()
            self.ax.autoscale_view()
            self.canvas.draw()
            
            # Log the detection result.
            if is_anomaly:
                log_msg = (f"Time {self.time_counter}: Anomaly Detected! "
                           f"Data: {data_point.tolist()}. Response: Block suspicious traffic.")
                self.log_area.append(log_msg)
            else:
                log_msg = f"Time {self.time_counter}: Normal traffic. Data: {data_point.tolist()}."
                self.log_area.append(log_msg)
        except Exception as e:
            # Log any errors to help with troubleshooting.
            error_msg = f"Error at time {self.time_counter}: {str(e)}"
            self.log_area.append(error_msg)
            print(error_msg)
