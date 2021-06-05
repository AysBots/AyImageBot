#!/usr/bin/env python


import os


def simple_test():
    here = os.path.dirname(os.path.realpath(__file__))
    main = os.path.join(here, "main.py")
    assert os.path.isfile(main)


if __name__ == "__main__":
    simple_test()
    print("Test passed. main.py file exists.")
