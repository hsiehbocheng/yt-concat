import sys
sys.path.append('./') # Add the root directory to the Python path so that we can import the yt_concat package


from yt_concat.pipeline.steps.get_videos_from_channel import GetVideoList
from yt_concat.pipeline.steps.download_captions import DownloadCaptions
from yt_concat.pipeline.steps.step import StepException
from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.pipeline.steps.preflight import Preflight
from yt_concat.pipeline.steps.postflight import Postflight
from yt_concat.utils import Utils

CHENNEL_ID = 'UCcabW7890RKJzL968QWEykA'

def main():
    inputs = {
        'channel_id': CHENNEL_ID
    }

    steps = [
        Preflight(),
        # GetVideoList(),
        # DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
    # print(sys.path)