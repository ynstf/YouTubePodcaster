from dotenv import load_dotenv
import os
from REDDIT.GENERATE_REDDIT import create_content
from LLM.GENERATE_PODCUST import create_conversation

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
text = create_content(CLIENT_ID,CLIENT_SECRET,USER_AGENT)
print("text from reddit created")


# Access the variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL")
MODEL = os.getenv("MODEL")
prompt = open("PROMPTS/conversation_prompt.txt", "r", encoding ="UTF-8").read()

# Create the conversation
conversation_list = create_conversation(prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
print("conversation created by llm")
