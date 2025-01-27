import numpy as np
from optimizer import Optimizer
from linear import Linear


class SGD(Optimizer):
    def __init__(self, learning_rate=1e-2):
        super(SGD, self).__init__(learning_rate)

    def update(self, module):
        if not (isinstance(module, Linear)):
            return  # the only module that contains trainable parameters is linear module.

        # todo: implement sgd update rule for Linear module.