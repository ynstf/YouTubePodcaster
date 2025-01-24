from dotenv import load_dotenv
import os
import json
import time
from REDDIT.GENERATE_REDDIT import create_content
from LLM.GENERATE_PODCUST import create_conversation,send_prompt
from AUDIO.GENERATE_AUDIO import create_audios, create_one_audio, mix_podcust_audio
from MUSIC.GENERATE_MUSIC import generate_music
from MUSIC.FIX_MUSIC import fix_music
from IMAGE.GENERATE_IMAGES import create_images_prompts, create_images
from VIDEO.GENERATE_VIDEO import generate_video
from UPLOAD.SHARE_VIDEO import share_video,split_infos, get_authenticated_service




print("START !!!!!!!!!!!!!!!!!!!!!!!!!!")


def delete_files(file_list):
    """
    Deletes a list of files.

    Args:
        file_list (list): A list of file paths to delete.
    """
    for file_path in file_list:
        try:
            # Check if the file exists
            if os.path.exists(file_path):
                # Delete the file
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
            else:
                print(f"File does not exist: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Load environment variables from .env file
load_dotenv()

# Initialize a list to store all generated paths
generated_paths = []

# Access the variables
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")


# Create text from reddit
print("creating text from reddit .....")
text = create_content(CLIENT_ID,CLIENT_SECRET,USER_AGENT)
print("text from reddit created")

time.sleep(5)

# Access the variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL")
MODEL = os.getenv("MODEL")
conversation_prompt = open("PROMPTS/conversation_prompt.txt", "r", encoding ="UTF-8").read()


time.sleep(5)

# Create the conversation
print("creating conversation ....")
conversation_list = create_conversation(conversation_prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
print("conversation created by llm")


time.sleep(5)


# Access the variables
VOICE_ID_MAN = os.getenv("VOICE_ID_MAN")
VOICE_ID_WOMAN = os.getenv("VOICE_ID_WOMAN")
# Load the proxies from the JSON file
print("Loading Proxies ....")
with open("proxies.json", "r") as file:
    proxies = json.load(file)
print("Proxies loaded")
print("creating podcust audios, wait for finish ....")
audios_list = create_audios(conversation_list,proxies,VOICE_ID_MAN,VOICE_ID_WOMAN)
print("podcust audios created")


time.sleep(5)

# create one audio
AUDIO_OUTPUT_FILE = os.getenv("AUDIO_OUTPUT_FILE")
print("generating one audio ...")
path_podcust_audio = create_one_audio(audios_list,AUDIO_OUTPUT_FILE)
print("one audio generated")



time.sleep(5)


# create music background
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
MUSIC_API_URL = os.getenv("MUSIC_API_URL")
llm_music_prompt = open("PROMPTS/music_prompt.txt", "r", encoding ="UTF-8").read()
conversation = open("conversation.txt", "r", encoding ="UTF-8").read()
print("generating prompt music ...")
music_prompt = send_prompt(llm_music_prompt,conversation,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
print("prompt music generated")


time.sleep(1)

print("generating music ....")
path_music = generate_music(music_prompt,
                conversation,
                HUGGING_FACE_TOKEN,
                MUSIC_API_URL,
                "podcast/background.mp3")
print("music generated")


time.sleep(5)

# fix music (adding metadata)
print("FIXING BACKGROUND ....")
path_fixed = fix_music()
print("music fixed")


time.sleep(5)



# mix music with audio 
print("MIXING PODCUST ...")
path_mixed_audio = mix_podcust_audio(path_podcust_audio,path_fixed)
print("podcast mixed")


time.sleep(5)


# generate images
# Get the IMAGE_API_URLS from the .env file
image_api_urls_str = os.getenv("IMAGE_API_URLS")
IMAGE_API_URLS = image_api_urls_str.split(",")
llm_images_prompt = open("PROMPTS/images_prompt.txt", "r", encoding ="UTF-8").read()

print('generating prompts of images....')
images_prompt = send_prompt(llm_images_prompt,conversation,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
print('prompts generated')
print('generating prompts list ...')
prompts_list = create_images_prompts(images_prompt)
print('prompts list generated')

time.sleep(1)
print("wait, generating images ........")
path_created_images = create_images(prompts_list,IMAGE_API_URLS,HUGGING_FACE_TOKEN)
print("images generated")


time.sleep(3)


# generate vedios
print("generating the video .....")
output_video_path = generate_video(path_mixed_audio, path_created_images)
print("video generated")

time.sleep(3)

generated_paths.append(path_podcust_audio)#
generated_paths.append(audios_list)#
generated_paths.append(path_music)#
generated_paths.append(path_fixed)#
generated_paths.append(path_mixed_audio)#
generated_paths.extend(path_created_images)#
generated_paths.append(output_video_path)#



# upload to youtube
UPLOAD_TO_YOUTUBE = os.getenv("UPLOAD_TO_YOUTUBE")
TOKEN_FILE_YOUTUBE = os.getenv("TOKEN_FILE_YOUTUBE")
share_prompt = open("PROMPTS/share_prompt.txt", "r", encoding ="UTF-8").read()

print('sharing is :', UPLOAD_TO_YOUTUBE)
if UPLOAD_TO_YOUTUBE == "ON":
    print("generating infos ....")
    video_infos = send_prompt(share_prompt,conversation,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
    title, description, tags = split_infos(video_infos)
    print("title, description, tags generated")

    time.sleep(1)

    with open("video_infos.txt", "w", encoding ="UTF-8") as file:
        content = f"""
        video infos : {video_infos} .
        title : {title} .
        description : {description} .
        tags : {tags} .
        """
        file.write(content)
    print("infos saved ! ")
    print("uploading video")
    youtube = get_authenticated_service(TOKEN_FILE_YOUTUBE)
    print("youtube ready !!")
    share_video(youtube, title, description, tags, output_video_path)
    print('video uploaded')
    # Delete all generated files
    delete_files(generated_paths)


