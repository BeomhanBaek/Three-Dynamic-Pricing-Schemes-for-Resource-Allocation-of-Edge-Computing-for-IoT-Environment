import numpy as np


class Buyer:
    def __init__(self, R, mu, C, Fmax):

        self.R = R
        self.mu = mu
        self.F = 0
        self.w = 0
        self.utility = 0
        self.C = C
        self.Fmax = Fmax

    def compute_utility(self, a):
        self.w = a
        return -self.R*self.C/self.F - self.mu*self.w

    def set_utility(self, w):
        self.utility = self.compute_utility(w)
