import os
import sys
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(dotenv_path):
    print(f"Missing .env file at {dotenv_path}")
    sys.exit(1)

load_dotenv(dotenv_path=dotenv_path)

DB_USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASS')
HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DB_NAME')