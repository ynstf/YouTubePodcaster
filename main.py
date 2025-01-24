from dotenv import load_dotenv
import os
import json
from REDDIT.GENERATE_REDDIT import create_content
from LLM.GENERATE_PODCUST import create_conversation,send_prompt
from AUDIO.GENERATE_AUDIO import create_audios, create_one_audio, mix_podcust_audio
from MUSIC.GENERATE_MUSIC import generate_music
from MUSIC.FIX_MUSIC import fix_music
from IMAGE.GENERATE_IMAGES import create_images_prompts, create_images
from VIDEO.GENERATE_VIDEO import generate_video
from UPLOAD.SHARE_VIDEO import share_video,split_infos, get_authenticated_service

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
#text = create_content(CLIENT_ID,CLIENT_SECRET,USER_AGENT)
print("text from reddit created")


# Access the variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL")
MODEL = os.getenv("MODEL")
conversation_prompt = open("PROMPTS/conversation_prompt.txt", "r", encoding ="UTF-8").read()

# Create the conversation
#conversation_list = create_conversation(conversation_prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
print("conversation created by llm")

print("START !!!!!!!!!!!!!!!!!!!!!!!!!!")

conversation_list = [{'role': 'Man',
  'text': "<speak><prosody rate='slow'>مرحبًا بالجميع،</prosody> <break time='1s'/> اليوم سنتحدث عن شيء مثير للاهتمام. <break time='1s'/> أنا محمد، مؤثر في مجال النشر الرقمي والسياسي. بالنسبة لي، هذا الموضوع يعني تغيرات هائلة في السياسة والمجتمع الأمريكي. ماذا يعني لكِ، آمنة؟</speak>"},
]

# Access the variables
VOICE_ID_MAN = os.getenv("VOICE_ID_MAN")
VOICE_ID_WOMAN = os.getenv("VOICE_ID_WOMAN")
AUDIO_OUTPUT_FILE = os.getenv("AUDIO_OUTPUT_FILE")
# Load the proxies from the JSON file
with open("proxies.json", "r") as file:
    proxies = json.load(file)
# create podcust audio
#audios_list = create_audios(conversation_list,proxies,VOICE_ID_MAN,VOICE_ID_WOMAN)

audios_list = ["podcast/segment_0.mp3","podcast/segment_1.mp3","podcast/segment_2.mp3"]
path_podcust_audio = "podcast/podcast_final.mp3"
print("audios_list",audios_list)
#path_podcust_audio = create_one_audio(audios_list,AUDIO_OUTPUT_FILE)

print("audios_list",audios_list)
print("path_podcust_audio",path_podcust_audio)





# create music background

HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
MUSIC_API_URL = os.getenv("MUSIC_API_URL")
llm_music_prompt = open("PROMPTS/music_prompt.txt", "r", encoding ="UTF-8").read()
conversation = open("conversation.txt", "r", encoding ="UTF-8").read()

#music_prompt = send_prompt(llm_music_prompt,conversation,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)

music_prompt = "Create a calm song about a podcast discussing political and social awareness, featuring instruments such as acoustic guitar, soft piano, and gentle strings. The tempo should be slow and soothing, setting a relaxed atmosphere for reflection on the podcast's dialogue between Mohamed and Amina. Capture the essence of their thoughtful conversation on the importance of political participation and social impact. Feel free to incorporate Arabic influences in the melody to reflect the cultural exchange in the podcast. Let the music evoke a sense of introspection and contemplation as listeners engage with the podcast's thought-provoking themes."

print("music_prompt",music_prompt)

"""path_music = generate_music(music_prompt,
                conversation,
                HUGGING_FACE_TOKEN,
                MUSIC_API_URL,
                "podcast/background.mp3")"""


# fix music (adding metadata)
print("FIXING BACKGROUND")
#path_fixed = fix_music()
#print(path_fixed)

path_fixed = "podcast/background_fixed.mp3"
# mix music with audio 
print("MIXING PODCUST")
#path_mixed_audio = mix_podcust_audio(path_podcust_audio,path_fixed)
#print(path_mixed_audio)
path_mixed_audio = "podcast/mixed_podcast.mp3"


# generate images
# Get the IMAGE_API_URLS from the .env file
image_api_urls_str = os.getenv("IMAGE_API_URLS")
# Split the string into a list
IMAGE_API_URLS = image_api_urls_str.split(",")
# Print the list to verify
print('IMAGE_API_URLS : ',IMAGE_API_URLS)
llm_images_prompt = open("PROMPTS/images_prompt.txt", "r", encoding ="UTF-8").read()

