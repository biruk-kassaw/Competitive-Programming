#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
# UDDDUDUU

def countingValleys(steps, path):
    # Write your code here
    u = 0
    d = 0
    valleys = 0
    added = False
    for i in path:
        if i == "U":
            u += 1
        else:
            d += 1
        if d > u and not added:
            valleys += 1
            added = True
        elif d <= u:
            added = False
    return valleys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
