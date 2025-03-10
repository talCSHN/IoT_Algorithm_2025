class TreeNode:
  def __init__(self):
    self.left = None
    self.data = None
    self.right = None

node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

def preorder(node):
  if node == None: return

  print(node.data, end=' -> ')
  preorder(node.left)
  preorder(node.right)
preorder(node1)
print()

def inorder(node):
  if node is None: return

  inorder(node.left)
  print(node.data, end=' -> ')
  inorder(node.right)

inorder(node1)
print()


def postorder(node):
  if node is None: return

  postorder(node.left)
  postorder(node.right)
  print(node.data, end=' -> ')

postorder(node1)
print()
