
class BinTreeNode(object):

	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right


class BinTree(object):

	def __init__(self,root = None):
		self.root = root

	def pre_visit(self,BinTreeNode):
		if BinTreeNode == None:
			return
		else:
			print(BinTreeNode.data)
			self.pre_visit(BinTreeNode.left)
			self.pre_visit(BinTreeNode.right)

	def middle_visit(self,BinTreeNode):
		if BinTreeNode == None:
			return
		else:
			self.middle_visit(BinTreeNode.left)
			print(BinTreeNode.data)
			self.middle_visit(BinTreeNode.right)

	@classmethod
	def post_visit(cls,BinTreeNode):
		if BinTreeNode == None:
			return
		else:
			cls.post_visit(BinTreeNode.left)
			cls.post_visit(BinTreeNode.right)
			print(BinTreeNode.data)


node_D = BinTreeNode('D')
node_E = BinTreeNode('E')
node_B = BinTreeNode('B',node_D,node_E)
node_F = BinTreeNode('F')
node_C = BinTreeNode('C',node_F)
node_A = BinTreeNode('A',node_B,node_C)

bintree = BinTree(node_A)


print('-----二叉树遍历-----')
print('-----前序遍历-----')
bintree.pre_visit(node_A)

print('-----中序遍历-----')
bintree.middle_visit(node_A)

print('-----后序遍历-----')
BinTree.post_visit(node_A)