# расстояние редактирования

# Вычислите расстояние редактирования двух данных непустых строк 
# длины не более 100, содержащих строчные буквы латинского алфавита.

# https://goo.gl/dUix6k

def solution(first, second):
    if first == second:
        return 0
    n = len(first) + 1
    m = len(second) + 1
    d = [list([0] * n) for _ in range(m)]
    for i in range(n):
        d[0][i] = i
    for j in range(m):
        d[j][0] = j
    for i in range(1, n):
        for j in range(1, m):
            c = (1 if first[i - 1] != second[j - 1] else 0)
            d[j][i] = min(d[j - 1][i] + 1, d[j][i - 1] + 1, d[j - 1][i - 1] + c)
    return d[m - 1][n - 1]


def main():
    first = input()
    second = input()
    print(solution(first, second))


if __name__ == "__main__":
    main()

"""
Sample Input 1:
ab
ab
Sample Output 1:
0
Sample Input 2:
short
ports
Sample Output 2:
3
"""
