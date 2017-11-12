# покрыть отрезки точками
# По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.

# https://stepik.org/lesson/13238/step/9

import operator

class Solution:
    def __init__(self, points):
        self.points = points
    
    def __str__(self):
        s = ""
        s += str(len(self.points)) + "\n"
        s += " ".join(map(str, self.points))
        return s


class PointsOnLines:
    def placing(self, lines):
        points = set()
        lines = sorted(lines, key=operator.itemgetter(0))
        while lines:
            p = lines[-1][0]
            points.add(p)
            lines = [l for l in lines if not(l[0] <= p <= l[1])]
        return Solution(points)


def main ():
    lines = []
    n = int(input())
    for i in range(n):
        lines.append(tuple(map(int, input().split())))
    print(PointsOnLines().placing(lines))


if __name__ == "__main__":
    main()

"""
Sample Input 1:
3
1 3
2 5
3 6
Sample Output 1:
1
3 
Sample Input 2:
4
4 7
1 3
2 5
5 6
Sample Output 2:
2
3 6 
"""
