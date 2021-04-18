import numpy as np
import matplotlib.pyplot as plt
import bst as bst

def smallest(t):
    if(type(t) == bst.BST):
        t = t.root
    if(t.left == None):
        return t.data
    return smallest(t.left)

def largest(t):
    if(type(t) == bst.BST):
        t = t.root
    if(t.right == None):
        return t.data
    return largest(t.right)

def sum_bst(t):
    if(type(t) == bst.BST):
        t = t.root
    if(t == None):
        return 0
    '''
    this  is extra computation that is not necessary
    if(t.right == None):
        return t.data + sum_bst(t.left)
    if(t.left == None):
        return t.data + sum_bst(t.right)
    '''
    return t.data + sum_bst(t.left) + sum_bst(t.right)

#this is very similar to drawing the tree in lab 1
def print_by_level(t):
    Stack = [t.root]
    while len(Stack)>0:
        t = Stack.pop(0)
        if t!=None:
            print(t.data,end = ' ')
            Stack.append(t.left)
            Stack.append(t.right)
    print()



if __name__ == "__main__":
    plt.close('all')
    A =[11, 6, 7, 16, 2, 4, 14, 8, 15, 1, 13, 0]
    T = bst.BST()

    for a in A:
        T.insert(a)
        
    print(smallest(T))
    print(largest(T))
    print(sum_bst(T))
    print_by_level(T)

