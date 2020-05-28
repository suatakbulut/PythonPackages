import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

class Gaussian(Distribution):

	def __init__(self, mu=0, sigma=1):
		Distribution.__init__(self, mu, sigma)


	def pdf(self, x):
		"""Probability density function calculator for the gaussian distribution.

		Args:
		x (float): point for calculating desnity function

		Returns:
		float: probability density function output		
		"""

		return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)


	def plot_histogram_pdf(self, n_spaces = 50):

		"""Function to plot the normalized histogram of the data and a plot of the 
		probability density function along the same range

		Args:
			n_spaces (int): number of data points 

		Returns:
			list: x values for the pdf plot
			list: y values for the pdf plot		
		"""
		
		mu = self.mean
		sigma = self.stdev

		min_range = min(self.data)
		max_range = max(self.data)

		# calculates the interval between x values
		interval = 1.0 * (max_range - min_range) / n_spaces

		x = []
		y = []

		# calculate the x values to visualize
		for i in range(n_spaces):
			tmp = min_range + interval*i
			x.append(tmp)
			y.append(self.pdf(tmp))

		# make the plots
		fig, axes = plt.subplots(2,sharex=True)
		fig.subplots_adjust(hspace=.5)
		axes[0].hist(self.data, density=True)
		axes[0].set_title('Normed Histogram of Data')
		axes[0].set_ylabel('Density')

		axes[1].plot(x, y)
		axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
		axes[0].set_ylabel('Density')
		plt.show()

		return x, y
		
		
	def __add__(self, other):
		
		"""Function to add together two Gaussian distributions
		
		Args:
			other (Gaussian): Gaussian instance
			
		Returns:
			Gaussian: Gaussian distribution
			
		"""
		
		result = Gaussian()
		result.mean = self.mean + other.mean
		result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
		
		return result
		
		
	def __repr__(self):
	
		"""Function to output the characteristics of the Gaussian instance
		
		Args:
			None
		
		Returns:
			string: characteristics of the Gaussian
		
		"""
		
		return "Gaussian distribution with mean {} and standard deviation {}".format(self.mean, self.stdev)

