from pytube import YouTube
from pytube import Search
import logging

logging.getLogger('pytube').setLevel(logging.ERROR)

class Video:
    def __init__(self, title, url):
        self.title = title
        self.url = url

    @classmethod
    def from_url(cls, url):
        pass

    @classmethod
    def from_title(cls, title):
        search = Search(title).results
        title_video = search[0].title
        link_video = search[0].watch_url
        return [title_video, link_video]
