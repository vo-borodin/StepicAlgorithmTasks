# Число инверсий в массиве

# https://goo.gl/PGTZ3q

import math
import array

inv = 0

def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    m = len(numbers) // 2
    return __merge(merge_sort(numbers[0:m]), merge_sort(numbers[m:]))


def __merge(a1, a2):
    global inv
    merged = array.array('L', [0] * (len(a1) + len(a2)))
    i = j = m = value = 0
    while m < len(merged):
        if i < len(a1) and j < len(a2):
            if a1[i] <= a2[j]:
                value = a1[i]
                i += 1
            else:
                value = a2[j]
                j += 1
                inv += (len(a1) - i)
            merged[m] = value
        else:
            if i == len(a1):
                merged[m] = a2[j]
                j += 1
            elif j == len(a2):
                merged[m] = a1[i]
                i += 1
        m += 1
    return merged


def count_inversions(numbers):
    global inv
    inv = 0
    merge_sort(numbers)
    return inv


def main():
    n = int(input())
    numbers = array.array('L', list(map(int, input().split(" "))))
    print (count_inversions(numbers))


if __name__ == "__main__":
    main()

"""
Sample Input:
5
2 3 9 2 9
Sample Output:
2
"""
