

class SegmentTreeNode():
	def __init__(self):
		self.start = -1
		self.end = -1
		self.tot = 0
		self.l_child = None
		self.r_child = None

class SegmentTree():

	root = None
	arr = None

	def __init__(self, arr):
		self.arr = arr
	
	def build(self):
		self.root = self.build_recur_helper(arr, 0, len(self.arr) - 1)


	def build_recur_helper(self, arr, start_idx, end_idx):
		print(	"start_idx, end_idx", start_idx, end_idx)
		
		if start_idx  == end_idx:
			print("return ", arr[start_idx])
			leaf_node = SegmentTreeNode()
			leaf_node.start = start_idx
			leaf_node.end = end_idx
			leaf_node.tot = arr[start_idx]
			return leaf_node

		mid = int((start_idx + end_idx) / 2)
		l_node = self.build_recur_helper(arr, start_idx ,mid) 
		r_node = self.build_recur_helper(arr, mid + 1 , end_idx)
		parent_node = SegmentTreeNode()
		parent_node.start = start_idx
		parent_node.end = end_idx
		parent_node.tot = l_node.tot + r_node.tot
		parent_node.l_child = l_node
		parent_node.r_child = r_node
		return parent_node

	def build__helper(self):
		pass

	def get_range_sum(self, root, start, end):

		if not root:
			root = self.root
		print("start", start, "end", end,"root",root.start, root.end )
		if root.start == start and root.end == end:
			return root.tot

		mid = int((start + end) / 2)
	
		if end <= mid:
			return self.get_range_sum(root.l_child, start, end)
		elif start >= mid:
			return self.get_range_sum(root.r_child, start, end)
		else:
			return self.get_range_sum(root.l_child, start, mid) + self.get_range_sum(root.r_child, mid+1, end)
		return self.get_range_sum(root, start, end)

	def update(self,idx, new_val):
		if new_val == arr[idx]:
			return
		# update array
		arr[idx] = new_val
		self.update_tree_helper(None, idx, new_val)

	def update_tree_helper(self, root, idx , val):
		if not root:
			root = self.root

		if root.start == root.end:
			root.tot = val
			return val			

		mid = (root.start + root.end) // 2

		if idx <= mid:
			self.update_tree_helper(root.l_child, idx, val) # move towards left
		else:
			self.update_tree_helper(root.r_child, idx, val) # move right

		root.tot = root.l_child.tot + root.r_child.tot

		return root.tot


	def print(self):
		queue = [[self.root]]
		while queue:
			childs = queue.pop()
			grand_childs = []
			for child in childs:
				print(child.tot, "[ " , child.start , child.end, " ]", end = "\t")
				if child.l_child:
					grand_childs.append(child.l_child)
				if child.r_child:
					grand_childs.append(child.r_child)
			if grand_childs:
				queue.append(grand_childs)
			print()

st = SegmentTree(arr)
st.build()
st.print()
print("range_sum", st.get_range_sum(None, 0,2))
st.update(2,5)
st.print()
print("range_sum", st.get_range_sum(None, 0,2))
