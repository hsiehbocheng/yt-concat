import os
import sys
sys.path.append('./')
from .step import Step, StepException
from yt_concat.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, inputs, data, utils):
        for url in data:
            pass