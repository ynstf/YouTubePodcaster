import librosa
from moviepy.editor import AudioFileClip, CompositeAudioClip, afx
import soundfile as sf
import numpy as np
import requests
import urllib3
# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to generate audio for a given text and voice ID using a proxy
def generate_audio(text, voice_id, proxy):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?allow_unauthenticated=1"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",  # Mimic Firefox
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://elevenlabs.io/",
        "Origin": "https://elevenlabs.io",
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",  # Ensure the correct model is used
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
        }
    }
    try:
        response = requests.post(url, json=data, headers=headers, proxies=proxy, timeout=10, verify=False)
        if response.status_code == 200 and response.headers.get('Content-Type') == 'audio/mpeg':
            return response.content  # Return audio as BytesIO object
        else:
            print(f"Error with proxy {proxy}: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Request failed with proxy {proxy}: {e}")
        return None

# make turn shorter if needed
def make_shorter(tst):
    if len(tst)>500:
        tst = tst.replace("<speak>","")
        tst = tst.replace("</speak>","")
        
        print("remove by <speak> and </speak> ")
    if len(tst)>500:
        tst = tst.replace("<prosody rate='slow'>","")
        print("remove by <prosody rate='slow'> ")
    if len(tst)>500:
        tst = tst.replace("</prosody>","")
        print("remove by </prosody> ")
    if len(tst)>500:
        tst = tst.replace("<break time='1s'/>","")
        print("remove by <break time='1s'/> ")
    if len(tst)>500:
        tst = tst[:500]
        print("remove by tst[:500] ")
        
    return tst

# Save each BytesIO object as an MP3 file
def save_files(audio_segments):
    audio_paths = []
    for i, segment in enumerate(audio_segments):
        with open(f"podcast/segment_{i}.mp3", "wb") as f:
            f.write(segment)
        print(f"Saved pudcast/segment_{i}.mp3")
        audio_paths.append(f"podcast/segment_{i}.mp3")
    return audio_paths

# Create all audios
def create_audios(proxies,VOICE_ID_MAN,VOICE_ID_WOMAN):
    # Generate audio for each chunk and combine
    audio_segments = []
    for i, turn in enumerate(conversation_list):
        role = turn["role"]
        text = turn["text"]
        text = make_shorter(text)
        #voice_id = VOICE_ID_MAN if role == "Man" else VOICE_ID_WOMAN
        voice_id = VOICE_ID_MAN if i % 2 == 0 else VOICE_ID_WOMAN
        print(f"Generating audio for {role} : {voice_id} (turn {i + 1})...")
        
        # Try all proxies for this chunk
        audio = None
        for proxy in proxies:
            print(f"Trying proxy {proxy}...")
            audio = generate_audio(text, voice_id, proxy)
            if audio:
                print(f"Successfully generated chunk {i + 1} with proxy {proxy}.")
                break
            else:
                print(f"Failed to generate chunk {i + 1} with proxy {proxy}.")

        if audio:
            audio_segments.append(audio)
        else:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?allow_unauthenticated=1"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",  # Mimic Firefox
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Referer": "https://elevenlabs.io/",
                "Origin": "https://elevenlabs.io",
            }
            data = {
                "text": text,
                "model_id": "eleven_multilingual_v2",  # Ensure the correct model is used
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                }
            }
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200 and response.headers.get('Content-Type') == 'audio/mpeg':
                audio = response.content
            if audio:
                audio_segments.append(audio)
            print(f"All proxies failed for chunk {i + 1}. Skipping this chunk.")
    save_files(audio_segments)
    audio_paths = save_files(audio_segments)
    return audio_paths

# Create the final audio
def create_one_audio(audios_list,OUTPUT_FILE):
    
    # Load and combine all audio files
    combined = []
    for file in audios_list:
        y, sr = librosa.load(file)
        combined.append(y)

    # Concatenate all audio segments
    final_audio = np.concatenate(combined)

    # Save the combined audio
    sf.write(f'podcast/{OUTPUT_FILE}', final_audio, sr)

# mix audio
def mix_podcust_audio(path_podcust_audio,path_fixed):
    
    # Load the podcast audio (MP3)
    podcast = AudioFileClip(path_podcust_audio)
    print("Podcast duration:", podcast.duration)

    # Load the background music (WAV or MP3)
    music = AudioFileClip(path_fixed)
    print("Music duration:", music.duration)

    # Adjust the volume of the background music (optional)
    music = music.volumex(0.4)  # Reduce volume by 50%

    # Ensure the music is the same length as the podcast
    if music.duration < podcast.duration:
        # Loop the music to match the podcast duration
        music = afx.audio_loop(music, duration=podcast.duration)
    else:
        # Trim the music to match the podcast duration
        music = music.subclip(0, podcast.duration)

    # Mix the podcast and music
    mixed_audio = CompositeAudioClip([podcast, music])

    # Export the mixed audio to a new file
    mixed_audio.write_audiofile("mixed_podcast.mp3", fps=44100)

    print("Mixed audio saved as 'mixed_podcast.mp3'")

    return "mixed_podcast.mp3"