from dotenv import load_dotenv
import os
from REDDIT.GENERATE_REDDIT import create_content

# Load environment variables from .env file
load_dotenv()

# Access the variables
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

# Example usage
print(f"Client ID: {CLIENT_ID}")
print(f"Client Secret: {CLIENT_SECRET}")
print(f"User Agent: {USER_AGENT}")

# Create text from reddit
create_content(CLIENT_ID,CLIENT_SECRET,USER_AGENT)


# Access the variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL")
MODEL = os.getenv("MODEL")