# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    ins = sorted([a, b, c])

    # require that the input values be >= 0 and <= 200
    if ins[0] > 200 or ins[1] > 200 or ins[2] > 200:
        return 'InvalidInput'

    if ins[0] <= 0 or ins[1] <= 0 or ins[2] <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (ins[0] >= (ins[1] + ins[2])) or (ins[1] >= (ins[0] + ins[2])) or (ins[2] >= (ins[0] + ins[1])):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if ins[0] == ins[1] and ins[1] == ins[2] and ins[2] == ins[0]:
        return 'Equilateral'
    elif ((ins[0] ** 2) + (ins[1] ** 2)) == (ins[2] ** 2):
        return 'Right'
    elif (ins[0] != ins[1]) and (ins[1] != ins[2]) and (ins[0] != ins[1]):
        return 'Scalene'
    else:
        return 'Isosceles'
