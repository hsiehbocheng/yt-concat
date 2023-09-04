import sys
sys.path.append('./') # Add the root directory to the Python path so that we can import the yt_concat package

from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps
    
    def run(self, inputs):
        for step in self.steps:
            try:
                step.process(inputs)
            except StepException as e:
                print('Exception happened: {e}')
                break
    