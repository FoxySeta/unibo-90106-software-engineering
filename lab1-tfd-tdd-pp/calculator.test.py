#!/usr/bin/env python3

import calculator


def test(s, exp):
    assert calculator.calc(s) == exp, \
    f'{exp} expected, {calculator.calc(s)} found'


def test_easy():
    test("5 7 2", 14)


def test_empty():
    test("", 0)


def test_none():
    test(None, 0)


def test_int():
    test(23, 0)


def test_spaces():
    test("4 5   2 1", 12)


def test_slash():
    test("2 / 4", 6)


def test_difficult():
    test("+2.1 -0./-4.0;2{{9", 9.1)


if __name__ == "__main__":
    test_easy()
    test_empty()
    test_none()
    test_int()
    test_spaces()
    test_slash()
    test_difficult()
    print("Everything passed")
