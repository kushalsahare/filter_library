#!/usr/bin/env python

import numpy as np


class RangeFilter:
    """Range Filter Class
           The Range filter crops all the values that are below range_min
           (resp. above range_max), and replaces them with with the range_min
           value(resp. range_max)

           y_i(t) = median(x_i(t), x_i(t-1), ..., x_i(t-D))
           where
           x: input of length-N scans and i ranges from 0 to N-1

           x = [x_0, x_1, ....., x_(N-1)] laser data
           y = [y_0, y_1, ....., y_(N-1)]


           Parameters
           ----------
           N : int
            length of an array

           dist_range: array of floats
              range of [0.03, 50] meters

           Returns
           -------
           y: filtered array of length-N

         """
    def __init__(self, N=5, dist_range=[0.03,50]):
        """Init method for the class
                takes the arguments and defines the class members.
                Args:
                    N (int): length of the scan, default is 5
                    D (array of floats): [range_min, range_max]
        """
        self.N = N
        self.range = dist_range
        self.data = np.zeros(N)

    def update(self, laser_data):
        """
        Update method takes the current data and clips it to
        range_max (or range_min) as explained above
        Args:
          laser_data(float array): actual laser data array of length N
        Returns:
          self.data (float array): Filtered array of length N
        """
        self.data = np.clip(laser_data, np.amin(self.range), np.amax(self.range))
        return self.data


if __name__ == "__main__":

    N = 5
    range_filter = RangeFilter(N,[0.03,50])

    for i in range(10):
            data = np.random.rand(N)*0 + 0.0
            print data
            data = range_filter.update(data)
            print data
            print "----------"
