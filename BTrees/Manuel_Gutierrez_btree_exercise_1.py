import matplotlib.pyplot as plt
import numpy as np
import btree

def smallest(T):
    t = T.root
    while not t.is_leaf: # traverses the Tree all the way to the smallest child
        t = t.child[0]
    return t.data[0]

def largest(T):
    t = T.root
    while not t.is_leaf: # traverses the Tree all the way to the biggest child
        t = t.child[-1] #by doing the reverse of smallest you can find the largest
    return t.data[-1]

def numNodes(T):
    if type(T)==btree.BTree:#wrapper function could take in a BSTree or a BSTreeNode
        T=T.root
    count = 1
    if not T.is_leaf: #traversal
        for i in T.child:
            count+= numNodes(i)
    return count

def numItems(T):
    if type(T)==btree.BTree:
        T=T.root
    count = 1
    if not T.is_leaf:
        for c in T.child:
            count+= numNodes(c)
    return count

def print_data(T):
    if type(T)==btree.BTree:
        T=T.root
    if T.is_leaf:
        for d in T.data:
            print(d,end=' ')
    else:
        for i in range(len(T.data)):
            print_data(T.child[0])
            print(T.data[i],end=' ')
        print_data(T.child[-1])

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums =[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26]
    
    for num in nums:
        T.insert(num)
    T.draw()
    print(smallest(T))  
    print(largest(T))   
    print(numNodes(T))  
    print(numItems(T))  
    
    print_data(T)
    print()

'''
Program output:
0
68
11
35
0 2 4 6 8 0 2 4 6 20 0 2 4 6 32 34 36 38 40 42 44 40 42 56 40 42 62 64 66 68 
'''