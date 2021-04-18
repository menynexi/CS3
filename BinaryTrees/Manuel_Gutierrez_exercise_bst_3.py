import bst
import matplotlib.pyplot as plt

def height(t): # MAY be used by is_perfect(t)
    if type(t) == bst.BST:
        return(height(t.root))
    if t == None:
        return -1
    return max(height(t.left),height(t.right))+1

def count_nodes(t): # MAY be used by is_perfect(t)
    count = 0
    Stack = [t.root]
    while len(Stack)>0:
        t = Stack.pop(0)
        count = count + 1
        if t!=None:
            Stack.append(t.left)
            Stack.append(t.right)
    return count
    
def in_order_stack(t):
    current = t.root 
    stack = []

    while True: 
        if current != None: 
            stack.append(current) 
            current = current.left  
        elif(stack): 
            current = stack.pop() 
            print(current.key, end=' ')
            current = current.right  
        else: 
            break     
    print() 

def tree2List(t): # May receive BST or BSTNode
    current = t.root 
    stack = []
    L = []

    while True: 
        if current != None: 
            stack.append(current) 
            current = current.left  
        elif(stack): 
            current = stack.pop() 
            L.append(current.key)
            current = current.right  
        else: 
            break     
    return L
    
def list2Tree(L): # Wrapper for list2Tree_n
    T = bst.BST()
    T.root = list2Tree_n(L)
    T.size = len(L)
    return T

def list2Tree_n(L): 
    if L == None or len(L) == 0:
        return None
    mid = len(L) // 2
    node = bst.BSTNode(L[mid]) 
    node.left = list2Tree_n(L[:mid]) 
    node.right = list2Tree_n(L[mid+1:])
    return node
    
def is_full(t): # May receive BST or BSTNode
    if(type(t) == bst.BST):
        return is_full(t.root)
        
    if t == None:
        return True
    
    if t.left == None and t.right is None:
        return True
    
    if t.left != None and t.right != None:
        return (is_full(t.left) and (is_full(t.right)))
    
    return False
    
def is_perfect(t): # May receive BST or BSTNode
    h = height(t)
    n = count_nodes(t)
    if h == -1 or n ==0:
        return True
    if h >= 0:
        equation = (2**(h+2))-1
    if n == equation:
        return True
    return False
        
    
if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
       
    T_empty = bst.BST()
    T_oneNode = bst.BST()
    T_oneNode.insert(23)
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TB = bst.BST()
    for b in B:
        TB.insert(b)
    
    plt.close('all')
    #TA.draw()
    #TB.draw()
    
    print('Question 0')
    for T in [T_empty, T_oneNode, TA, TB]:
        print(count_nodes(T))
    
    print('Question 1')
    for T in [T_empty, T_oneNode, TA, TB]:
        in_order_stack(T)
        
    print('Question 2')
    for T in [T_empty, T_oneNode, TA, TB]:
        print(tree2List(T))
   
    print('Question 3')
    for L in [[], [1], [i*10 for i in range(10)], [i for i in range(1,16)]]:
        T=list2Tree(L)
        T.inOrderShape()
        T.draw()
    
    print('Question 4')
    T4 = bst.BST()
    for i in [11, 14, 6, 7, 4, 18, 2, 5, 13, 16, 20,  1]:
        print(is_full(T4))
        #T4.draw()
        T4.insert(i)
    
    print('Question 5')
    T5 = bst.BST()
    for i in [11, 6, 16, 2, 9, 14, 19, 1, 4, 8, 10, 13, 15, 18, 20, 25 ]:
        print(is_perfect(T5))
        T5.draw()
        T5.insert(i)

'''
Program Output:
    
Question 1
Tree contents: 
Tree contents: 23 
Tree contents: 1 2 4 6 7 8 11 13 14 15 16 17 18 20 
Tree contents: 2 4 5 6 7 8 11 13 14 15 18 
Question 2
[]
[23]
[1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
[2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 18]
Question 3
Tree is empty
1

      90
   80
      70
         60
50
      40
         30
   20
      10
         0

         15
      14
         13
   12
         11
      10
         9
8
         7
      6
         5
   4
         3
      2
         1

Question 4
True
True
False
True
False
True
False
False
False
True
False
True
Question 5
True
True
False
True
False
False
False
True
False
False
False
False
False
False
False
True

'''        
    