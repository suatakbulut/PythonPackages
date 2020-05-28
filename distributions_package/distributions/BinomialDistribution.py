import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

class Binomial(Distribution):
	""" Binomail dist'n class for calculating and 
	visualizing binomial dist'n.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data (list of floats) a list of floats extracted from the data file
            p (float) the probability of success
            n (int) the toal number of trials
            """

	def __init__(self, prob=0.5, size=20):

		self.p = prob
		self.n = size 

		Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())


    def __add__(self, other): 

        try: 
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error: 
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result


    def __repr__(self): 

        """Function to output the characteristics of the Binomial instance

        Args:
        None

        Returns:
        string: characteristics of the Gaussian

        """

        return "mean {}, standard deviation {}, p {}, n {}".\
        format(self.mean, self.stdev, self.p, self.n)   	