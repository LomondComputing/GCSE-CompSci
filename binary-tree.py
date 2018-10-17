# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left

def preOrder(tree):
        if tree != None:
            print(tree.getNodeValue())
            preOrder(tree.getLeftChild())
            preOrder(tree.getRightChild())

def inOrder(tree):
        if tree != None:
            inOrder(tree.getLeftChild())
            print(tree.getNodeValue())
            inOrder(tree.getRightChild())

def postOrder(tree):
        if tree != None:
            postOrder(tree.getLeftChild())
            postOrder(tree.getRightChild())
            print(tree.getNodeValue())
            
# test tree

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    print('\nPre-Order Traversal:')
    preOrder(myTree)
    print('\nIn-Order Traversal:')
    inOrder(myTree)
    print('\nPost-Order Traversal:')
    postOrder(myTree)
        
