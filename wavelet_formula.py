import os
import matplotlib.pyplot as plt


class WaveletFormulas:
    """
    class which is dedicated to show the wavelet values
    """
    def __init__(self, list_x:list) -> None:
        self.list_x = list_x

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

    def calculate_wavelet_(self, x:float, k:int, j:int) -> float:
        """
        Method which calcutes wavelet transition
        Input:  x = value x which main argument of the calculation
                k = index 1
                j = index 2
        Output: value of the wavlet transition
        """
        return (2**(j/2))*self.calculate_wavelet_func((2**j)*x - k)

    def calculate_wavele_updated(self, x:float, a:int, b:int) -> float:
        """
        Method which calculates wavelet in cases of the 
        Input:  x = value x which we are taking for a function
                a = 
                b =
        Output: float value
        """
        return (abs(a)**-0.5)*self.calculate_wavelet_func((x - b)/a)

    def calculate_selected_plot(self, value_choice:str) -> object:
        """"""
        pass