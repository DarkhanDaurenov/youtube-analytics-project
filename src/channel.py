from googleapiclient.discovery import build
import os
import json
from pprint import pprint
from dotenv import load_dotenv
from settings import FILE_NAME
load_dotenv(FILE_NAME)


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self._channel = None
        self._url = f"https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"

    @property
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = self.youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        pprint(self.channel)


    @property
    def title(self):
        if not self._channel:
            self.print_info
        return self.channel['items'][0]['snippet']['localized']['title']


    @property
    def video_count(self):
        if not self._channel:
            self.print_info
        return self.channel['items'][0]['statistics']['videoCount']


    @property
    def url(self):
        return self._url


    @property
    def channel_id(self):
        return self.channel_id



    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, filename: str) -> None:
        data = {
            "id_channel": self._channel_id,
            "title": self.title,
            "video_count": self.video_count,
            "url": self._url
        }
        with open('moscowpython.json', 'w') as file:
            json.dump(data, file)
