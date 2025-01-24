import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define scopes
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def split_infos(video_infos):
    info = video_infos
    title = info.split('|')[0]
    description = info.split('|')[1]
    tags = info.split('|')[2]
    if ',' in tags:
        tags = info.split('|')[2].split(",")
    if '،' in tags:
        tags = info.split('|')[2].split("،")

    return title, description, tags


# Authenticate and create the API client
def get_authenticated_service(TOKEN_FILE_YOUTUBE):
    creds = None
    if TOKEN_FILE_YOUTUBE:
        print("takeing Credentials ...")
        creds = Credentials.from_authorized_user_file(TOKEN_FILE_YOUTUBE, SCOPES)
        print("i take Credentials")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "UPLOAD/client.json", SCOPES
            )
            creds = flow.run_local_server(port=8080)  # Use port 8080
        with open(TOKEN_FILE_YOUTUBE, "w") as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def share_video(youtube, title, description, tags, video_path):
    request_body = {
        "snippet": {
            "categoryId": "22",  # Category ID (e.g., 22 is for People & Blogs)
            "title":title ,
            "description":description ,
            "tags": tags,
        },
        "status": {
            "privacyStatus": "public",  # "public", "unlisted", or "private"
            "selfDeclaredMadeForKids": False,  # Explicitly declare the video is not made for kids
        },
    }

    # Path to the video file you want to upload
    #media_file = "videos/output_video.mp4"
    media_file = video_path

    # Upload the video
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=MediaFileUpload(media_file, chunksize=-1, resumable=True),
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload {int(status.progress() * 100)}%")

    print(f"Video uploaded with ID: {response['id']}")