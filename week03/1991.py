class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

n = int(input())
tree_dict = dict()
first = ''

for i in range(n):
    value, left, right = map(str, input().split())
    tree_dict[value] = Tree(value, left, right)
    if i == 0:
        first = value

#전위순회
def preOrder(node: Tree):
    print(node.value, end='')
    if node.left != '.':
        preOrder(tree_dict[node.left])
    if node.right != '.':
        preOrder(tree_dict[node.right])

#중위순회
def inOrder(node: Tree):
    if node.left != '.':
        inOrder(tree_dict[node.left])
    print(node.value, end='')
    if node.right != '.':
        inOrder(tree_dict[node.right])

#후위순회
def postOrder(node: Tree):
    if node.left != '.':
        postOrder(tree_dict[node.left])
    if node.right != '.':
        postOrder(tree_dict[node.right])
    print(node.value, end='')


preOrder(tree_dict[first])
print()
inOrder(tree_dict[first])
print()
postOrder(tree_dict[first])