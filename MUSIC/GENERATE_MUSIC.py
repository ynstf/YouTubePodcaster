from ..LLM.GENERATE_PODCUST import send_prompt
import requests
import time

# Function to generate a conversation
def generate_music_prompt(prompt,podcust):
    prompt_total = prompt + podcust
    return send_prompt(prompt_total)

def generate_music(prompt,podcust,HUGGING_FACE_TOKEN,API_URL):
    # Your Hugging Face API token
    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_TOKEN}",
        "Content-Type": "application/json"
    }
    # Payload with the prompt
    payload = {
        "inputs": prompt
    }
    while True:
        # Send the POST request
        response = requests.post(API_URL, headers=headers, json=payload)
        print(response)
        # Check if the request was successful
        if response.status_code == 200:
            # Save the generated music
            with open("podcust/background.mp3", "wb") as f:
                f.write(response.content)
            print("Music saved as 'podcust/background.mp3'")
            break
        else:
            print(f"Failed to generate music. Status code: {response.status_code}")
            print(response.text)
        time.sleep(5)
    
    return "podcust/background.mp3"


