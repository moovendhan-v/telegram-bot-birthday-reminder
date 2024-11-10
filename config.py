import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# List of environment variable names that we need to check
required_vars = ["TELEGRAM_BOT_TOKEN", "API_URL", "DATABASE_DEFAULT_PATH"]

# Check each required environment variable
for var in required_vars:
    value = os.getenv(var)
    if not value:
        print(f"Error: {var} not set in environment variables.")
        sys.exit(1)  # Exit with a non-zero code if any variable is missing

# If both variables are present, print their values (for debugging purposes)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = os.getenv("API_URL")
DATABASE_DEFAULT_PATH = os.getenv("DATABASE_DEFAULT_PATH")

print(f"Using bot token:")
print(f"Using API URL: {API_URL}")
print(f"Using databse path : {DATABASE_DEFAULT_PATH}")
