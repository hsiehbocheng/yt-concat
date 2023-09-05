from yt_concat.settings import CAPTIONS_DIR
from .step import Step, StepException


class DownloadCaptions(Step):
    def process(self, inputs, data, utils):
        for url in data:
            pass
