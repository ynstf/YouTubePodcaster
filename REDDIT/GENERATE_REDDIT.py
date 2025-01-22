import praw

# Function to load previously fetched subjects
def load_done_subjects(DONE_SUBJECTS_FILE):
    try:
        with open(DONE_SUBJECTS_FILE, "r") as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

# Function to save a new subject
def save_done_subject(post_id,DONE_SUBJECTS_FILE):
    with open(DONE_SUBJECTS_FILE, "a") as file:
        file.write(post_id + "\n")

# Function to save a new subject
def save_content(text,SAVE_CONTENT_FILE):
    with open(SAVE_CONTENT_FILE, "w") as file_to_save:
        file_to_save.write(text)

# Create the content
def create_content(CLIENT_ID,CLIENT_SECRET,USER_AGENT):
    # Initialize PRAW
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

    # File to store previously fetched subjects
    DONE_SUBJECTS_FILE = "done_subjects.txt"
    SAVE_CONTENT_FILE = "content.txt"
    # Fetch hot posts from the "AskReddit" subreddit
    subreddit = reddit.subreddit("AskReddit")
    posts = list(subreddit.hot(limit=100))  # Fetch 100 hot posts
    # Load previously fetched subjects
    done_subjects = load_done_subjects(DONE_SUBJECTS_FILE)
    # Filter out posts that have been fetched before
    new_posts = [post for post in posts if post.id not in done_subjects]
    if not new_posts:
        print("No new subjects found.")
        exit()
    # Select the most engaging post (e.g., highest number of comments)
    most_engaging_post = max(new_posts, key=lambda post: post.num_comments)
    # Save the post ID to avoid fetching it again
    save_done_subject(most_engaging_post.id,DONE_SUBJECTS_FILE)
    # Save the post & content
    text = ""
    for i, comment in enumerate(most_engaging_post.comments.list(), 1):
        try:
            if len(comment.body)>900:
                text += f"{comment.body}"
        except:
            pass
    save_content(text,SAVE_CONTENT_FILE)
    return text