#images_prompt = send_prompt(llm_images_prompt,conversation,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
#print('image prompt :',images_prompt)
images_prompt = """1. An image of two individuals engaged in a passionate conversation about politics and social issues, symbolizing the podcast's focus on raising political awareness and democratic participation.
2. A graphic illustration showcasing various symbols of individual rights and freedoms intertwined with political elements, representing the podcast's theme of advocating for personal liberties and civic engagement.
3. A vibrant visual representation of a diverse group of young people casting their votes in an election, highlighting the importance of youth involvement in shaping political decisions.
4. A scene depicting a person attending a political rally holding a sign with a powerful message, inspired by the podcast's content on the impact of political participation in the society.
5. An abstract artwork with intricate patterns symbolizing the complexity of political influence and societal change, capturing the essence of the podcast's thought-provoking discussions.
6. A thought-provoking image of a spectrum of diverse voices coming together in unity, reflecting the podcast's theme of inclusivity and the power of shared perspectives in politics.
7. A dynamic illustration of a vibrant cityscape with people actively engaging in political discourse and activism, representing the podcast's topic of promoting civic engagement among communities.
8. A visually appealing infographic showcasing key points related to the podcast's main idea of the intersection between politics and marginalized communities, making the information accessible and engaging.
9. A detailed and dynamic collage featuring various symbols of political activism and social change, inspired by the podcast's in-depth exploration of the impact of current political trends on marginalized groups.
10. A captivating scene of individuals from different backgrounds coming together in a public square, exchanging ideas and opinions on political matters, capturing the essence of the podcast's theme on promoting dialogue and awareness in the society."""
#prompts_list = create_images_prompts(images_prompt)
prompts_list = ["An image of two individuals engaged in a passionate conversation about politics and social issues, symbolizing the podcast's focus on raising political awareness and democratic participation.", "A graphic illustration showcasing various symbols of individual rights and freedoms intertwined with political elements, representing the podcast's theme of advocating for personal liberties and civic engagement.", 'A vibrant visual representation of a diverse group of young people casting their votes in an election, highlighting the importance of youth involvement in shaping political decisions.', "A scene depicting a person attending a political rally holding a sign with a powerful message, inspired by the podcast's content on the impact of political participation in the society.", "An abstract artwork with intricate patterns symbolizing the complexity of political influence and societal change, capturing the essence of the podcast's thought-provoking discussions.", "A thought-provoking image of a spectrum of diverse voices coming together in unity, reflecting the podcast's theme of inclusivity and the power of shared perspectives in politics.", "A dynamic illustration of a vibrant cityscape with people actively engaging in political discourse and activism, representing the podcast's topic of promoting civic engagement among communities.", "A visually appealing infographic showcasing key points related to the podcast's main idea of the intersection between politics and marginalized communities, making the information accessible and engaging.", "A detailed and dynamic collage featuring various symbols of political activism and social change, inspired by the podcast's in-depth exploration of the impact of current political trends on marginalized groups.", "A captivating scene of individuals from different backgrounds coming together in a public square, exchanging ideas and opinions on political matters, capturing the essence of the podcast's theme on promoting dialogue and awareness in the society."]
#print("prompts list : ",prompts_list)

#path_created_images = create_images(prompts_list,IMAGE_API_URLS,HUGGING_FACE_TOKEN)
#print('images generated : ', path_created_images )




# generate vedios
path_created_images = ['images/generated_image_0.png', 'images/generated_image_1.png', 'images/generated_image_2.png', 'images/generated_image_3.png', 'images/generated_image_4.png', 'images/generated_image_5.png', 'images/generated_image_6.png', 'images/generated_image_7.png', 'images/generated_image_8.png', 'images/generated_image_9.png']
#output_video_path = generate_video(path_mixed_audio, path_created_images)
output_video_path = "podcast/podcast.mp4"




# upload to youtube

UPLOAD_TO_YOUTUBE = os.getenv("UPLOAD_TO_YOUTUBE")
TOKEN_FILE_YOUTUBE = os.getenv("TOKEN_FILE_YOUTUBE")
share_prompt = open("PROMPTS/share_prompt.txt", "r", encoding ="UTF-8").read()
print('sharing is :', UPLOAD_TO_YOUTUBE)




if UPLOAD_TO_YOUTUBE == "ON":
    print(share_prompt)
    video_infos = send_prompt(share_prompt,conversation,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
    title, description, tags = split_infos(video_infos)
    with open("video_infos.txt", "w", encoding ="UTF-8") as file:
        content = f"""
        video infos : {video_infos} .
        title : {title} .
        description : {description} .
        tags : {tags} .
        """
        file.write(content)
    youtube = get_authenticated_service(TOKEN_FILE_YOUTUBE)
    print("youtube ready !!")
    share_video(youtube, title, description, tags, output_video_path)





