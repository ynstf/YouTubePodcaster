import requests
import json

# Function to send a prompt to the free model
def send_prompt(prompt,text,OPENROUTER_API_URL,OPENROUTER_API_KEY,MODEL):
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

# Function to split the conversation into a dictionary list
def split_conversation(conversation):
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