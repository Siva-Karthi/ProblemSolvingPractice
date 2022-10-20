# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node():
		childrens = {}
		end = False

class Trie():

	root = None

	def __init__(self):
		self.root = Node()

	def insert(self, string):
		node = self.root
		for char in string:
			if char in node.childrens:
				node = node.childrens[char]
			else:
				new_node = Node()
				node.childrens[char] = new_node
				node = new_node
		node.end = True
	
	def search(self, string):
		node = self.root
		for char in string:
			if char in node.childrens:
				node = node.childrens[char]
			else:
				return False
		if node.end == True:
			return True
		else:
			return False

	def startswith(self, string):
		node = self.root
		for char in string:
			if char in node.childrens:
				node = node.childrens[char]
			else:
				return False
		return True
		
trie = Trie()
trie.insert("google")
print(trie.startswith("google"))
print(trie.search("google"))
