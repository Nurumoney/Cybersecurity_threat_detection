# Cybersecurity Threat Detection and Response Dashboard

![Dashboard Screenshot](images/dashboard_screenshot.png)

## Overview

The Cybersecurity Threat Detection and Response Dashboard is a user-friendly application designed to monitor and identify potential security threats in real-time. It provides alerts and logs suspicious activities, enabling users to respond promptly to potential cybersecurity incidents.

## Background

In today's digital landscape, cybersecurity is paramount. This project was initiated out of a personal interest in enhancing security monitoring tools. The goal was to create an intuitive interface that simplifies the complex task of threat detection, making it accessible even to those without extensive technical expertise.

## Features

- **Real-Time Monitoring:** Continuously scans for suspicious activities.
- **User-Friendly Interface:** Intuitive design for easy navigation and understanding.
- **Alert System:** Immediate notifications of potential threats.
- **Logging:** Detailed records of detected threats for further analysis.

## Visuals

![Threat Alert](images/threat_alert.png)

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
   git clone https://github.com/yourusername/cybersecurity-dashboard.git
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

