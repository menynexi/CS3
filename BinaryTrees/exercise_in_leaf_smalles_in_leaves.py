import bst
import btree

# VERSION 1
def in_leaf0(t,k):
    if type(t) == bst.BST:
        t = t.root
    if t.left != None:
        in_leaf0(t.left, k)
    if(t.left is None and t.right is None): 
        if t.key == k:
            return True 
        else:
            return False
    if t.right != None:
        in_leaf0(t.right, k)

# VERSION 2    
def in_leaf1(t,k):
    if type(t) == bst.BST:
        t = t.root
    if t == None:
        return
    if t.left == None and t.right == None:
        if t.key == k:
            return True
        else:
            return False
    return in_leaf1(t.left,k) or in_leaf1(t.right,k)

# VERSION 3
def in_leaf2(t,k):
    if type(t) == bst.BST:
         t = t.root
    if t.left is not None:
         return in_leaf2(t.left,k)
    if t.right is not None:
         return in_leaf2(t.right,k) 
    if t.left is None and t.right is None:
       if t.key == k: 
          return True
    return False

# VERSION 4
def in_leaf3(t,k):
    if t==None:
        return False
    if type(t) == bst.BST:
        t=t.root
    if t.key==k:
        return t.left == None and t.right ==None
    if t.key<k:
        return in_leaf3(t.right,k)
    return in_leaf3(t.left,k)

# VERSION 1    
def smallest_in_leaves0(T):
    if type(T)==btree.BTree:
        T = T.root
    for c in T.child:
        return smallest_in_leaves0(c)
    if T.is_leaf:
        return [T.data[0]]

# VERSION 2
def smallest_in_leaves1(T):
    small = [ ]
    if type(T)==btree.BTree:
        T = T.root
    if not T.is_leaf:
        for i in range(len(T.child)):
            small.append(smallest_in_leaves1(T.child[i]))
    if T.is_leaf:
         return T.data[0]
    return small

'''
# VERSION 3
def smallest_in_leaves2(T):
    if type(T)==btree.BTree:
        T = T.root
    small = [ ]    
    if T.is_leaf:
        small.append(T.data[0])
    else:
        for c in T.child:
            return small + smallest_in_leaves2(c)
    return small

# VERSION 4
def smallest_in_leaves3(T):
    if type(T)==btree.BTree:
        T = T.root
    small = [ ]    
    if T.is_leaf:
        small.append(T.data[0])
    else:
        for c in T.child:
            smallest_in_leaves3(c)
    return small

# VERSION 5
def smallest_in_leaves4(T):
    if type(T) == btree.BTree:
        return smallest_in_leaves4(T.root)
    if T.is_leaf:
        return [T.data[0]]
    s = [ ]
    for c in T.child:
        s = s + smallest_in_leaves4(c)
    return s
'''
if __name__ == "__main__":

    A =[11,6,16,2,7,14,1,4,8,13,15,0]
    B =[7]
    
   
    T_empty = bst.BST()
    T_oneNode = bst.BST()
    T_oneNode.insert(23)
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TB = bst.BST()
    for b in B:
        TB.insert(b)
        
        
    print("question 1")
    #print(in_leaf0(T_empty, 5)) 
    print(in_leaf0(TB,5))
    print(in_leaf0(TA, 11))
    print(in_leaf0(TA, 1))
    print(in_leaf0(TA, 20))
    print(in_leaf0(TA, 8))
    
    print("question 2")
    print(in_leaf1(T_empty, 5)) 
    print(in_leaf1(TB,5))
    print(in_leaf1(TA, 11))
    print(in_leaf1(TA, 1))
    print(in_leaf1(TA, 20))
    print(in_leaf1(TA, 8))
    
    
    print("question 3")    
    #print(in_leaf2(T_empty, 5)) 
    print(in_leaf2(TB,5))
    print(in_leaf2(TA, 11))
    print(in_leaf2(TA, 1))
    print(in_leaf2(TA, 20))
    print(in_leaf2(TA, 8))
    
    print("question 4")
    print(in_leaf3(T_empty, 5)) 
    print(in_leaf3(TB,5))
    print(in_leaf3(TA, 11))
    print(in_leaf3(TA, 1))
    print(in_leaf3(TA, 20))
    print(in_leaf3(TA, 8))
    
    print("question 5")
    T = btree.BTree()
    T2 = btree.BTree()

    nums =[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26]
    nums2 = [1,2,3,4,5]
    
    for num in nums:
        T.insert(num)
    T.draw()
    
    for num in nums2:
        T2.insert(num)
    T2.draw
    
    print(smallest_in_leaves0(T))
    print(smallest_in_leaves0(T2))

    print("question 5.1")
    print(smallest_in_leaves1(T))
    print(smallest_in_leaves1(T2))
    '''
    print("question 5.2")
    print(smallest_in_leaves2(T))
    print(smallest_in_leaves2(T2))
    
    print("question 5.3")
    print(smallest_in_leaves3(T))
    print(smallest_in_leaves3(T2))
    
    print(smallest_in_leaves4(T))
    print(smallest_in_leaves4(T2))
    '''
    
    
    