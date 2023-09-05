from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps
    
    def run(self, inputs, utils):
        data = None # data 初始值為 None, 因為一開始下載資料並不需要 data, 但後續會依序傳遞下去
        for step in self.steps:
            try:
                data = step.process(inputs=inputs, data=data, utils=utils)
            except StepException as e:
                print(f'Exception happened: {e}')
                break
    