import time
from collections import defaultdict
from logger import log_event

#Stores connection timestamps per IP address
connection_history = defaultdict(list)

#Stores unique ports contacted per IP address
port_history = defaultdict(set)

#Detection thresholds
BRUTE_FORCE_THRESHOLD = 5  # Number of connections in a short time frame
TIME_WINDOW = 10  # Time frame in seconds for counting connections
PORT_SCAN_THRESHOLD = 5    # Number of unique ports contacted in a short time frame

#Analyzes incoming connections for potential brute-force attacks and port scans
def analyze_connection(ip, port):

    current_time = time.time()

    connection_history[ip].append(current_time)

    connection_history[ip] = [t for t in connection_history[ip] if current_time - t <= TIME_WINDOW]

    if len(connection_history[ip]) > BRUTE_FORCE_THRESHOLD:
        log_event("ALERT", f"Possible brute-force attack detected from {ip}")

    port_history[ip].add(port)

    if len(port_history[ip]) > PORT_SCAN_THRESHOLD:
        log_event("ALERT", f"Possible port scan detected from {ip}")