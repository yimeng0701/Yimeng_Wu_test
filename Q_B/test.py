# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:28:17 2019

@author: prettyyang2
"""
from compareVersion import Solution
import unittest
S = Solution()

class TestSolution(unittest.TestCase):
    """Test two functions: checkInput and compareVersion"""
    def test_checkInput(self):
        self.assertEqual(True,S.checkInput("1 1.0"))
        self.assertEqual(True,S.checkInput("0 1.0001.001"))
        self.assertEqual(True,S.checkInput("v1.2.3 1.0.6"))
        self.assertEqual(True,S.checkInput("3.1.5a 2.7"))
        self.assertEqual(True,S.checkInput("10.2 10.2.5d"))
        self.assertEqual(False,S.checkInput("5.a.6b 3.7"))
        self.assertEqual(False,S.checkInput("2.7.3-a 1.0.0"))
        self.assertEqual(False,S.checkInput("a.b.v 9.5.6"))
        self.assertEqual(False,S.checkInput("3.1.5A 3.1.5a"))
        self.assertEqual(False,S.checkInput("2.1.3-alpha 10.0"))
    def test_compareVersion(self):
        self.assertEqual("0.1 is less than 1.5" ,S.compareVersion("0.1 1.5"))
        self.assertEqual("1.0 is equal to 1" ,S.compareVersion("1.0 1"))
        self.assertEqual("1.0.1 is equal to 1.0.1.0" ,S.compareVersion("1.0.1 1.0.1.0"))
        self.assertEqual("1.0 is less than 1.001" ,S.compareVersion("1.0 1.001"))
        self.assertEqual("v1.0 is less than v1.001" ,S.compareVersion("v1.0 v1.001"))
        self.assertEqual("1.2.1 is greater than 1.2.1b" ,S.compareVersion("1.2.1 1.2.1b"))
        self.assertEqual("1.3.1 is greater than 1.2.1b" ,S.compareVersion("1.3.1 1.2.1b"))
        self.assertEqual("3.7b is greater than 1.2.1b" ,S.compareVersion("3.7b 1.2.1b"))
        self.assertEqual("5 is greater than 5.0.0b" ,S.compareVersion("5 5.0.0b"))
        self.assertEqual("3.2.5 is less than 3.2.7" ,S.compareVersion("3.2.5 3.2.7"))

if __name__ == '__main__':
    unittest.main()
        



