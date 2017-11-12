# Лестница

# https://stepik.org/lesson/13262/step/4?unit=3447

def solution(steps):
    prev = 0
    current = steps[0]
    i = 2
    while i <= len(steps):
        further = max(current + steps[i-1], prev + steps[i-1])
        prev = current
        current = further
        i += 1
    return current


def main():
    _ = int(input())
    steps = list(map(int, input().split(" ")))
    print(solution(steps))


if __name__ == "__main__":
    main()

"""
Sample Input 1:
2
1 2
Sample Output 1:
3
Sample Input 2:
2
2 -1
Sample Output 2:
1
Sample Input 3:
3
-1 2 1
Sample Output 3:
3
"""
