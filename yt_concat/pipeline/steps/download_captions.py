from yt_concat.settings import CAPTIONS_DIR
from .step import Step, StepException
from yt_concat.utils import Utils
import yt_dlp

class DownloadCaptions(Step):
    def process(self, inputs, data, utils):
        CHANNEL_ID = inputs['channel_id']
        for url in data:
            ydl_opts = {
                "writesubtitles": True,
                "writeautomaticsub": True,
                "skip_download": True,
                "subtitleslangs": ["en"],
                "convertsubs": "srt",
                "outtmpl": f"{CAPTIONS_DIR}/%(id)s.%(ext)s",
                # "outtmpl": f"{CAPTIONS_DIR}/{utils.get_caption_filepath(url)}",
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            break
