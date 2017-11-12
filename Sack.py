# Непрерывный рюкзак
# https://stepik.org/lesson/13238/step/10

def calc(pairs, weight):
    pairs = sorted(pairs, key=lambda x: x[0]/x[1])
    amount = 0
    while weight and pairs:
        item = pairs[-1]
        if item[1] <= weight:
            amount += item[0]
            weight -= item[1]
        else:
            amount += weight * (item[0] / item[1])
            weight = 0
        pairs = pairs[:-1]
    return "{:.3f}".format(amount)


def main():
    pairs = []
    n, W = map(int, input().split())
    for i in range(n):
        pair = tuple(map(int, input().split()))
        pairs.append(pair)
    print(calc(pairs, W))


if __name__ == "__main__":
    main()

"""
Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.000
"""