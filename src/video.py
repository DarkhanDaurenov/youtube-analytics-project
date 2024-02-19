import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from settings import FILE_NAME

load_dotenv(FILE_NAME)

class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self._video_id = video_id
        try:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',id=video_id).execute()
            if video_response.get('items'):
                self.title = str(video_response['items'][0]['snippet']['title'])
                self.count = str(video_response['items'][0]['statistics']['viewCount'])
                self.like_count = int(video_response['items'][0]['statistics']['likeCount'])
                self.comment_count = int(video_response['items'][0]['statistics']['commentCount'])
            else:
                self.title = None
                self.count = None
                self.like_count = None
                self.comment_count = None
        except Exception as e:
            print(f"Произошла ошибка при получении данных для видео с идентификатором. {video_id}: {e}")
            self.title = None
            self.count = None
            self.like_count = None
            self.comment_count = None

    def __str__(self):
        return f"{self.title}"

class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f"{self.title}"



