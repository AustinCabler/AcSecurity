# We use Panadas for Logging
import pandas as pd
from datetime import datetime
import os
from pathlib import Path
# Define the log file path
LOG_FILE = Path("acsecurity_log.csv")
if not LOG_FILE.exists():
    # Create the log file with headers if it doesn't exist
    df = pd.DataFrame(columns=["timestamp", "level", "message"])
    df.to_csv(LOG_FILE, index=False)
def log_message(level, message):
    """
    Log a message with a specific level to the log file.
    Args:
        level (str): The log level (e.g., 'INFO', 'WARNING', 'ERROR').
        message (str): The message to log.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = pd.DataFrame([[timestamp, level, message]], columns=["timestamp", "level", "message"])
    
    # Append the log entry to the log file
    log_entry.to_csv(LOG_FILE, mode='a', header=False, index=False)
    
    # Print the log entry to the console
    print(f"{timestamp} [{level}] {message}")
def log_info(message):
    """
    Log an informational message.
    Args:
        message (str): The message to log.
    """
    log_message("INFO", message)
def log_warning(message):
    """
    Log a warning message.
    Args:
        message (str): The message to log.
    """
    log_message("WARNING", message)
def log_error(message):
    """Log an error message.
    Args:
        message (str): The message to log.
    """
    log_message("ERROR", message)
def read_log():
    """ Read the log file and return its contents.
    Returns:
        pd.DataFrame: A DataFrame containing the log entries.
    """
    if LOG_FILE.exists():
        return pd.read_csv(LOG_FILE)
    else:
        log_warning("Log file does not exist.")
        return pd.DataFrame(columns=["timestamp", "level", "message"])
def clear_log():
    """Clear the log file."""
    if LOG_FILE.exists():
        os.remove(LOG_FILE)
        log_info("Log file cleared.")
    else:
        log_warning("Log file does not exist, nothing to clear.")
def get_log_file_path():
    """Get the path to the log file.
    Returns:
    The path to the log file as a string.
    """
    return str(LOG_FILE.resolve())
def log_to_console():
    """Log the contents of the log file to the console."""
    df = read_log()
    if not df.empty:
        print(df.to_string(index=False))
    else:
        log_info("Log file is empty.")