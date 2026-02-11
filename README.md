# Lightweight Network IDS

This was a fast project aimed at learning more about network-based Intrusion Detection Systems (IDS) built in Python.  
The project monitors incoming TCP connections and detects suspicious activity such as brute-force attacks and port scanning using threshold-based anomaly detection.

---

## Features

- Multithreaded TCP server
- Real-time connection monitoring
- Brute-force detection (sliding time window)
- Port scan detection
- Alert cooldown system (prevents alert spam)
- Structured logging to file
- IPv4 and IPv6 support

---

## Detection Logic

The project uses a threshold-based anomaly detection model:

### Brute-force Detection
If an IP address exceeds a defined number of connections within a time window:

→ An alert is triggered.

### Port Scan Detection
If an IP contacts multiple unique ports

→ An alert is triggered.

### Alert Cooldown
To prevent alert flooding, a cooldown mechanism limits repeated alerts from the same IP.

---

## How to Run

### Requirements

- Python 3.10+

### Start the server

bash
python main.py


### Simulate connections (Linux/maxOS)
for i in {1..10}; do nc localhost 9999; done

### Simulate connections (Windows PowerShell)
for ($i=0; $i -lt 10; $i++) { Test-NetConnection localhost -Port 9999 }