#!/usr/bin/env python3

# Language: Python 3.10.8
# IDE/code editor: NVIM 0.8.0
# Testing framework: unittest Python module

import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_easy(self):
        self.assertEqual(calculator.calc("5 7 2"), 14)


    def test_empty(self):
        self.assertEqual(calculator.calc(""), 0)


    def test_none(self):
        self.assertEqual(calculator.calc(None), 0)


    def test_int(self):
        self.assertEqual(calculator.calc(23), 0)


    def test_spaces(self):
        self.assertEqual(calculator.calc("4 5   2 1"), 12)


    def test_slash(self):
        self.assertEqual(calculator.calc("2 / 4"), 6)


    def test_difficult(self):
        self.assertEqual(calculator.calc("+2.1 -0./-4.0;2{{9"), 9.1)

if __name__ == '__main__':
    unittest.main()
