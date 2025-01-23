from dotenv import load_dotenv
import os
import json
from REDDIT.GENERATE_REDDIT import create_content
from LLM.GENERATE_PODCUST import create_conversation
from AUDIO.GENERATE_AUDIO import create_audios, create_one_audio, mix_podcust_audio
from main import conversation_list, MUSIC_API_URL, path_music
from MUSIC.GENERATE_MUSIC import generate_music
from MUSIC.FIX_MUSIC import fix_music

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
conversation_prompt = open("PROMPTS/conversation_prompt.txt", "r", encoding ="UTF-8").read()

# Create the conversation
conversation_list = create_conversation(conversation_prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
print("conversation created by llm")


# Access the variables
VOICE_ID_MAN = os.getenv("VOICE_ID_MAN")
VOICE_ID_WOMAN = os.getenv("VOICE_ID_WOMAN")
AUDIO_OUTPUT_FILE = os.getenv("AUDIO_OUTPUT_FILE")
# Load the proxies from the JSON file
with open("proxies.json", "r") as file:
    proxies = json.load(file)
# create podcust audio
audios_list = create_audios(proxies,VOICE_ID_MAN,VOICE_ID_WOMAN)
path_podcust_audio = create_one_audio(audios_list,AUDIO_OUTPUT_FILE)



# create music background
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
MUSIC_API_URL = os.getenv("MUSIC_API_URL")
music_prompt = open("PROMPTS/music_prompt.txt", "r", encoding ="UTF-8").read()
with open("conversation.txt", "r") as file:
    conversationTXT = file.read()
path_music = generate_music(music_prompt,
                conversationTXT,
                HUGGING_FACE_TOKEN,
                MUSIC_API_URL)

# fix music (adding metadata)
path_fixed = fix_music(path_music)

# mix music with audio 
path_mixed_audio = mix_podcust_audio(path_podcust_audio,path_fixed)










