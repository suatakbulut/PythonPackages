import math
import matplotlib.pyplot as plt

class Distribution: 

    def __init__(self, mu=0, sigma=1):
        """
        Generic two parameters, (mean, standard deviation), 
        distribution class for calculating and visualizing 
        a probability distribution

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data (list of floats) a list of floats extracted from the data file
            """
        self.mean = mu
        self.stdev = sigma
        self.data = []

    
    def read_data_file(self, file_name):
        """ Function to read in data from a txt file. The txt file should have 
        one number (float) per line. The numbers are stored in the data attribute
        as a list.

        Args:
            file_name (string): name of the file to read from

        Returns:
            None
        """

        with open(file_name) as f:
            data_list = []
            line = f.readline()
            while line:
                data.append(float(line))
                line = f.readline()


        self.data = data 


    def calculate_mean(self):
    
        """Function to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
                    
        avg = 1.0 * sum(self.data) / len(self.data)
        
        self.mean = avg
        
        return self.mean


    def calculate_stdev(self, sample=True):

        """Function to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
    
        mean = self.mean
    
        sigma = 0
    
        for d in self.data:
            sigma += (d - mean) ** 2
        
        sigma = math.sqrt(sigma / n)
    
        self.stdev = sigma
        
        return self.stdev

    
    def plot_histogram(self):
        """Function to ouput a histogram of the instance variable data 
        using matplotlib.pyplot library

        Args:
            None

        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')


