# File: threat_detector.py
import numpy as np
from sklearn.ensemble import IsolationForest

class ThreatDetector:
    def __init__(self):
        # Generate an initial simulated dataset of "normal" traffic for training.
        self.train_data = self.generate_normal_data(1000)
        # Train the IsolationForest model on this data.
        # contamination=0.01 means we expect about 1% anomalies in the real world.
        self.model = IsolationForest(contamination=0.01, random_state=42)
        self.model.fit(self.train_data)
    
    def generate_normal_data(self, n):
        """
        Generates n samples of normal traffic data.
        Each sample consists of 4 features:
         - packet_size: Simulated as a normal distribution (mean=500, std=50)
         - src_port: Random integer between 1024 and 65535
         - dst_port: Random integer between 20 and 1024 (common port range)
         - protocol: Categorical encoded as 0 (TCP) or 1 (UDP)
        """
        packet_size = np.random.normal(500, 50, n)
        src_port = np.random.randint(1024, 65535, n)
        dst_port = np.random.randint(20, 1024, n)
        protocol = np.random.choice([0, 1], n)  # 0 for TCP, 1 for UDP
        data = np.column_stack((packet_size, src_port, dst_port, protocol))
        return data
    
    def simulate_data_point(self):
        """
        Simulates a single data point representing network traffic.
        There is a 10% chance that this data point is anomalous.
        Anomalies are simulated by using extreme values:
         - A much higher packet_size,
         - Source port from a suspicious (lower) range,
         - Destination port from an unusual range,
         - And a protocol value that is not normal (e.g., 2 to indicate anomaly).
        """
        if np.random.rand() < 0.1:  # 10% chance of anomaly
            # Generate anomalous data with extreme values.
            packet_size = np.random.normal(1000, 100)  # larger packet size
            src_port = np.random.randint(1, 1024)        # suspicious source port
            dst_port = np.random.randint(1024, 65535)     # unusual destination port
            protocol = np.random.choice([2])             # protocol '2' represents anomaly
        else:
            # Generate normal data.
            packet_size = np.random.normal(500, 50)
            src_port = np.random.randint(1024, 65535)
            dst_port = np.random.randint(20, 1024)
            protocol = np.random.choice([0, 1])
        return np.array([packet_size, src_port, dst_port, protocol])
    
    def detect_threat(self, data_point):
        """
        Uses the trained IsolationForest model to detect if a given data point is anomalous.
        Returns True if the data point is an anomaly, False otherwise.
        """
        # The model expects a 2D array, so we reshape the data_point accordingly.
        data_point = data_point.reshape(1, -1)
        prediction = self.model.predict(data_point)
        # IsolationForest returns -1 for anomalies and 1 for normal data.
        return prediction[0] == -1
