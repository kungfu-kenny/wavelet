import os
import math
from datetime import datetime
import matplotlib.pyplot as plt


class WaveletFormulas:
    """
    class which is dedicated to show the wavelet values
    """
    def __init__(self) -> None:
        self.mkdir = lambda x: os.path.exists(x) or os.mkdir(x)
        self.folder_origin = os.path.dirname(os.path.abspath(__file__))
        self.get_name = lambda x, date: f"{date.strftime('%Y_%m_%d_%H_%M')}_{x}.png"

    @staticmethod
    def calculate_function_x(x) -> float:
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
        Input:  x = value which is required to transform
        Output: float value
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

    def plot_original(self, value_x:list) -> None:
        """
        Method which is dedicated to plot usual function
        Input:  value_x = list with 
        Output: we calculated
        """
        pass

    def plot_function(self, value_x:list, value_y:list=[]) -> None:
        """
        Method which is dedicated to plot original values
        Input:  value_x = list with the x values
                value_y = list with the values of the f(x)
        Output: plot was saved on the 
        """
        value_y = [self.calculate_function_x(x) for x in value_x] if not value_y else value_y


    def plot_discrete(self, value_x:list) -> None:
        """
        Method which is dedicated 
        """
        pass

    def plot_updated(self, value_x) -> None:
        """"""
        pass

    def calculate_selected_plot(self, value_choice:str, value_x:float) -> object:
        """
        High order method which creates plot depending on the type of the plot
        Input:  value_choice = string value which taks certain part of function
        Output: returns execution of selected function
        """
        value_dict = {
            'func': self.plot_function,
            'original' : self.plot_original,
            'discrete': self.plot_discrete,
            'update': self.plot_updated,
        }
        return value_dict.get(value_choice, None)(value_x)


if __name__ == '__main__':
    a = WaveletFormulas()