import tempfile
from enum import Enum

import youtube_dl


class YTDownloadFormat(Enum):
    mp3 = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    m4a = {'format': '140'}
    mp4_144p = {'format': '160+bestaudio'}
    mp4_240p = {'format': '133+bestaudio'}
    mp4_360p = {'format': '134+bestaudio'}
    mp4_480p = {'format': '135+bestaudio'}
    mp4_720p = {'format': '136+bestaudio'}
    mp4_1080p = {'format': '137+bestaudio'}
    best_video = {'format': 'bestvideo+bestaudio'}


class YoutubeDLFactory:
    def __init__(self):
        self._ydl_options = {}

    def register_options(self, download_format: str, options: dict):
        self._ydl_options[download_format] = options

    def create(self, download_format: str):
        options = self._ydl_options.get(download_format)
        if options is None:
            raise ValueError(download_format)
        return youtube_dl.YoutubeDL(options)


class DownloadHandler:
    def download(self, url: str, download_format: str):
        raise NotImplementedError


class YoutubeDownloadHandler(DownloadHandler):
    def __init__(self, format_options: dict):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.ydl_factory = YoutubeDLFactory()
        for download_format, options in format_options.items():
            updated_options = self.redirect_download_to_temp(options)
            self.ydl_factory.register_options(download_format, updated_options)

    def redirect_download_to_temp(self, ydl_options: dict) -> dict:
        if 'outtmpl' in ydl_options.keys():
            current_output = ydl_options['outtmpl']
            output_option = {'outtmpl': f'{self.temp_dir.name}/{current_output}'}
        else:
            output_option = {
                'outtmpl': f'{self.temp_dir.name}/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s'}

        ydl_options.update(output_option)
        return ydl_options

    @classmethod
    def default(cls):
        format_options = {}
        for dl_format in YTDownloadFormat:
            new_format = {dl_format.name: dl_format.value}
            format_options.update(new_format)

        return cls(format_options)

    def download(self, url: str, download_format: str):
        ydl = self.ydl_factory.create(download_format)
        ydl.download([url])
        print(self.temp_dir.name)
