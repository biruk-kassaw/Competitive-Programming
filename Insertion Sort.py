#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    element = arr[n-1]
    n = n-2
    while n >= 0 and arr[n] > element:
        arr[n+1] = arr[n]
        print(*arr)
        n -= 1
    arr[n+1] = element
    print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
