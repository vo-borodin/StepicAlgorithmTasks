# Двоичный поиск

# https://stepik.org/lesson/13246/step/4?unit=3431

def solution(sorted_list, k):
    l = 0
    r = len(sorted_list) - 1
    while l <= r:
        m = l + (r - l) // 2
        if sorted_list[m] == k:
            return m + 1
        elif sorted_list[m] > k:
            r = m - 1
        elif sorted_list[m] < k:
            l = m + 1
    return -1


if __name__ == "__main__":
    numbers = list(map(int, input().split(" ")))[1:]
    searched = list(map(int, input().split(" ")))[1:]
    results = [str(solution(numbers, s)) for s in searched]
    print(" ".join(results))

"""
Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11
Sample Output:
3 1 -1 1 -1
"""
