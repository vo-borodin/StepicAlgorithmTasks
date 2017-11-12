# Очередь с приоритетами

# https://goo.gl/UXoQdd

import operator
import math

class PriQue:
    def __init__(self):
        self.stor = []

    def __get_parent_index(self, node_index):
        if node_index % 2:
            index = (node_index - 1) // 2
        else:
            index = (node_index - 2) // 2
        return max(index, 0)
    
    def __get_left_child_index(self, node_index):
        index = 2 * node_index + 1
        if index >= len(self.stor):
            return -1
        else:
            return index

    def __get_right_child_index(self, node_index):
        index = 2 * node_index + 2
        if index >= len(self.stor):
            return -1
        else:
            return index
    
    def extract_max(self):
        self.stor[0], self.stor[-1] = self.stor[-1], self.stor[0]
        max_value = self.stor.pop()
        i = 0
        child_index = 0
        while True:
            left_child_index = self.__get_left_child_index(i)
            right_child_index = self.__get_right_child_index(i)
            if left_child_index == -1 and right_child_index == -1:
                break
            if right_child_index == -1 or self.stor[left_child_index] >= self.stor[right_child_index]:
                child_index = left_child_index
            else:
                child_index = right_child_index
            if self.stor[i] >= self.stor[child_index]:
                break
            else:
                self.stor[i], self.stor[child_index] = self.stor[child_index], self.stor[i]
                i = child_index
        return max_value

    def insert(self, value):
        i = len(self.stor)
        self.stor.append(value)
        while True:
            parent_index = self.__get_parent_index(i)
            if self.stor[parent_index] >= self.stor[i] or i == parent_index:
                break
            else:
                self.stor[parent_index], self.stor[i] = self.stor[i], self.stor[parent_index]
                i = parent_index

    def __str__(self):
        return str(self.stor)


def main():
    nops = int(input())
    ops = []
    queue = PriQue()
    for i in range(nops):
        t = tuple(map(str, input().split(" ")))
        ops.append(t)
    for t in ops:
        if t[0] == "Insert":
            queue.insert(int(t[1]))
        if t[0] == "ExtractMax":
            print(queue.extract_max())


if __name__ == "__main__":
    main()

"""
Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:
200
500
"""
