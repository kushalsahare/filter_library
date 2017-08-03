#!/usr/bin/env python

import numpy as np

class RangeFilter():

    def __init__(self, N, dist_range):
        self.N = N
        self.range = dist_range
        self.data = np.zeros(N)

    def update(self, data):
        self.data = np.clip(data, np.amin(self.range), np.amax(self.range))
        return self.data


if __name__ == "__main__":

    range_filter = RangeFilter(10,[0.03,50])
    N = 10
    for i in range(10):
            data = np.random.rand(N)*0 + 0.0
            print data
            data = range_filter.update(data)
            print data
            print "----------"
