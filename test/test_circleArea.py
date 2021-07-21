import unittest
from src.circle import circleArea
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circleArea(1), pi)
        self.assertEqual(circleArea(0), 0)
        self.assertEqual(circleArea(2.34).__round__(2), 17.20)

    def test_negativeRadius(self):
        self.assertRaises(ValueError, circleArea, -2.0)

    def test_invalidDataType(self):
        self.assertRaises(TypeError, circleArea, -2.0+3j) # complex radius
        self.assertRaises(TypeError, circleArea, "hello") # string radius
        self.assertRaises(TypeError, circleArea, None) # none radius
        self.assertRaises(TypeError, circleArea, True) # complex radius
        self.assertRaises(TypeError, circleArea, False) # complex radius
        
