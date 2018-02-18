
class BinTreeNode(object):

	def __init__(self,data=None,left=None,right=None):
		self.right = right
		self.data = data
		self.left = left

def pre_visit(BinTreeNode):
	if BinTreeNode == None:
		return
	else:
		print(BinTreeNode.data)
		pre_visit(BinTreeNode.left)
		pre_visit(BinTreeNode.right)

def middle_visit(BinTreeNode):
	if BinTreeNode == None:
		return
	else:
		pre_visit(BinTreeNode.left)
		print(BinTreeNode.data)
		pre_visit(BinTreeNode.right)

def post_visit(BinTreeNode):
	if BinTreeNode == None:
		return
	else:
		pre_visit(BinTreeNode.left)
		pre_visit(BinTreeNode.right)
		print(BinTreeNode.data)


node_D = BinTreeNode('D')
node_E = BinTreeNode('E')
node_B = BinTreeNode('B',node_D,node_E)
node_F = BinTreeNode('F')
node_C = BinTreeNode('C',node_F)
node_A = BinTreeNode('A',node_B,node_C)


print('-----二叉树遍历-----')
print('-----前序遍历-----')
pre_visit(node_A)

print('-----中序遍历-----')
middle_visit(node_A)

print('-----后序遍历-----')
post_visit(node_A)