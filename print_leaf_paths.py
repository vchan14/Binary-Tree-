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


def print_list(list):
    for i in list:
        print(i, end =" ")
    print("\n")
        
def leaf_path(current, list):
    list.append(current.data)
    if (current.left == None) and (current.right == None):
        print_list(list)
        list.pop()
    if(current.left != None):
        leaf_path(current.left, list)
    if(current.right != None): 
        leaf_path(current.right, list)


root = nodeA
list = []
leaf_path(root, list)