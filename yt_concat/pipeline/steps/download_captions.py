from yt_concat.settings import CAPTIONS_DIR
from .step import Step, StepException
import os
import sys
sys.path.append('./')


class DownloadCaptions(Step):
    def process(self, inputs, data, utils):
        for url in data:
            pass
