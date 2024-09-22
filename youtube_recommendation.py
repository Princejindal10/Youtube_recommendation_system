from authenticator import authenticate_user
from googleapiclient.discovery import build

def get_recommendations(credentials):
    print("Fetching recommendations...")  # Debug statement
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request = youtube.videos().list(
        part='snippet',
        chart='mostPopular',
        maxResults=10,
        regionCode='US'
    )
    response = request.execute()
    
    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']
        print(f"Title: {title}, URL: https://www.youtube.com/watch?v={video_id}")

if __name__ == "__main__":
    print("Authenticating user...")  # Debug statement
    credentials = authenticate_user()
    print("User authenticated.")  # Debug statement
    get_recommendations(credentials)