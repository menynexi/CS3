# Code to implement basic binary search tree operations
# Programmed by Olac Fuentes
# Last modified June 24, 2020

import matplotlib.pyplot as plt
import numpy as np

class BSTNode:

    def __init__(self, key,  left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self,newkey):
        if self.key > newkey:
            if self.left == None:
                self.left = BSTNode(newkey)
            else:
                self.left.insert(newkey)
        else:
            if self.right == None:
                self.right = BSTNode(newkey)
            else:
                self.right.insert(newkey)

    def inOrder(self):
        if self.left !=None:
            self.left.inOrder()
        print(self.key,end=' ')
        if self.right !=None:
            self.right.inOrder()

    def inOrderShape(self,space):
        if self.right !=None:
            self.right.inOrderShape(space+'   ')
        print(space+str(self.key))
        if self.left !=None:
            self.left.inOrderShape(space+'   ')
        



    def draw(self, ax, x0, y0, delta_x, delta_y):
        delta_x = max([20,delta_x])
        if self.left is not None:
            ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
            self.left.draw(ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)
        if self.right is not None:
            ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
            self.right.draw(ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y)
        ax.text(x0,y0, str(self.key), size=14,ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))

    def find(self,key):
        if self.key == key:
            return self
        if self.key > key:
            child = self.left
        else:
            child = self.right
        if child == None:
            return None
        else:
            return child.find(key)

    def find_node_and_parent(self,parent,key):
        # Same as find, but it also returns the parent of the node that contains key
        # if key is in the tree
        if self.key == key:
            return self, parent
        if self.key > key:
            child = self.left
        else:
            child = self.right
        if child == None:
            return None, self
        else:
            return child.find_node_and_parent(self,key)

class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,newkey):
        if self.root == None:
            self.root = BSTNode(newkey)
        else:
            self.root.insert(newkey)
        self.size += 1

    def delete(self,key):
        if self.root == None:
            print('Trying to delete from empty tree')
            return -1
        node_to_delete, parent = self.root.find_node_and_parent(None,key)
        if node_to_delete == None:
            print('Trying to delete key that is no in the tree')
            return -1
        num_children = int(node_to_delete.left!=None) + int(node_to_delete.right!=None) # Returns reference to node to delete and its parent
        if num_children==0: # key is in a leaf node
            if parent==None: # Deleting root, which is the only node in the tree
                self.root = None
            elif parent.left == node_to_delete:
                parent.left = None
            else:
                parent.right = None   
            self.size -= 1
        elif num_children==1: # key is in a node that has one child
            child = node_to_delete.left
            if child==None:
                child = node_to_delete.right
            if parent==None: # Deleting root
                self.root = child  
            elif parent.left == node_to_delete:
                parent.left = child
            else:
                parent.right = child
            self.size -= 1
        else:  # key is in a node that has two children
            t =  node_to_delete.right
            while t.left!=None:     # Find key's successor
                t=t.left
            successor = t.key
            self.delete(successor)  # Delete key's successor
            node_to_delete.key = successor   # Copy successor to node that contains key (thus deleting key)   
        return 1
      
    def find(self,key):
        if self.root == None:
            return None
        return self.root.find(key)

    def inOrder(self):
        if self.root != None:
            self.root.inOrder()
            print()
        else:
            print('Tree is empty')

    def inOrderShape(self):
        if self.root != None:
            self.root.inOrderShape('')
            print()
        else:
            print('Tree is empty')

    def draw(self):
        fig, ax = plt.subplots()
        if self.root != None:
            self.root.draw(ax, 0, 0, 1000, 120)
        ax.axis('off')
        plt.show()
        
            

if __name__ == "__main__":
    plt.close('all')
    A =[8, 11, 6, 7, 16, 2,15, 1, 9, 4, 14,  13, 0]
   
    T = BST()
    filenum = 0
    for a in A:
        T.insert(a)
        T.draw()
   
    T.inOrder()
   
    T.draw()
    
    print('Tree size:',T.size)
    
    for k in A:
        print('Deleting',k)
        T.delete(k)
        T.draw()


