import os
import requests
import time



def generate_music(prompt,podcust,HUGGING_FACE_TOKEN,API_URL,file_path):
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
            with open(file_path, "wb") as f:
                f.write(response.content)
            print("Music saved as 'podcust/background.mp3'")
            break
        else:
            print(f"Failed to generate music. Status code: {response.status_code}")
            print(response.text)
        time.sleep(5)
    
    return file_path


