import tempfile
from pathlib import Path

import youtube_dl


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
        mp3_settings = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        format_options = {'mp3': mp3_settings}

        return cls(format_options)

    def download(self, url: str, download_format: str):
        ydl = self.ydl_factory.create(download_format)
        ydl.download([url])
        print(self.temp_dir.name)
