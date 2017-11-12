# Кодирование Хаффмана

# https://goo.gl/dvQCnu

import operator
import uuid

class MyTree:
    def __init__(self):
        self.d = {}
        self.root = None
        self.code = {}

    def set_root(self, root_uuid):
        self.root = root_uuid

    def extract_by_uuid(self, node_id):
        return self.d[node_id]

    def extract_min(self):
        return self.get_subtrees()[-1]

    def insert(self, obj, priority):
        obj["priority"] = priority
        obj["left"] = None
        obj["right"] = None
        obj["parent"] = None
        new_uuid = uuid.uuid4()
        self.d[new_uuid] = obj
        return new_uuid

    def set_node_as_parent(self, parent_uuid, left_uuid, right_uuid):
        parent = self.d[parent_uuid]
        parent["left"] = left_uuid
        parent["right"] = right_uuid
        self.d[left_uuid]["parent"] = parent_uuid
        self.d[right_uuid]["parent"] = parent_uuid

    def get_subtrees(self):
        return sorted([x for x in self.d.items() if not x[1]["parent"]], key=lambda x: x[1]["priority"], reverse=True)
    
    def __iterate(self, node_uuid, code):
        right_uuid = self.d[node_uuid]["right"]
        left_uuid = self.d[node_uuid]["left"]
        if not right_uuid:
            self.code[self.d[node_uuid]["letter"]] = code + self.d[node_uuid]["dig"]
        else:
            self.__iterate(right_uuid, code + self.d[node_uuid]["dig"])
        if not left_uuid:
            self.code[self.d[node_uuid]["letter"]] = code + self.d[node_uuid]["dig"]
        else:
            self.__iterate(left_uuid, code + self.d[node_uuid]["dig"])

    def collect_code(self):
        if len(self) == 1:
            l = self.d[self.root]["letter"]
            c = self.d[self.root]["dig"]
            return { l: c }
        right_uuid = self.d[self.root]["right"]
        left_uuid = self.d[self.root]["left"]
        self.__iterate(right_uuid, "")
        self.__iterate(left_uuid, "")
        return self.code

    def __len__(self):
        return len(self.d)

    def __str__(self):
        return str(self.root) + "\n" + str(self.d)

def solve(string):
    fqs = {}
    for l in string:
        if l not in fqs:
            fqs[l] = 1
        else:
            fqs[l] += 1
    fqsl = sorted(fqs.items(), key=operator.itemgetter(1))
    tree = MyTree()
    for item in fqsl:
        tree.insert({"letter": item[0]}, item[1])

    while True:
        nodes = tree.get_subtrees()
        if len(nodes) == 1:
            nodes[0][1]["dig"] = "0"
            tree.set_root(nodes[0][0])
            break
        right = nodes[-1]
        right_uuid = right[0]
        right_min = right[1]
        right_min["dig"] = "1"
        left = nodes[-2]
        left_uuid = left[0]
        left_min = left[1]
        left_min["dig"] = "0"
        parent_uuid = tree.insert({"letter": None}, left_min["priority"] + right_min["priority"])
        tree.set_node_as_parent(parent_uuid, left_uuid, right_uuid)

    code = tree.collect_code()
    cipher = ""
    for l in string:
        cipher += code[l]
    result = {
        "letters": len(fqsl),
        "size": len(cipher),
        "code": code,
        "cipher": cipher
    }
    return result


def main():
    string = input()
    solution = solve(string)
    print("{0} {1}".format(solution["letters"], solution["size"]))
    for l, c in solution["code"].items():
        print("{0}: {1}".format(l, c))
    print(solution["cipher"])


if __name__ == "__main__":
    main()

"""
Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0
Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""
