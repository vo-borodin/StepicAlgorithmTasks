# Реализация дерева отрезков для нахождения минимума в массиве

import operator
import random

MONOID = 1000000001

class Tree:
    def __init__(self, numbers):
        self.a = numbers
        size = len(numbers)
        k = 0
        while (1 << k) < size: k += 1
        new_size = 1 << k
        for _ in range(new_size - size):
            numbers.append(MONOID)
        self.tree = [None] * (new_size << 1)

    # root element has index 1
    def build(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = { "cnt": 1, "min": self.a[tl] }
        else:
            tm = tl + ((tr - tl) >> 1)
            self.build(i << 1, tl, tm)
            self.build((i << 1) + 1, tm + 1, tr)
            self.tree[i] = Tree.__merge(self.tree[i << 1], self.tree[(i << 1) + 1])

    @staticmethod
    def __merge(l_item, r_item):
        if l_item["min"] < r_item["min"]:
            return l_item
        if l_item["min"] > r_item["min"]:
            return r_item
        return { "cnt": l_item["cnt"] + r_item["cnt"], "min": l_item["min"] }

    def get_min(self, i, tl, tr, l, r):
        if l > r:
            return { "cnt": 0, "min": MONOID }
        if l == tl and r == tr:
            return self.tree[i]
        tm = tl + ((tr - tl) >> 1)
        return self.merge(self.get_min(i << 1, tl, tm, l, min(r, tm)),
                          self.get_min((i << 1) + 1, tm + 1, tr, max(l, tm + 1), r))


def solution(a):
    tree = Tree(a)
    tree.build(1, 0, len(a) - 1)
    return tree.get_min(1, 0, len(a) - 1, 0, 2)


def main():
    n = int(input())
    numbers = list(map(int, input().split(" ")))
    s = solution(numbers)
    print (s[0])
    print (" ".join([str(si) for si in s[1]]))


def test():
    size = random.randint(50, 250)
    numbers = [random.randint(1, 100) for _ in range(size)]
    sol = solution(numbers)
    print (size)
    print (" ".join([str(n) for n in numbers]))
    print ("solution={0}, min={1}".format(sol["min"], min(numbers)))


if __name__ == "__main__":
    main()
            
