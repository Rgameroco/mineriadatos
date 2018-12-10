import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math
import csv
class Lin_reg():

    def __init__(self, X, Y):
        """
        :param X: lista con los valores de la variable de las abscisas
        :param y: lista con los valores de la variable de las ordenadas
        """
        self.X = X
        self.y = Y
        self.N = len(self.X)
        self.X_mean = sum(self.X) / len(self.X)
        self.y_mean = sum(self.y) / len(self.y)
        self.X_std = (1 / (self.N - 1) * sum((ele - self.X_mean) ** 2
                                             for ele in self.X)) ** 0.5
        self.y_std = (1 / (self.N - 1) * sum((ele - self.y_mean) ** 2
                                             for ele in self.y)) ** 0.5
        self.X_var = self.X_std ** 2
        self.y_var = self.y_std ** 2
        self.cov = sum([i * j for (i, j) in zip([ele - self.X_mean for ele in self.X],
                                                [ele - self.y_mean for ele in self.y])]) / (self.N)

        self.r = self.cov / (self.X_std * self.y_std)

    def Coeficientes(self):
        if len(self.X) != len(self.y):
            raise ValueError('unequal length')
        self.b = self.cov / self.X_var
        self.a = self.y_mean - (self.b * self.X_mean)
        return self.a, self.b

    def predict(self, X):
        yp = []
        for x in X:
            yp.append(self.a + self.b * x)
        return yp