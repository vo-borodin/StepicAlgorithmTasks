# Наибольшая невозрастающая подпоследовательность

# https://goo.gl/VfWNUA

import random

def solution(a):
    if len(a) <= 1:
        return a
    size = len(a)
    d = [-1000000001] * (size + 1)
    d[0] = 1000000001
    pos = [0] * (size + 1)
    pos[0] = -1
    prev = [0] * size

    length = 0
    for i in range(size):
        j = bin_search(d, a[i])
        #print("j={0}".format(j))
        if d[j - 1] >= a[i] and a[i] >= d[j]:
            d[j] = a[i]
            pos[j] = i
            prev[i] = pos[j - 1]
            length = max(length, j)
    l = []
    p = pos[length]
    while p != -1:
        l.append(p)
        p = prev[p]
    l = list(sorted([li + 1 for li in l]))
    return l


def bin_search(decreasing_array, value):
    lo = - 1
    hi = len(decreasing_array) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if value > decreasing_array[mid]:
            hi = mid
        else:
            lo = mid + 1
    return hi


def test():
    numbers = [random.randint(1, 100000) for _ in range(10)]
    print(*numbers)
    sol = solution(numbers)
    print(len(sol))
    print(*sol)


def main():
    n = int(input())
    numbers = tuple(map(int, input().split(" ")))
    sol = solution(numbers)
    print(len(sol))
    print(*sol)

if __name__ == "__main__":
    main()

"""
Sample Input:
5
5 3 4 4 2
Sample Output:
4
1 3 4 5 
"""
