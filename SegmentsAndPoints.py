# Различные варианты алгоритма быстрой сортировки

import random
import array

class PrimaryQuick:
    """ самая простая версия быстрой сортировки
    опорный элемент - первый в обрабатываемом массиве
    деление массива на две части """
    def __init__(self):
        self.s = []

    def __get_sep(self, l, r):
        return l

    def __partition(self, l, r):
        m = self.__get_sep(l, r)
        x = self.s[m]
        j = m
        for i in range(l, r):
            if i == j:
                continue
            if self.s[i] <= x:
                j += 1
                self.s[j], self.s[i] = self.s[i], self.s[j]
        self.s[m], self.s[j] = self.s[j], self.s[m]
        return j

    def __quick_sort(self, l, r):
        if r - l <= 1:
            return
        m = self.__partition(l, r)
        self.__quick_sort(l, m)
        self.__quick_sort(m + 1, r)

    def sort(self, segments):
        self.s = segments
        self.__quick_sort(0, len(self.s))
        return list(self.s)


class RandQuick(PrimaryQuick):
    """ версия алгоритма быстрой сортировки
    со случайным выбором опорного элемента
    и разбиением на две части """
    def __get_sep(self, l, r):
        return random.randint(l, r - 1)


class TripleQuick(PrimaryQuick):
    """ версия алгоритма быстрой сортировки
    с разбиением на три части
    опорный элемент - первый"""
    def __partition(self, l, r):
        m = self.__get_sep(l, r)
        x = self.s[m]
        j1 = j2 = m
        for i in range(l, r):
            if i >= j1 and i < j2:
                continue
            if self.s[i] < x:
                j1 += 1
                self.s[j1], self.s[i] = self.s[i], self.s[j1]
            elif self.s[i] > x:
                j2 += 1
        self.s[m], self.s[j1] = self.s[j1], self.s[m]
        return (j1, j2)

    def __quick_sort(self, l, r):
        if r - l <= 1:
            return
        m1, m2 = self.__partition(l, r)
        self.__quick_sort(l, m1)
        self.__quick_sort(m2 + 1, r)


class TripleRandQuick(TripleQuick, RandQuick):
    """ алгоритм быстрой сортировки со
    случайным выбором опорного элемента и
    разбиением на три части"""
    pass

class BinarySearch:
    def __init__(self):
        self.s = []
        self.p = 0

    def run(self, segments, point):
        self.s = segments
        self.p = point
        if self.p < self.s[0]:
            return 0
        elif self.p > self.s[-1]:
            return len(self.s)
        return self.__binary_search(0, len(self.s))

    def __binary_search(self, start, end):
        if end - 1 == start:
            return end
        m = (start + end) // 2
        if self.p < self.s[m]:
            return self.__binary_search(start, m)
        else:
            return self.__binary_search(m, end)


def solution(starts, ends, points):
    sorter = TripleQuick()
    search = BinarySearch()
    starts_sorted = sorter.sort(starts)
    ends_sorted = sorter.sort(ends)
    result = []
    for p in points:
        first = search.run(starts_sorted, p)
        second = search.run(ends_sorted, p - 1)
        result.append(first - second)
    return result


def main():
    s, p = tuple(map(int, input().split(" ")))
    starts = array.array('l')
    ends = array.array('l')
    for i in range(s):
        seg = tuple(map(int, input().split(" ")))
        starts.append(seg[0])
        ends.append(seg[1])
    points = tuple(map(int, input().split(" ")))
    print(" ".join([str(item) for item in solution(starts, ends, points)]))


if __name__ == "__main__":
    main()
