# Определение высоты дерева

# https://stepik.org/lesson/41234/step/2?unit=19818

def build_tree(nodes):
    tree = [[] for _ in range(len(nodes))]
    root = 0
    for i, n in enumerate(nodes):
        if n != -1:
            tree[n].append(i)
        else:
            root = i
    return (root, tree)

def height(root, tree):
    h = 0
    current_level = [root]
    while len(current_level):
        if len(current_level):
            h += 1
        new_level = []
        for n in current_level:
            new_level += tree[n]
        current_level = new_level
    return h

def main():
    _ = input()
    nodes = list(map(int, input().split(" ")))
    root, tree = build_tree(nodes)
    print(height(root, tree))

if __name__ == "__main__":
    main()

"""
Sample Input:
10
9 7 5 5 2 9 9 9 2 -1
Sample Output:
4
"""
