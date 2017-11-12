# Проверка правильности расстановки скобок в строке

# https://stepik.org/lesson/41234/step/1?unit=19818

HOOKS = (('(', ')'), ('[', ']'), ('{', '}'))

def solution(string):
    stack1 = []
    stack2 = []
    for i, s in list(enumerate(string)):
        if s in [h[0] for h in HOOKS]:
            stack1.append(s)
            stack2.append(i + 1)
        else:
            for h in HOOKS:
                if s == h[1]:
                    if len(stack1) and stack1[-1] == h[0]:
                        stack1.pop()
                        stack2.pop()
                    else:
                        return i + 1
    if not len(stack1):
        return "Success"
    else:
        return stack2[-1]
        

def main():
    string = input()
    print(solution(string))

if __name__ == "__main__":
    main()

"""
Sample Input 1:
([](){([])})
Sample Output 1:
Success
Sample Input 2:
()[]}
Sample Output 2:
5
Sample Input 3:
{{[()]]
Sample Output 3:
7
"""
