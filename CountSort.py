# Сортировка подсчётом

# https://goo.gl/vfGxyJ

def count_sort(numbers):
    size = len(numbers)
    b = [0] * (max(numbers) + 1)
    sorted_numbers = [0] * size
    for n in numbers:
        b[n] += 1
    for i in range(1, len(b)):
        b[i] += b[i - 1]
    for n in reversed(numbers):
        sorted_numbers[b[n] - 1] = n
        b[n] -= 1
    return sorted_numbers


def main():
    n = int(input())
    numbers = list(map(int, input().split(" ")))
    print(*count_sort(numbers))


if __name__ == "__main__":
    main()

"""
Sample Input:
5
2 3 9 2 9
Sample Output:
2 2 3 9 9
"""
