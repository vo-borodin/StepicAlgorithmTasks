# Наибольшая последовательнократная подпоследовательность

# https://goo.gl/WMvimC

def solution(numbers):
    size = len(numbers)
    if size == 1:
        return 1
    d = [1] * size
    for i, n in enumerate(numbers):
        for j in range(i):
            if n % numbers[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(size):
        ans = max(ans, d[i])
    return ans

def main():
    n = int(input())
    numbers = tuple(map(int, input().split(" ")))
    print(solution(numbers))

if __name__ == "__main__":
    main()

"""
Sample Input:
4
3 6 7 12
Sample Output:
3
"""
