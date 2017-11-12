# Калькулятор

# https://stepik.org/lesson/13262/step/5?unit=3447

def solution(number):
    if number == 1:
        return [1]
    D = [0] + [i - 1 for i in range(1, number + 1)]
    prev = [0] * (number + 1)
    prev[2] = 1
    i = 1
    while i <= number:
        indeces = (i + 1, 2 * i, 3 * i)
        for ind in indeces:
            if ind <= number:
                if D[i] + 1 < D[ind]:
                    D[ind] = D[i] + 1
                    prev[ind] = i
        i += 1
    res = [number]
    j = len(prev) - 1
    while j != 1:
        k = prev[j]
        res.append(k)
        j = k
    return list(reversed(res))


def main():
    N = int(input())
    s = solution(N)
    print(len(s) - 1)
    print(" ".join([str(si) for si in s]))
    

if __name__ == "__main__":
    main()

"""
Sample Input 1:
1
Sample Output 1:
0
1 
Sample Input 2:
5
Sample Output 2:
3
1 2 4 5 
Sample Input 3:
96234
Sample Output 3:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234 
"""
