#!/usr/bin/env python
"""
Author: Su Na <sunamask@gmail.com>
Xit, here we go again.
"""

# import numpy as np
# import pandas as pd
import argparse as ap


def get_args():
    """Read commmand line arguments"""

    args = ap.ArgumentParser(description="Say hello")
    args.add_argument('-n',
                      '--name',
                      metavar='name',
                      default='World',
                      help="Name to greet")
    return args.parse_args()


def main():
    """Say hello to the fuking fuk"""

    args = get_args()

    # print("xit happens, yet life goes on.")
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
