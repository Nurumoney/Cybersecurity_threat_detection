# Cybersecurity Threat Detection and Response Dashboard

![image description](https://github.com/Vaskar71/Cybersecurity-Threat-Detection-and-Response-Dashboard/blob/main/Introduction%20Image.png?raw=true)



## Overview

The **Cybersecurity Threat Detection and Response Dashboard** is a user-friendly **desktop application** designed to **monitor network activity in real-time**, detect **potential security threats** using simulated threat patterns, and provide **immediate alerts**. It logs suspicious activities, enabling users to track incidents effectively and respond **promptly to cybersecurity threats**.

## Tech Stack Used:
- **Programming Language:**  Python
- **GUI Framework:**  PyQt5 (for building the desktop application UI)
- **Styling:**  QDarkStyle (for a modern, dark-themed UI)
- **Concurrency:**  PyQt5 QThread (to run threat detection without freezing the UI)
- **Machine Learning Techniques:**
-    **Anomaly Detection**  (to identify unusual patterns in simulated network data)
-    **Statistical Analysis & Rule-Based Detection**  (simulating real-world cybersecurity detection methods)
-    **Dataset:** Simulated threat patterns  (randomized data generation) 

## Background

In today's digital landscape, cybersecurity is paramount. This project was initiated out of a personal interest in enhancing security monitoring tools. The goal was to create an intuitive interface that simplifies the complex task of threat detection, making it accessible even to those without extensive technical expertise.

## Features

- **Real-Time Monitoring:** Continuously scans for suspicious activities.
- **User-Friendly Interface:** Intuitive design for easy navigation and understanding.
- **Alert System:** Immediate notifications of potential threats.
- **Logging:** Detailed records of detected threats for further analysis.

## Visuals

![Threat Alert](https://github.com/Vaskar71/Cybersecurity-Threat-Detection-and-Response-Dashboard/blob/main/Threat.png?raw=true)

*Figure 1: Dashboard displaying a threat alert.*

## Known Issues and To-Do List

### Known Issues

- **False Positives:** Occasionally, benign activities may be flagged as threats.
- **Performance:** High system resource usage during intensive monitoring periods.

### To-Do

- **Enhance Detection Algorithms:** Improve accuracy to reduce false positives.
- **Optimize Performance:** Refine the monitoring process to be more resource-efficient.
- **Add Customization Options:** Allow users to adjust sensitivity and configure alert preferences.

## Installation and Setup

Follow these steps to clone, build, and run the application:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Vaskar71/Cybersecurity-Threat-Detection-and-Response-Dashboard.git
   cd cybersecurity-dashboard
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Design the GUI:**

   - Open Qt Designer:

     ```bash
     designer
     ```

   - Load the `dashboard.ui` file located in the project directory.
   - Ensure the GUI components are correctly configured and save any changes.

5. **Run the Application:**

   ```bash
   python main.py
   ```

   The dashboard should now be operational and monitoring for threats.

