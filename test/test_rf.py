#!usr/bin/env python
# -*- coding: utf-8 -*-

from filters import range_filter as rf
import numpy as np
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_min(self):
        """ Test for the minimum range"""
        N = 10
        dist_range =[0.03, 50]
        RF = rf.RangeFilter(N, dist_range)
        data = np.zeros(N)
        min_data = np.ones(N)*0.03
        self.assertEqual(tuple(RF.update(data)), tuple(min_data))

    def test_max(self):
        """ Test for the maximum range"""
        N = 10
        dist_range =[0.03, 50]
        RF = rf.RangeFilter(N, dist_range)
        data = np.ones(N)*1000
        min_data = np.ones(N)*np.amax(dist_range)
        self.assertEqual(tuple(RF.update(data)), tuple(min_data))


if __name__ == '__main__':
    unittest.main()
