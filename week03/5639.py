import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#시간초과 ---------------------------------------> 반복문으로 변경
# def insert(node, value):
#     if value < node.value:
#         if node.left is None:
#             node.left = Node(value)
#         else:
#             insert(node.left, value)
#     else:
#         if node.right is None:
#             node.right = Node(value)
#         else:
#             insert(node.right, value)

def insert_iter(root, value):
    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = Node(value)
                break
            else:
                current = current.right


#시간초과 ---------------------------------------> 스택으로 변경
# def postorder(node):
#     if node is None:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.value)

def postorder_non_recursive(root):
    stack = []
    result = []
    last_visited = None
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                node = peek.right
            else:
                result.append(peek.value)
                last_visited = stack.pop()
    
    sys.stdout.write('\n'.join(map(str, result)) + '\n')

inputs = sys.stdin.read().split()
nodes = list(map(int, inputs))

root = Node(nodes[0])
for value in nodes[1:]:
    #insert(root, value)
    insert_iter(root, value)

# postorder(root)
postorder_non_recursive(root)