# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:39:20 2019

@author: prettyyang2
"""

from overlap import Solution
import unittest
S = Solution()

class TestSolution(unittest.TestCase):
    """Test two functions: checkInput and compareVersion"""
    def test_overlap(self):
        self.assertEqual(False ,S.overlap((1,5),(6,8)))
        self.assertEqual(True ,S.overlap((1,5),(2,6)))
        self.assertEqual(True, S.overlap((-5.634563464,4.3123424),(-10.61324,-2.123131)))
        self.assertEqual(True, S.overlap((-10.61324,-2.123131),(-5.634563464,4.3123424)))
        self.assertEqual(True ,S.overlap((10,7),(20,3)))
        self.assertEqual(False ,S.overlap((-9.01,-3.228),(-2.18,5)))
        self.assertEqual(False ,S.overlap((-2.18,5),(-9.01,-3.228)))
        self.assertEqual(True ,S.overlap((0,-1.76),(-1.0004,9)))
        self.assertEqual(True ,S.overlap((2,100),(3,6)))
        self.assertEqual(False ,S.overlap((-2,9),(-3.7,-2.01)))

if __name__ == '__main__':
    unittest.main()