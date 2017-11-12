# Декодирование Хаффмана

# https://goo.gl/y19qqg

import operator
import uuid

def solve(code, encoded):
    inv_code = {v: k for k, v in code.items()}
    code_list = sorted(inv_code.items(), key=operator.itemgetter(0), reverse=True)
    decoded = ""
    i = 0
    while i < len(encoded):
        for cand, letter in code_list:
            start = i
            end = i+len(cand)
            if encoded[start:end] == cand:
                decoded += letter
                i += len(cand)
                break
    return decoded

def main():
    letters, size = map(int, input().split(" "))
    code = {}
    for i in range(0, letters):
        l, c = map(str, input().split(": "))
        code[l] = c
    encoded = input()
    print(solve(code, encoded))

if __name__ == "__main__":
    main()

"""
Sample Input 1:
1 1
a: 0
0
Sample Output 1:
a
Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
Sample Output 2:
abacabad
"""
