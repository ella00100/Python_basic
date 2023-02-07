class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

node1 = TreeNode()
node1.data = '대표'

node2 = TreeNode()
node2.data = '관리이사'
node1.left = node2

node3 = TreeNode()
node3.data = '기술이사'
node1.right = node3

node4 = TreeNode()
node4.data = '인사부장'
node2.left = node4

node5 = TreeNode()
node5.data = '회계부장'
node2.right = node5

node6 = TreeNode()
node6.data = '연구부장'
node3.left = node6

def preorder(node) :
	if node == None:
		return
	print(node.data, end='->') # 데이터 처리
	preorder(node.left)		   # 왼쪽 서브트리로 이동
	preorder(node.right)	   # 오른쪽 서브트리로 이동

def inorder(node):
	if node == None :
		return
	inorder(node.left)			# 왼쪽 서브트리로 이동
	print(node.data, end='->')  # 데이터 처리
	inorder(node.right)         # 오른쪽 서브트리로 이동

def postorder(node):
	if node == None :
		return
	postorder(node.left)		# 왼쪽 서브트리로 이동
	postorder(node.right)       # 오른쪽 서브트리로 이동
	print(node.data, end='->')  # 데이터 처리

print('전위 순회 : ', end = '')
preorder(node1)
print('끝')

print('중위 순회 : ', end = '')
inorder(node1)
print('끝')

print('후위 순회 : ', end = '')
postorder(node1)
print('끝')
