# Различные слагаемые

# По данному числу 1<=n<=10^9 найдите максимальное число k, для которого n можно 
# представить как сумму kk различных натуральных слагаемых. Выведите в первой 
# строке число k, во второй — k слагаемых.

# https://stepik.org/lesson/13238/step/11?unit=3424

class Solution:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        s = ""
        s += str(len(self.numbers)) + "\n"
        s += " ".join(list(map(str, self.numbers)))
        return s


def solve(n):
    i = 1
    numbers = []
    while n:
        if i <= n and ((n-i) > i or n == i):
            n -= i
            numbers.append(i)
        i += 1
    return Solution(list(numbers))


def main():
    n = int(input())
    print(solve(n))


if __name__ == "__main__":
    main()

"""
Sample Input 1:
4
Sample Output 1:
2
1 3 
Sample Input 2:
6
Sample Output 2:
3
1 2 3 
"""
