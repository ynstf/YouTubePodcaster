import requests
import json

# Function to send a prompt to the free model
"""def send_prompt(prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL):
    MODELS = MODEL.split(',')
    trys = 3
    delay = 60

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    final_prompt = prompt + text
    data = {
        "model": MODEL,  # Use the free model
        "messages": [
            {"role": "user", "content": final_prompt}
        ]
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

"""
def send_prompt(prompt, text, OPENROUTER_API_URL, OPENROUTER_API_KEY, MODEL):
    MODELS = MODEL.split(',')  # Split the models into a list
    max_retries = 3  # Maximum number of retries per model
    delay = 60  # Delay between retries in seconds

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    final_prompt = prompt + text

    for model in MODELS:  # Iterate through each model
        for attempt in range(max_retries):  # Try each model up to 3 times
            data = {
                "model": model,  # Use the current model
                "messages": [
                    {"role": "user", "content": final_prompt}
                ]
            }
            try:
                response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
                response.raise_for_status()  # Raise an error for bad status codes
                return response.json()["choices"][0]["message"]["content"]  # Return the response if successful
            except requests.exceptions.RequestException as e:
                print(f"Error with model {model} (attempt {attempt + 1}): {e}")
                if attempt < max_retries - 1:  # If not the last attempt, wait before retrying
                    time.sleep(delay)
                else:
                    print(f"All attempts failed for model {model}. Moving to the next model.")
                    break  # Move to the next model after 3 failed attempts

    print("All models failed after retries.")
    return None  # Return None if all models fail


# Function to split the conversation into a dictionary list
"""def split_conversation(conversation):
    turns = conversation.split("\n")
    roles = ["Man", "Woman"]
    conversation_list = []
    role_index = 0

    for turn in turns:
        if turn.strip():  # Skip empty lines
            role = roles[role_index % len(roles)]
            conversation_list.append({"role": role, "text": turn.strip()})
            role_index += 1

    return conversation_list

"""
def split_conversation(conversation):
    # Split the conversation into <speak> blocks
    conversation = conversation.replace('```xml\n',"")
    conversation = conversation.replace('```',"")
    conversation = conversation.replace('xml',"")
    turns = conversation.split("</speak>")
    roles = ["Man", "Woman"]
    conversation_list = []
    role_index = 0

    for turn in turns:
        if turn.strip():  # Skip empty lines
            # Add the closing </speak> tag back to the turn
            turn = turn.strip() + "</speak>"
            role = roles[role_index % len(roles)]
            conversation_list.append({"role": role, "text": turn})
            role_index += 1

    return conversation_list

# Function to save a new conversation
def save_conversation(conversation,SAVE_CONVERSATION_FILE):
    with open(SAVE_CONVERSATION_FILE, "w", encoding ="UTF-8") as file_to_save:
        file_to_save.write(conversation)

def create_conversation(prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL):
    # Generate the conversation
    print("Generating conversation...")
    conversation = send_prompt(prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL)
    SAVE_CONVERSATION_FILE = "conversation.txt"
    save_conversation(conversation,SAVE_CONVERSATION_FILE)
    if not conversation:
        print("Failed to generate conversation.")
    # Split the conversation into a dictionary list
    conversation_list = split_conversation(conversation)
    return conversation_list