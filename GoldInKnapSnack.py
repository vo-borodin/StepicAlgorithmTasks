# Рюкзак с золотом

# https://goo.gl/nXqNXw

def solution(capacity, n, weights):
    W = capacity + 1
    n = n + 1
    D = [list([0] * W) for _ in range(n)]
    for w in range(W):
        D[0][w] = 0
    for i in range(n):
        D[i][0] = 0
    for i in range(1, n):
        for w in range(1, W):
            D[i][w] = D[i - 1][w]
            if weights[i - 1] <= w:
                D[i][w] = max(D[i][w], D[i-1][w - weights[i - 1]] + weights[i - 1])
    return D[-1][-1]


def main():
    C, n = tuple(map(int, input().split(" ")))
    weights = tuple(map(int, input().split(" ")))
    print(solution(C, n, weights))

if __name__ == "__main__":
    main()

"""
Sample Input:
10 3
1 4 8
Sample Output:
9
"""
