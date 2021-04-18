# Implementation of binary search trees using lists\
# The course name
# Name of the nstructor 
# Name of writen program 
import matplotlib.pyplot as plt
import numpy as np

def insert(T,newItem): # Insert newItem to BST T
    # Running time is O(log n) for a balanced tree
    if T == None:  # T is empty
        T = [newItem,None,None]
    else:
        if newItem< T[0]:
            T[1] = insert(T[1],newItem) # Insert newItem in left subtree
        else:
            T[2] = insert(T[2],newItem) # Insert newItem in right subtree
    return T

def inOrder(T):
    # Prints keys in the tree in ascending order
    # Running time is O(n) for a balanced or unbalanced tree
    if T!=None:
        inOrder(T[1])
        print(T[0],end=' ')
        inOrder(T[2])

#O(n)
def height(T): # MAY be used by is_perfect(t)
    if T == None:
        return -1
    return max(height(T[1]),height(T[2]))+1

#O(n)
def count_nodes(T): # MAY be used by is_perfect(t)
    count = 0
    Stack = [T]
    while len(Stack)>0:
        T = Stack.pop(0)
        count = count + 1
        if T!=None:
            Stack.append(T[1])
            Stack.append(T[2])
    return count

#O(n)           
def size(T):
    if(T == None):
        return 0
    return 1 + size(T[1]) + size(T[2]) 

#O(n)
def minimum(T):
    if(T[1] == None):
        return T[0]
    return minimum(T[1])

#O(n)
def maximum(T):
    if(T[2] == None):
        return T[0]
    return maximum(T[2])

#O(n)
def height(T):
    if T == None:
        return -1
    heightOfLeft = 1 + height(T[1])
    heightOfRight = 1 + height(T[2])
        
    if heightOfLeft > heightOfRight:
        return heightOfLeft
    return heightOfRight

#O(log n) in a balanced tree
def inTree(T,i):
    if(T == None):
        return False
    if(i == T[0]):
        return True
    if(i > T[0]):
        return inTree(T[2], i)
    return inTree(T[1], i)

#O(n)
def printByLevel(T):
    Stack = [T]
    while len(Stack)>0:
        T = Stack.pop(0)
        if T!=None:
            print(T[0],end = ' ')
            Stack.append(T[1])
            Stack.append(T[2])
    print()

#O(n)
def leaves(T):
    L = []
    if T != None:
        if T[1] == None and T[2] == None:
            L.append(T[0])
            return L
        else:
            L = L + leaves(T[1])
            L = L + leaves(T[2])
    return L

#O(n)
def itemsAtDepthD(T,d):
    L = []
    if T==None:
        return []
    if d == 0:
        L.append(T[0])
    return L + itemsAtDepthD(T[1],d-1) + itemsAtDepthD(T[2],d-1)

#O(log n) in  a balanced tree
def depthOfK(T,k):
    if T==None:
        return -1
    if T[0]==k:
        return 0
    child = T[1]
    if T[0]<k:
        child = T[2]
    d = depthOfK(child,k)
    if d>=0:
        d+=1
    return d

# draw akes O(1) as its just a wrapperfunction but draw1 takes O(n) and over all the draw functions take O(n)
def draw(T):
    fig, ax = plt.subplots()
    if T != None:
        draw1(T,ax, 0, 0, 1000, 120)
    ax.axis('off')
    plt.show()
    
def draw1(T, ax, x0, y0, delta_x, delta_y):
    delta_x = max([20,delta_x])
    if T[1] is not None:
        ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw1(T[1],ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)
    if T[2] is not None:
        ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw1(T[2],ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y)
    ax.text(x0,y0, str(T[0]), size=14,ha="center", va="center",
        bbox=dict(facecolor='w',boxstyle="circle"))
    
#O(n)
def tree_to_list_stack(T):
    current = T
    stack = []
    L = []
    while True: 
        if current != None: 
            stack.append(current) 
            current = current[1] 
        elif(stack): 
            current = stack.pop()
            L.append(current[0])
            current = current[2] 
        else: 
            break
    return L

#O(n)
def is_full(T):        
    if T == None:
        return True
    if T[1] == None and T[2] is None:
        return True
    if T[1] != None and T[2] != None:
        return (is_full(T[1]) and (is_full(T[2])))
    return False

# height takes O(n) times adn count of nodes also takes O(n) times over all it will take O(n) times
# even though the function only has if stamenets an assignments 
def is_perfect(T):
    h = height(T)
    n = count_nodes(T)
    if h == -1 or n ==0:
        return True
    if h >= 0:
        equation = (2**(h+2))-1
    if n == equation:
        return True
    return False

