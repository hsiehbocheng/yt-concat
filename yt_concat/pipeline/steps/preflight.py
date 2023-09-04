import sys
sys.path.append('./')

from .step import Step
from yt_concat.utils import Utils
from yt_concat.settings import DOWNLOADS_DIR, CAPTIONS_DIR, VIDEOS_DIR


class Preflight(Step):
    def process(self, utils, inputs=None, data=None):
        print('in Preflight: making directories')
        utils.create_dirs()