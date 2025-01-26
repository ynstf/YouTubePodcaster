<<<<<<< HEAD
# YouTubePodcaster  
**Automated AI-Powered Content Creation Pipeline**  

This project automates the process of transforming trending Reddit discussions into engaging YouTube videos. It leverages AI tools to generate dialogues, create audio and visuals, and compile everything into a polished video ready for publishing.  

---

## Overview  
The **YouTubePodcaster** pipeline extracts popular topics from Reddit, generates expert-level dialogues using GPT-3.5 Turbo, synthesizes natural-sounding voices with ElevenLabs, creates visuals using AI image models, and compiles everything into a video with background music. The final video is uploaded to YouTube with automatically generated metadata (title, description, and tags).  

---

## Features  
- **Reddit Scraping:** Fetches trending topics from Reddit based on comment engagement.  
- **Dialogue Generation:** Uses GPT-3.5 Turbo to create conversational dialogues between two characters (Ahmed and Amna).  
- **Voice Synthesis:** Utilizes ElevenLabs to generate realistic voiceovers for each character.  
- **Image Generation:** Creates visuals using AI models like Stable Diffusion, DALL-E, and others.  
- **Music Generation:** Generates background music using AI models like MusicGen.  
- **Video Compilation:** Combines audio, visuals, and music into a cohesive video.  
- **YouTube Upload:** Automatically uploads the final video to YouTube with generated metadata.  

---

## How It Works  
1. **Data Collection:**  
   - Scrape Reddit for trending topics with high engagement.  
   - Extract key points from the discussions.  

2. **Content Generation:**  
   - Use GPT-3.5 Turbo to create a dialogue between two experts (Ahmed and Amna).  
   - Generate voiceovers for each character using ElevenLabs.  

3. **Visuals and Audio:**  
   - Create images using AI models based on topic prompts.  
   - Generate background music using AI music models.  

4. **Video Production:**  
   - Combine audio, visuals, and music into a single video file.  
   - Use video editing tools to ensure smooth transitions and synchronization.  

5. **Publishing:**  
   - Automatically generate a title, description, and tags using GPT.  
   - Upload the final video to YouTube.  

---

## Technologies Used  
- **Natural Language Processing (NLP):** GPT-3.5 Turbo for dialogue generation and metadata creation.  
- **Voice Synthesis:** ElevenLabs for realistic voice generation.  
- **Image Generation:** Stable Diffusion, DALL-E, and other Hugging Face models for creating visuals.  
- **Music Generation:** MusicGen and other Hugging Face models for background music.  
- **Video Editing:** MoviePy for combining audio, images, and music.  
- **Web Scraping:** PRAW for Reddit data extraction.  
- **YouTube API:** For uploading videos and managing metadata.  

---

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/ynstf/YouTubePodcaster.git  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Configure environment variables:  
   - Create a `.env` file in the root directory and add your API keys:  
     ```plaintext  
     # Reddit API credentials  
     CLIENT_ID="your_reddit_client_id"  
     CLIENT_SECRET="your_reddit_client_secret"  
     USER_AGENT="your_user_agent"  

     # OpenRouter API settings  
     OPENROUTER_API_KEY="your_openrouter_api_key"  
     OPENROUTER_API_URL="https://openrouter.ai/api/v1/chat/completions"  
     MODEL="gpt-3.5-turbo"  

     # ElevenLabs Constants  
     VOICE_ID_MAN="your_voice_id_man"  
     VOICE_ID_WOMAN="your_voice_id_woman"  
     AUDIO_OUTPUT_FILE="podcast/podcast_final.mp3"  

     # Hugging Face  
     HUGGING_FACE_TOKEN="your_hugging_face_token"  
     MUSIC_API_URL="https://api-inference.huggingface.co/models/facebook/musicgen-small"  
     IMAGE_API_URLS="https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev,https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image,https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"  

     # YouTube Upload  
     UPLOAD_TO_YOUTUBE="ON"  
     TOKEN_FILE_YOUTUBE="UPLOAD/token.json"  
     ```  

4. Run the pipeline:  
   ```bash  
   python main.py  
   ```  

---

## File Structure  
```plaintext  
YouTubePodcaster/  
├── AUDIO/                  # Audio generation scripts  
├── IMAGE/                  # Image generation scripts  
├── LLM/                    # Dialogue generation scripts  
├── MUSIC/                  # Music generation scripts  
├── REDDIT/                 # Reddit scraping scripts  
├── UPLOAD/                 # YouTube upload scripts  
├── VIDEO/                  # Video compilation scripts  
├── PROMPTS/                # Prompt templates for GPT  
├── podcast/                # Generated audio files and Final video output  
├── images/                 # Generated image files  
├── .env                    # Environment variables  
├── main.py                 # Main script to run the pipeline  
├── README.md               # Project documentation  
└── requirements.txt        # Python dependencies  
```  

---

## Future Improvements  
- Add support for multiple languages and automated subtitles.  
- Improve the quality of generated visuals and music.  
- Integrate with additional platforms (e.g., TikTok, Instagram).  
- Add a user-friendly interface for non-technical users.  

---

## Contributing  
Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.  

---

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

