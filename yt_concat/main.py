import os
from yt_concat.pipeline.steps.get_videos_from_channel import GetVideoList
from yt_concat.pipeline.steps.download_captions import DownloadCaptions
from yt_concat.pipeline.steps.step import StepException
from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.pipeline.steps.preflight import Preflight
from yt_concat.pipeline.steps.postflight import Postflight
from yt_concat.utils import Utils
from yt_concat.settings import DOWNLOADS_DIR, CAPTIONS_DIR, VIDEOS_DIR

CHENNEL_ID = 'UCcabW7890RKJzL968QWEykA'
GET_VIDEO_LIST_OR_NOT = not os.path.exists(
    os.path.join(VIDEOS_DIR, CHENNEL_ID + '.txt')
) # 如果存在該 Channel 的 Video List 就不重新抓, 防止達到 API 上限

def main():
    inputs = {
        'channel_id': CHENNEL_ID,
        'get_video_list': GET_VIDEO_LIST_OR_NOT,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        # DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs=inputs, utils=utils)

if __name__ == '__main__':
    main()
    print(GET_VIDEO_LIST_OR_NOT)