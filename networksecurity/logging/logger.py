import logging
import os
from datetime import datetime

# Create a timestamped log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Set up logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")
# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Set the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO,
)