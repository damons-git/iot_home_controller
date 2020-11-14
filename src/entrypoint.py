from dotenv import load_dotenv
from pathlib import Path
import os

from hub_controller import Controller


# Setup dotenv environment variables
env_path = Path('.env')
load_dotenv(dotenv_path = env_path)

# Load application
controller = Controller()
controller.start()
