# File:  main.py
import sys
from PyQt5 import QtWidgets
from threat_detector import ThreatDetector
from dashboard import Dashboard

if __name__ == '__main__':
    # Create the PyQt5 application.
    app = QtWidgets.QApplication(sys.argv)
    
    # Initialize the threat detection module.
    threat_detector = ThreatDetector()
    
    # Create and show the dashboard, passing in the threat detector.
    dashboard = Dashboard(threat_detector)
    dashboard.show()
    
    # Start the PyQt5 event loop.
    sys.exit(app.exec_())
