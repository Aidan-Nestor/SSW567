# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', '3,5,4 is a Right triangle')

    def testInputs(self):
        self.assertEqual(classifyTriangle("5", [3, 2], 4), 'InvalidInput', '5,3,4 contains a invalid inputs')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testSizingA(self):
        self.assertEqual(classifyTriangle(5, 1, 1), 'NotATriangle', '5,1,1 is not a valid triangle')

    def testSizingB(self):
        self.assertEqual(classifyTriangle(1, 5, 1), 'NotATriangle', '1,5,1 is not a valid triangle')

    def testSizingC(self):
        self.assertEqual(classifyTriangle(1, 1, 5), 'NotATriangle', '1,1,5 is not a valid triangle')

    def testIsosceles(self):
        self.assertEqual(classifyTriangle(5, 5, 6), 'Isosceles', '5,5,6 is an isosceles triangle')

    def testBoundsA(self):
        self.assertEqual(classifyTriangle(200, 250, 250), 'InvalidInput', '200,250,250 is outside the bounds')

    def testBoundsB(self):
        self.assertEqual(classifyTriangle(-200, -250, -250), 'InvalidInput', '-200,-250,-250 is outside the bounds')

    def testScalene(self):
        self.assertEqual(classifyTriangle(18, 28, 38), 'Scalene', '18,28,38 is a scalene triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

