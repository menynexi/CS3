import matplotlib.pyplot as plt
import numpy as np
import btree

#problem type 1 
def roots_children(T): 
    L = []
    t = T.root
    if not t.is_leaf:
        for item in t.child:
           L = L + item.data # could not fix it i know i need a recurive function 
    return L

# probem of type 3 must find a specific node and the traversal will be based on that 
def find_k(T,k):
    if type(T) == btree.BTree:
         return find_k(T.root,k)
    if k in T.data:
        return True
    if T.is_leaf:
        return False
    ch = 0
    for i in range(len(T.data)):
        if k > T.data[i]:
            ch += 1 
    return find_k(T.child[ch],k)

# problem of type 2 that requres to traverse all the tree
def add_n(T,n):
    if(type(T) == btree.BTree):
        T = T.root
        T.data[0] += n
    for c in T.child:
        for j in range(len(c.data)):
            c.data[j] += n
        add_n(c, n)
    return

# problem of type 2 must traverse the children and just remove the leaves 
def prune_leaves(T):
    if type(T)==btree.BTree:
        T = T.root
    if T.child[0].is_leaf:
        T.is_leaf = True
    else:
        for item in T.child:
            prune_leaves(item)
    return T

# problme of type 2 must traverse the whole tree
def make_binary(T):
    return


if __name__ == "__main__":  
    plt.close('all') 
    T = btree.BTree()  
    T2 = btree.BTree()  
    T3 = btree.BTree()  
    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for num in nums:
        T.insert(num)
        T3.insert(num)
        T3.insert(num+21)
    T.draw('Original tree')  
    for i in range(5):
        T2.insert(i)
    T2.draw('One-node tree')  
    T3.draw('Bigger tree')  
    
    print('Question 1')
    print(roots_children(T))        # [3, 7, 14, 17]
    print(roots_children(T2))       # []
    print(roots_children(T3))       # [3,7,16,19,28,31,35,38]
    
    print('Question 2')  
    T2a = btree.BTree()  
    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for num in nums:
        T2a.insert(num)
    add_n(T2a,5)
    T2a.draw('Question 2') 
    
    # Uncomment and fix
    print('Question 3')
    print(find_k(T,10))    # True
    print(find_k(T,14))    # True
    print(find_k(T,9))     # True
    print(find_k(T,25))    # False
   
    print('Question 4')
    T = btree.BTree()  
    for num in nums:
        T.insert(num)    
    prune_leaves(T)
    T.draw('Question 4') 
    
    print('Question 5')
    T = btree.BTree()  
    for num in nums:
        T.insert(num)    
    make_binary(T)
    T.draw('Question 5') 
    make_binary(T3)
    T3.draw('Question 5') 