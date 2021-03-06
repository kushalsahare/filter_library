#!/usr/bin/env python

from collections import deque
import numpy as np


class TemporalMedianFilter():
    """Temporal Median Filter Class
       The temporal median filter class returns the median of the current and
       the previous D scans
       
       y_i(t) = median(x_i(t), x_i(t-1), ..., x_i(t-D))
       where
       x: input of length-N scans and i ranges from 0 to N-1
       
       x = [x_0, x_1, ....., x_(N-1)] laser data
       y = [y_0, y_1, ....., y_(N-1)]
       
       
       Parameters
       ----------
       N : int
        length of an array 
       
       D : int
        number of previous scans to be considered
      
       Returns
       -------
       y: filtered array of length-N
       
     """ 

    def __init__(self, N, D):
        """Init method for the class
        takes the arguments and defines the class members.
        this class uses a deque of length D to keep the previous D+1 scans
        Args:
            N (int): length of the scan, default is 5
            D (int): Number of previous scans to be considered
        """
        self.N = N
        self.D = D
        self.data = np.zeros(N)
        
        self.data_queue = deque([], self.D+1)

    def update(self, data):
        """
        Update method takes the current data, enques it, finds the median and
        returns the filtered scan
        
        Args:
          data(float array): actual laser data array of length N
        Returns:
          self.data (float array): Filtered array of length N
        """
        self.data_queue.append(data)
       
        data_array = np.array(self.data_queue)
        
        # axis=0 for taking median along the columns
        self.data = np.median(data_array, axis=0)
       
        return self.data


if __name__ == "__main__":
    data = [[0., 1., 2., 1., 3.],
            [1., 5., 7., 1., 3.],
            [2., 3., 4., 1., 0.],
            [3., 3., 3., 1., 3.],
            [10.,2., 4., 0., 0.]]
    tm_filter = TemporalMedianFilter(len(data[0]),3)

    for i in range(len(data)):
        data_filtered= tm_filter.update(data[i])
        print data_filtered
        # print "----------"
