#!usr/bin/env python
# -*- coding: utf-8 -*-

from filters import temporal_median_filter as tmf
import unittest

class RFTestSuite(unittest.TestCase):
    """Basic test cases."""
       
    def test_data(self):
        """ Test if the data is equal to expected"""
        
        laser_data = [ [0., 1., 2., 1., 3.],
                       [1., 5., 7., 1., 3.],
                       [2., 3., 4., 1., 0.],
                       [3., 3., 3., 1., 3.],
                       [10.,2., 4., 0., 0.]]
        TMF = tmf.TemporalMedianFilter(len(laser_data[0]),3)
                       
        expected_filtered = [ [0.0,  1.0, 2.0,  1.0, 3.0],
                              [0.5,  3.0, 4.5,  1.0, 3.0],
                              [1.0,  3.0, 4.0,  1.0, 3.0],
                              [1.5,  3.0, 3.5,  1.0, 3.0],
                              [2.5,  3.0, 4.0,  1.0, 1.5]
                            ]
        data = []
        for i in range(len(laser_data)):
              data.append(TMF.update(laser_data[i]))
              self.assertEqual( tuple(data[i]),tuple(expected_filtered[i]))

if __name__ == '__main__':
    unittest.main()
