__author__ = 're9ulus'

import numpy as np
from problems import traveling_salesman_problem as TSP

class SimulatedAnnealing:

    def __init__(self, max_steps, temperature, min_energy, problem):
        self.temperature = temperature
        self.max_steps = max_steps
        self.min_energy = min_energy
        self.problem = problem

    def scheldure(self, t):
        # Temperature decreasing
        # TODO: Find how this funciton should be implemented
        return float(self.temperature) / (t + 1)

    def randomly_generate_next_state(self, state):
        x, y = np.random.randint(0, high=len(state), size=2)
        state[x], state[y] = state[y], state[x]
        return state

    def value(self, state):
        return self.problem.evaluate(state)

    def simulate(self):
        # Set state to initial state
        current_state = self.problem.generate_random_path()
        self.problem.plot_path(current_state)

        t = 1
        for t in xrange(self.max_steps):

           #print self.value(current_state)

            T = self.scheldure(t)
            if T == 0:
               break
            next_state = list(current_state)
            next_state = self.randomly_generate_next_state(next_state)

            E = self.value(current_state) - self.value(next_state)



            if E > 0:
                current_state = list(next_state)
            elif E < 0:
                threshold = 1. / (1 + np.exp(float(E) / T))
                rand_val = np.random.rand()
                if rand_val > threshold:
                    current_state = list(next_state)

        return current_state


if __name__ == '__main__':
    tsp = TSP.TravelinSalesmanProblem()
    tsp.generate_random_problem(25, 0, 100)
    tsp.plot_cities()

    si = SimulatedAnnealing(1000, 100,  1, tsp)
    solution = si.simulate()


    tsp.plot_path(solution)
    #pass