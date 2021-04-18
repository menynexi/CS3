import bst
import matplotlib.pyplot as plt

def height(t):
    if type(t) == bst.BST:
        return height(t.root)
    if t == None:
        return -1
    heightOfLeft = 1 + height(t.left)
    heightOfRight = 1 + height(t.right)
        
    if heightOfLeft > heightOfRight:
        return heightOfLeft
    return heightOfRight
     
def printSmaller(t,k):
    if type(t) == bst.BST:
        t = t.root
    if t != None:
        printSmaller(t.left,k)
        if k>t.data:
            print(t.data,end=' ')
            printSmaller(t.right,k)

def printLeaves(t):
    if type(t) == bst.BST:
        t = t.root
    if t != None:
        if t.left == None and t.right == None:
            print(t.data,end=' ')
        else:
            printLeaves(t.left)
            printLeaves(t.right)

def atDepth(t,d):
    if type(t) == bst.BST:
        t = t.root
    if t==None:
        return []
    if d == 0:
        return [t.data]
    return atDepth(t.left,d-1) + atDepth(t.right,d-1)

def depthOfK(t,k):
    if type(t) == bst.BST:
        t = t.root
    if t==None:
        return -1
    if t.data==k:
        return 0
    child = t.left
    if t.data<k:
        child = t.right
    d = depthOfK(child,k)
    if d>=0:
        d+=1
    return d

   
if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
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
    TA.draw()
    TB.draw()
    
    print('Question 1')
    print(height(T_empty)) 
    print(height(T_oneNode)) 
    print(height(TA)) 
    print(height(TB))
    
   
    
 
    print('Question 2')
    printSmaller(T_empty, 16) 
    print()
    printSmaller(T_oneNode, 30) 
    print()
    printSmaller(TA, 16) 
    print()
    printSmaller(TA, 5)  
    print()
    printSmaller(TB, 0)  
    print()
    printSmaller(TB, 2302)  
    print()
    
    print('Question 3')
    printLeaves(T_empty) 
    print()
    printLeaves(T_oneNode) 
    print()
    printLeaves(TA) 
    print()
    printLeaves(TB) 
    print()
    
    print('Question 4')
    print(atDepth(T_empty,2))      
    print(atDepth(T_oneNode,0))    
    for i in range(5):
        print(atDepth(TA,i))  
        
    for i in range(5):
        print(atDepth(TB,i))   
            
    print('Question 5')
    print(depthOfK(T_empty,2301))   
    print(depthOfK(T_oneNode,0))    
    print(depthOfK(TA,11))          
    print(depthOfK(TA,6))           
    print(depthOfK(TA,18))          
    print(depthOfK(TA,21))          
    print(depthOfK(TB,11))                       
    

'''
Program Output:
    
Question 1
-1
0
4
3
Question 2

23 
1 2 4 6 7 8 11 13 14 15 
1 2 4 

2 4 5 6 7 8 11 13 14 15 18 
Question 3

23 
1 4 8 13 15 20 
4 7 11 14 18 
Question 4
[]
[23]
[11]
[6, 16]
[2, 7, 14, 17]
[1, 4, 8, 13, 15, 18]
[20]
[8]
[5, 15]
[2, 6, 13, 18]
[4, 7, 11, 14]
[]
Question 5
-1
-1
0
1
3
-1
3
'''        
    