# O(log n) in a balanced tree 
# for an unballeanced tree worst case scenario will be O(n) best case O(1) if the tree is empty
def delete(T,key):
    
    '''
    #cheatingall this does is make the node nll but never deletes it 
    if T==None:
        return T
    if T[0]==k:
        T[0] = None
        return T
    child = T[1]
    if T[0]<k:
        child = T[2]
    delete(child,k)
    '''
    
    # start of fuentes code    
    if T == None:
        print('Trying to delete from empty tree')
        return -1
    node_to_delete, parent = find_node_and_parent(T,None,key) # Returns reference to node to delete and its parent
    if node_to_delete == None:
        print('Trying to delete key that is no in the tree')
        return -1
    num_children = int(node_to_delete[1]!=None) + int(node_to_delete[2]!=None) # Returns reference to node to delete and its parent
    if num_children==0: # key is in a leaf node
        if parent==None: # Deleting root, which is the only node in the tree
            T[0] = None
        elif parent[1] == node_to_delete:
            parent[1] = None
        else:
            parent[2] = None   
        # at any point here you can return the tree
        
    elif num_children==1: # key is in a node that has one child
        child = node_to_delete[1]
        if child==None:
            child = node_to_delete[2]
        if parent==None: # Deleting root
            T[0] = child  
        elif parent[1] == node_to_delete:
            parent[1] = child
        else:
            parent[2] = child
    
    # this part needs to be solved
    else:  # key is in a node that has two children
        t =  node_to_delete[2]
        while t[1]!=None:     # Find key's successor
            t=t[1]
        successor = t[0]
        delete(T,successor)  # Delete key's successor
        node_to_delete[0] = successor   # Copy successor to node that contains key (thus deleting key)   
    return T #at the end return the tree with the deleted node 

#O(log n) if the tree is balanced 
#O(n) in a worst case or O(1) in the best of cases
def find_node_and_parent(T,parent,key):
    # Same as find, but it also returns the parent of the node that contains key
    # if key is in the tree
    if T[0] == key:
        return T, parent
    if T[0] > key:
        child = T[1]
    else:
        child = T[2]
    if child == None:
        return None, T
    else:
        return find_node_and_parent(child,T,key) # in order to progress T becomes the parent 
    
    
if __name__ == "__main__":
    #list used for testing 
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]
    B = [11, 9, 12]
    C = [11, 9, 12, 8]
    D = [1,2,3,4,5,6]
    
    #trees used for testing 
    T = None
    testTree = None
    testTreeDelete = None
    emptyTree = None
    unbalancedTree = None
    
    # to make the list it takes 
    for a in A:
        print('Inserting',a)
        T = insert(T,a) 
        print(T)    
    
    for b in B:
        print('Inserting',b)
        testTree = insert(testTree,b)   
        print(testTree)  
        
    for c in C:
        print('Inserting',c)
        testTreeDelete = insert(testTreeDelete,c) 
        print(testTreeDelete)  
        
    for d in D:
        print('Inserting',d)
        unbalancedTree = insert(unbalancedTree,d) 
        print(unbalancedTree) 
        
        
        
    inOrder(T)
    
    print("\n")
    print("question 1")
    print(size(T))
    print(size(emptyTree))
    print(size(unbalancedTree))

    print("question 2")
    print(minimum(T))
    print(minimum(unbalancedTree))
    
    print("question 3")
    print(maximum(T))
    print(maximum(unbalancedTree))
    
    print("question 4")
    print(height(T))
    print(height(emptyTree))
    print(minimum(unbalancedTree))
  
    print("question 5")
    print(inTree(T, 1))
    print(inTree(T, 4))
    print(inTree(T, 5))
    print(inTree(emptyTree, -1))
    print(inTree(unbalancedTree, 5))
    
    print("question 6")
    printByLevel(T)
    printByLevel(emptyTree)
    printByLevel(unbalancedTree)
    
    print("question 7")
    print(tree_to_list_stack(T))
    print(tree_to_list_stack(testTree))
    print(tree_to_list_stack(emptyTree))
    print(tree_to_list_stack(unbalancedTree))
    
    print("question 8")
    print(leaves(T))
    print(leaves(testTree))
    print(leaves(emptyTree))
    print(leaves(unbalancedTree))
    
    print("question 9")
    print(itemsAtDepthD(T, 0))
    print(itemsAtDepthD(T, 1))
    print(itemsAtDepthD(T, 2))
    print(itemsAtDepthD(T, 3))
    print(itemsAtDepthD(T, 4))
    print(itemsAtDepthD(unbalancedTree, 3))
    
    print("question 10")
    print(depthOfK(T, 10))
    print(depthOfK(T, 11))
    print(depthOfK(T, 20))
    print(depthOfK(emptyTree, 0))
    print(depthOfK(unbalancedTree, 3))
    
    print("question 11")
    draw(T)
    draw(testTree)
    draw(emptyTree)
    draw(unbalancedTree)
    
    print("question 12")
    print(is_full(T))
    print(is_full(unbalancedTree))
    
    print("question 13")
    print(is_perfect(T))
    print(is_perfect(unbalancedTree))
    
    print("question 14")
    print(find_node_and_parent(testTree,11,9))# working fine
    print(delete(testTree, 9))
    print(delete(testTreeDelete, 8))
    print(delete(T, 6))
    print(delete(emptyTree, 0))
    print(delete(unbalancedTree, 3))
    
    
    
