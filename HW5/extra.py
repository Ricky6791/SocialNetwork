from bintrees import RBTree

#From geeksforgeeks.com
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root)

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root)

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    def inorder(self):
        ''' For Inorder traversal of the BST '''
        global count
        count += 1
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print("[",count,"]", str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

    def height(self):
        #climb each side if there is both sides
        if self.leftChild and self.rightChild:
            #max to figure out which one has more
            return 1 + max(self.leftChild.height(), self.rightChild.height())
        #if there is only left
        elif self.leftChild:
            return 1 + self.leftChild.height()
        #if there is only right
        elif self.rightChild:
            return 1 + self.rightChild.height()
        else:
            return 1

    def countNode(self):
        if self.leftChild and self.rightChild:
            #plus 1 for each node counted on either side
            return 1 + self.leftChild.countNode() + self.rightChild.countNode()
        elif self.leftChild:
            #plus 1 for each in left
            return 1 + self.leftChild.countNode()
        elif self.rightChild:
            #plus 1 for each in right
            return 1 + self.rightChild.countNode()
        else:
            return 1


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
    #to get root from node class
    def height(self):
        if self.root:
            return self.root.height()
        else:
            return -1
    #to get root from node class
    def countNode(self):
        if self.root:
            return self.root.countNode()
        else:
            return -1


tree = Tree()
arr = []
with open("rand1000000.txt", 'r') as f:
    lines = f.read()
    for i in lines.split():
        arr.append(i)
#for each number in the array from txt file
for number in arr:
    tree.insert(number)
count = 0
tree.inorder()

print("")
print("The height of Binary Search tree is ", tree.height())
print("Total nodes in Binary Search tree is ", tree.countNode())
