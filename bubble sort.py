#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swaps = 0
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                swaps += 1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    last = a[len(a)-1]
    first = a[0]
    print('Array is sorted in '+ str(swaps) +' swaps.')
    print('First Element: '+ str(first))
    print('Last Element: '+str(last))
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
