#!/usr/bin/env python


import os


def test_simple():
    here = os.path.dirname(os.path.realpath(__file__))
    main = os.path.join(here, "main.py")
    assert os.path.isfile(main)


if __name__ == "__main__":
    test_simple()
    print("Test passed. main.py file exists.")
