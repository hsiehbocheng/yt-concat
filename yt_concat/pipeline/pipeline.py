from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps
    
    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(inputs=inputs, data=data, utils=utils)
            except StepException as e:
                print(f'Exception happened: {e}')
                break
    