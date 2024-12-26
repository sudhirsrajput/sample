import logging
import os
from datetime import datetime

# Determine the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Generate a log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory relative to the project root
log_dir = os.path.join(project_root, 'logs')

# Construct the full path for the log file
logs_path = os.path.join(log_dir, LOG_FILE)

# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Example log message
logging.info("Logging setup is complete.")
