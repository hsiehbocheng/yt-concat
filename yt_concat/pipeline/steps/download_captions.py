from yt_concat.settings import CAPTIONS_DIR
from .step import Step, StepException
import yt_dlp

class DownloadCaptions(Step):
    def process(self, inputs, data, utils):
        for url in data:
            ydl_opts = {
                "writesubtitles": True,
                "writeautomaticsub": True,
                "skip_download": True,
                "subtitleslangs": ["en"],
                "convertsubs": "srt",
                "outtmpl": f"{CAPTIONS_DIR}/%(id)s",
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            break