=======
# YouTubePodcaster  
**Automated AI-Powered Content Creation Pipeline**  

This project automates the process of transforming trending Reddit discussions into engaging YouTube videos. It leverages AI tools to generate dialogues, create audio and visuals, and compile everything into a polished video ready for publishing.  

---

## Overview  
The **YouTubePodcaster** pipeline extracts popular topics from Reddit, generates expert-level dialogues using GPT-3.5 Turbo, synthesizes natural-sounding voices with ElevenLabs, creates visuals using AI image models, and compiles everything into a video with background music. The final video is uploaded to YouTube with automatically generated metadata (title, description, and tags).  

---

## Features  
- **Reddit Scraping:** Fetches trending topics from Reddit based on comment engagement.  
- **Dialogue Generation:** Uses GPT-3.5 Turbo to create conversational dialogues between two characters (Ahmed and Amna).  
- **Voice Synthesis:** Utilizes ElevenLabs to generate realistic voiceovers for each character.  
- **Image Generation:** Creates visuals using AI models like Stable Diffusion, DALL-E, and others.  
- **Music Generation:** Generates background music using AI models like MusicGen.  
- **Video Compilation:** Combines audio, visuals, and music into a cohesive video.  
- **YouTube Upload:** Automatically uploads the final video to YouTube with generated metadata.  

---

## How It Works  
1. **Data Collection:**  
   - Scrape Reddit for trending topics with high engagement.  
   - Extract key points from the discussions.  

2. **Content Generation:**  
   - Use GPT-3.5 Turbo to create a dialogue between two experts (Ahmed and Amna).  
   - Generate voiceovers for each character using ElevenLabs.  

3. **Visuals and Audio:**  
   - Create images using AI models based on topic prompts.  
   - Generate background music using AI music models.  

4. **Video Production:**  
   - Combine audio, visuals, and music into a single video file.  
   - Use video editing tools to ensure smooth transitions and synchronization.  

5. **Publishing:**  
   - Automatically generate a title, description, and tags using GPT.  
   - Upload the final video to YouTube.  

---

## Technologies Used  
- **Natural Language Processing (NLP):** GPT-3.5 Turbo for dialogue generation and metadata creation.  
- **Voice Synthesis:** ElevenLabs for realistic voice generation.  
- **Image Generation:** Stable Diffusion, DALL-E, and other Hugging Face models for creating visuals.  
- **Music Generation:** MusicGen and other Hugging Face models for background music.  
- **Video Editing:** MoviePy for combining audio, images, and music.  
- **Web Scraping:** PRAW for Reddit data extraction.  
- **YouTube API:** For uploading videos and managing metadata.  

---

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/ynstf/YouTubePodcaster.git  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Configure environment variables:  
   - Create a `.env` file in the root directory and add your API keys:  
     ```plaintext  
     # Reddit API credentials  
     CLIENT_ID="your_reddit_client_id"  
     CLIENT_SECRET="your_reddit_client_secret"  
     USER_AGENT="your_user_agent"  

     # OpenRouter API settings  
     OPENROUTER_API_KEY="your_openrouter_api_key"  
     OPENROUTER_API_URL="https://openrouter.ai/api/v1/chat/completions"  
     MODEL="gpt-3.5-turbo"  

     # ElevenLabs Constants  
     VOICE_ID_MAN="your_voice_id_man"  
     VOICE_ID_WOMAN="your_voice_id_woman"  
     AUDIO_OUTPUT_FILE="podcast/podcast_final.mp3"  

     # Hugging Face  
     HUGGING_FACE_TOKEN="your_hugging_face_token"  
     MUSIC_API_URL="https://api-inference.huggingface.co/models/facebook/musicgen-small"  
     IMAGE_API_URLS="https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev,https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image,https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"  

     # YouTube Upload  
     UPLOAD_TO_YOUTUBE="ON"  
     TOKEN_FILE_YOUTUBE="UPLOAD/token.json"  
     ```  

4. Run the pipeline:  
   ```bash  
   python main.py  
   ```  

---

## File Structure  
```plaintext  
YouTubePodcaster/  
├── AUDIO/                  # Audio generation scripts  
├── IMAGE/                  # Image generation scripts  
├── LLM/                    # Dialogue generation scripts  
├── MUSIC/                  # Music generation scripts  
├── REDDIT/                 # Reddit scraping scripts  
├── UPLOAD/                 # YouTube upload scripts  
├── VIDEO/                  # Video compilation scripts  
├── PROMPTS/                # Prompt templates for GPT  
├── podcast/                # Generated audio files and Final video output  
├── images/                 # Generated image files  
├── .env                    # Environment variables  
├── main.py                 # Main script to run the pipeline  
├── README.md               # Project documentation  
└── requirements.txt        # Python dependencies  
```  

---

## Future Improvements  
- Add support for multiple languages and automated subtitles.  
- Improve the quality of generated visuals and music.  
- Integrate with additional platforms (e.g., TikTok, Instagram).  
- Add a user-friendly interface for non-technical users.  

---

## Contributing  
Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.  

---

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

>>>>>>> d1f4886b7e2409a12a43515778cabc06f2f172f6
