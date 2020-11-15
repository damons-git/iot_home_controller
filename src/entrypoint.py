from dotenv import load_dotenv
from pathlib import Path
import os

from hub_controller import Controller
from logger import Logger


# Setup dotenv environment variables
env_path = Path('.env')
load_dotenv(dotenv_path = env_path)

# Setup logger
log_path = os.getenv("LOG_OUTPUT_DIR")
log_name = "application.log"
Logger.output_dir(log_path)
Logger.output_name(log_name)
Logger.setup()
log = Logger()

# Load application
controller = Controller()
controller.start()
