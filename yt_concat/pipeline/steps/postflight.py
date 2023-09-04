from .step import Step
import sys
sys.path.append('./')
class Postflight(Step):
    def process(self, inputs, data=None, utils=None):
        print('in Postflight')
