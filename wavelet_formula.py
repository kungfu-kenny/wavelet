import os
import math
import matplotlib.pyplot as plt


class WaveletFormulas:
    """
    class which is dedicated to show the wavelet values
    """
    def __init__(self, list_x:list) -> None:
        self.list_x = list_x

    @staticmethod
    def calculat_function_x(x) -> float:
        """
        Static method which is dedicated to get some values of the function
        Input:  x = value of the x
        Output: f(x) value which currently is sin(x)
        """
        return math.sin(x)

    @staticmethod
    def calculate_wavelet_func(x:float) -> float:
        """
        Static method which calcuates basic wavelet function
        Input:  x - value which is required to transform
        Output: float values
        """
        if 0 <= x < 0.5:
            return 1
        elif 0.5 <= x < 1:
            return -1
        return 0

    def calculate_wavelet_basic(self, x:float, k:int, j:int) -> float:
        """
        Method which calcutes wavelet transition
        Input:  x = value x which main argument of the calculation
                k = index 1
                j = index 2
        Output: value of the wavlet transition
        """
        return (2**(j/2))*self.calculate_wavelet_func((2**j)*x - k)

    def calculate_wavelet_updated(self, x:float, a:int, b:int) -> float:
        """
        Method which calculates wavelet in cases of the 
        Input:  x = value x which we are taking for a function
                a = 
                b =
        Output: float value
        """
        return (abs(a)**-0.5)*self.calculate_wavelet_func((x - b)/a)

    def calculate_wavelet_discrete(self, x, b, a) -> float:
        """
        Method which is dedicated to calculate discrete 
        Input:  x = value which we require to a function
                b = 
                a = 
        Output: calculated value of F[a, b]
        """
        pass

    def calculate_selected_plot(self, value_choice:str) -> object:
        """
        High order method which creates plot depending on the type of the plot
        Input:  value_choice = string value which taks certain part of function
        Output: returns execution of selected function
        """
        pass

if __name__ == '__main__':
    a = WaveletFormulas([])