import sys
sys.path.append('./') # Add the root directory to the Python path so that we can import the yt_concat package

from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps
    
    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                step.process(inputs=inputs, data=data, utils=utils)
            except StepException as e:
                print(f'Exception happened: {e}')
                break
    