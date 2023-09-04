import sys
sys.path.append('./') # Add the root directory to the Python path so that we can import the yt_concat package


from yt_concat.pipeline.steps.get_videos_from_channel import GetVieosList
from yt_concat.pipeline.steps.step import StepException
from yt_concat.pipeline import Pipeline

CHENNEL_ID = 'UCcabW7890RKJzL968QWEykA'

def main():
    inputs = {
        'channel_id': CHENNEL_ID
    }

    steps = [
        GetVieosList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
    # print(sys.path)