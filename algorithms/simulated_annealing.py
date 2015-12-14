__author__ = 're9ulus'

import numpy as np

class simulated_annealing:

    def __init__(self, temperature, max_steps, min_energy):
        self.temperature = temperature
        self.max_steps = max_steps
        self.min_energy = min_energy

    def update_temperatuer(self, current_step):
        raise 'ERROR: Not implemented'

    def simulate(self):
        raise 'ERROR: Not implemented'
        # Set state to initial state
        for k in xrange(self.max_steps):
            t = self.update_temperature(k)
            # Pick random neighbour
            # If probability: move to new state
        # Output final state


if __name__ == '__main__':
    pass