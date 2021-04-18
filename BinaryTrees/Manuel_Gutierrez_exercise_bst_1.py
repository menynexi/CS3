import bst
import numpy as np
import matplotlib.pyplot as plt

def smallest(t):# May receive BST or BSTNode
    if(type(t) == bst.BST):
        t = t.root
    if(t.left == None):
        return t.key
    return smallest(t.left)

def largest(t):# May receive BST or BSTNode
    if(type(t) == bst.BST):
        t = t.root
    if(t.right == None):
        return t.key
    return largest(t.right)

def sum_bst(t): # May receive BST or BSTNode
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
    return t.key + sum_bst(t.left) + sum_bst(t.right)

def printByLevel(t):
    Stack = [t.root]
    while len(Stack)>0:
        t = Stack.pop(0)
        if t!=None:
            print(t.key,end = ' ')
            Stack.append(t.left)
            Stack.append(t.right)
    print()

if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
    
    T = bst.BST()
    T2 = bst.BST()
    
    for a in A:
        T.insert(a)

    for b in B:
        T2.insert(b)

    T.inOrder()
    T2.inOrder()
   
    plt.close('all')
    T.draw()
    T2.draw()
    
    print('Question 1')
    print(smallest(T))
    print(smallest(T2))
    
    print('Question 2')
    print(largest(T))  
    print(largest(T2))  
    
    print('Question 3')
    print(sum_bst(T))  
    print(sum_bst(T2))  
   
    print('Question 4')
    printByLevel(T)
    printByLevel(T2)
    
    
'''
Program Output:
1 2 4 6 7 8 11 13 14 15 16 17 18 20 
2 4 5 6 7 8 11 13 14 15 18 
Question 1
1
2
Question 2
20
18
Question 3
152
103
Question 4
11 6 16 2 7 14 17 1 4 8 13 15 18 20 
8 5 15 2 6 13 18 4 7 11 14 
'''