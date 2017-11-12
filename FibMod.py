# Даны целые числа 1<=n<=10^18 и 2<=m<=10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.
# https://goo.gl/uc4QLb

def fib_mod(n, m):
    period = pizano_period(m)
    index = n%len(period)
    return period[index]


def pizano_period(m):
    res = [0,1]
    i = 2
    while True:
        res.append((res[i-1] + res[i-2])%m)
        i += 1
        res.append((res[i-1] + res[i-2])%m)
        i += 1
        if check_period(res, i//2):
            return res[0:i//2]


def check_period(mods, n):
    for i in range(0, n):
        if mods[i] != mods[i+n]:
            return False
    return True


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

"""
Sample Input:
10 2
Sample Output:
1
"""
