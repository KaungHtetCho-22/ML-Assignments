import numpy as np

class LinearRegression:
    def __init__(self, regularization, lr, method, init_method, momentum):
        self.lr = lr
        self.method = method
        self.regularization = regularization
        self.init_method = init_method
        self.momentum = momentum

    def predict(self, X):
        return X @ self.theta 

class Normal(LinearRegression):
    def __init__(self, grad, lr, init_theta, momentum):
        super().__init__(None, lr, grad, init_theta, momentum)
