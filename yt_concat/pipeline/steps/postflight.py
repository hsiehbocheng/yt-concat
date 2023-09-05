from .step import Step


class Postflight(Step):
    def process(self, inputs=None, data=None, utils=None):
        print('in Postflight')
