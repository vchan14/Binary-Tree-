class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


nodeA = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')
nodeG = Node('g')
nodeH = Node('h')
nodeZ = Node('z')

nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeZ
nodeB.right = nodeD
nodeD.left = nodeE
nodeD.right = nodeF
nodeC.left = nodeH
nodeC.right = nodeG



def count_node(current, count):
    if(current != None):
        count[0] = count[0] + 1
    if(current.left != None):
        count_node(current.left, count)
    if(current.right != None):
        count_node(current.right, count)

root = nodeA
count = [0]
count_node(root, count)
print("Your Total Nodes is count" , count[0])