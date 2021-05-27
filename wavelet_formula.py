import os
import math
from datetime import datetime
import matplotlib.pyplot as plt


class WaveletFormulas:
    """
    class which is dedicated to show the wavelet values
    """
    def __init__(self) -> None:
        self.img = 'img'
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
        return math.sin(math.radians(x))

    @staticmethod
    def calculate_wavelet_func(x:float) -> float:
        """
        Static method which calcuates basic wavelet function
        Input:  x = value which is required to transform
        Output: float value
        """
        if 0 <= x <= 0.5:
            return 1
        elif 0.5 < x <= 1:
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

    def plot_original(self, value_x:list, value_y:list=[], *_) -> None:
        """
        Method which is dedicated to plot usual function
        Input:  value_x = list with x values
                value_y = list of the y values
        Output: we calculated
        """
        func = 'original'
        self.folder_func = os.path.join(self.folder_img, func)
        self.mkdir(self.folder_func)
        value_y = [self.calculate_wavelet_func(x) for x in value_x] if not value_y else value_y
        plt.rcParams["figure.figsize"] = (20,5)
        plt.plot(value_x, value_y)
        plt.savefig(os.path.join(self.folder_func, self.get_name(func, self.datetime)))
        plt.close()

    def plot_function(self, value_x:list, value_y:list=[], *_) -> None:
        """
        Method which is dedicated to plot original values
        Input:  value_x = list with the x values
                value_y = list with the values of the f(x)
        Output: plot was saved on the 
        """
        func = 'function'
        self.folder_func = os.path.join(self.folder_img, func)
        self.mkdir(self.folder_func)
        value_y = [self.calculate_function_x(x) for x in value_x] if not value_y else value_y
        plt.rcParams["figure.figsize"] = (20,5)
        plt.plot(value_x, value_y)
        plt.savefig(os.path.join(self.folder_func, self.get_name(func, self.datetime)))
        plt.close()


    def plot_discrete(self, value_x:list, value_y:list=[]) -> None:
        """
        Method which is dedicated to plot discrete function
        Input:  value_x = x values
                value_y = y value of the x format
        Output: save
        """
        pass

    def plot_updated(self, value_x:list, value_y:list) -> None:
        """
        Method which is dedicated to plot updated function
        Input:  value_x = list with x values
                value_y = list with y values
        Output: saved plot values
        """
        pass

    def plot_basic(self, value_x:list, value_y:list, *kwargs:set) -> None:
        """
        Method which is dedicated to plot basic values of the basic wavelet
        Input:  value_x = list with x values
                value_y = list with y values
        Output: plots which is dedicated
        """
        m, n = kwargs
        func = 'basic'
        self.folder_func = os.path.join(self.folder_img, func)
        self.mkdir(self.folder_func)
        value_y = [self.calculate_wavelet_basic(x, m, n) for x in value_x for x in value_x] if not value_y else value_y
        plt.rcParams["figure.figsize"] = (20,5)
        plt.plot(value_x, value_y)
        plt.savefig(os.path.join(self.folder_func, self.get_name(func, self.datetime)))
        plt.close()

    def calculate_selected_plot(self, value_choice:str, value_x:list, value_y:list, *kwargs) -> object:
        """
        High order method which creates plot depending on the type of the plot
        Input:  value_choice = string value which taks certain part of function
                value_x = list with the x values
                value_y = list with the y values
        Output: returns execution of selected function
        """
        value_dict = {
            'function': self.plot_function,
            'original' : self.plot_original,
            'basic': self.plot_basic,
            'discrete': self.plot_discrete,
            'update': self.plot_updated,
        }
        return value_dict.get(value_choice, None)(value_x, value_y, *kwargs)

    def make_test(self):
        """
        Method to make tests
        Input:  None
        Output: None
        """
        self.folder_img = os.path.join(self.folder_origin, self.img)
        self.datetime = datetime.utcnow()
        self.mkdir(self.folder_img)
        value_x = [x for x in range(7201)]
        value_y = [self.calculate_function_x(x) for x in value_x]
        self.calculate_selected_plot('function', value_x, value_y)
        value_x =[0.01*x for x in range(101)]
        value_y = [self.calculate_wavelet_func(x) for x in value_x]
        self.calculate_selected_plot('original', value_x, value_y)
        m, n = 3, 4
        value_x = [0.01*x for x in range(101)] 
        value_y = [self.calculate_wavelet_basic(x, m, n) for x in value_x] * (10)
        # value_y = [self.calculate_wavelet_basic(x, m, n) for x in value_x]
        self.calculate_selected_plot('basic', [x for x in range(len(value_y))], value_y, m, n)

if __name__ == '__main__':
    a = WaveletFormulas()
    a.make_test()