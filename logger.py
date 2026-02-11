from datetime import datetime

LOG_FILE = "netwatch.log"

# Simple logging function to log events with timestamps and severity levels
def log_event(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{level}] {message}\n"

    print(log_message.strip())  # Print to console

    with open(LOG_FILE, "a") as f:
        f.write(log_message)  # Append to log file