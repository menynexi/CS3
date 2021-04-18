import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def first(L):
    if(L.head == None):
        return None
    return L.head.data

def last(L):
    if(L.head == None):
        return None
    return L.tail.data

def swap_first_and_last(L):
    if(L.head == None or L.tail == None or L.head == L.tail):
        return L
    temp = L.head.data
    L.head.data = L.tail.data
    L.tail.data = temp
    return L
   
def length(t):
    return length_n(t.head)

def length_n(t):
    if(t==None):
        return 0
    return 1 + length_n(t.next)
    
def sum_list(t):
    return sum_list_n(t.head)

def sum_list_n(t):
    if(t==None):
        return 0
    return t.data + sum_list_n(t.next)

def max_list(t):
    if t.head == None:
        return -math.inf
    return max_list_n(t.head)

def max_list_n(t):
    if (t.next == None):
        return t.data
    return max(t.data, max_list_n(t.next));

def to_list(t):
    List = []
    if(t.head == None):
        return List
    return to_list_n(t.head, List)

def to_list_n(t,List):
    if(t==None):
        return List
    return to_list_n(t.next, List+[t.data])
    

def identical(t1,t2):
    if(length(t1) != length(t2)):
        return False
    return identical_n(t1.head, t2.head)

def identical_n(t1,t2):
    if(t1 == None and t2 == None):
        return True
    if(t1.data != t2.data):
        return False
    return identical_n(t1.next, t2.next)
  
def print_list(t):
    List = []
    if(t.head == None):
        print(List)
        return List
    return print_list_n(t.head,List)

def print_list_n(t,List):
    if(t==None):
        print(List)
        return List
    return print_list_n(t.next, List+[t.data])
    

if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.print()
    L1.draw()
   
    L2 = sll.List()
    L2.extend([3,6,1,0,9,7,4,8,5])
    L2.print()
    L2.draw()
    
    L3 = sll.List()
    L3.append(2)
    L3.print()
    L3.draw()
    
    print('Question 1')
    print(first(L1))   
    print(first(L2))   
    print(first(L3))   
    
    print('Question 2')
    print(last(L1))   
    print(last(L2))    
    print(last(L3))    
    
    print('Question 3')   
    swap_first_and_last(L1)
    L1.print()             
    swap_first_and_last(L2) 
    L2.print()          
    swap_first_and_last(L3) 
    L3.print()  
    
    L1 = sll.List()
    L2 = sll.List()
    L2.extend([3,6,1,0,9,7,4,8,5])

    L3 = sll.List()
    L3.append(2)
   
    print('Question 4')   
    print(length(L1))
    print(length(L2))
    print(length(L3))
    
    print('Question 5')  
    print(sum_list(L1))
    print(sum_list(L2))
    print(sum_list(L3))
    
    print('Question 6')
    print(max_list(L1))
    print(max_list(L2))
    print(max_list(L3))
    
    print('Question 7')
    print(to_list(L1))
    print(to_list(L2))
    print(to_list(L3))
    
    print('Question 8')
    L4 = sll.List()
    L4.extend([3,6,1,0,9,7,4,8,5])
    
    L5 = sll.List()
    L5.extend([3,6,1,0])
    
    print(identical(L1,L3))
    print(identical(L4,L2))
    print(identical(L2,L3))
    print(identical(L3,L4))
    print(identical(L4,L5))
    
    print('Question 9')
    for L in [L1,L2,L3,L4,L5]:
        L.print()
        print_list(L)
    

'''
[]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[2]
Question 1
None
3
2
Question 2
None
5
2
Question 3
[]
[5, 6, 1, 0, 9, 7, 4, 8, 3]
[2]
Question 4
0
9
1
Question 5
0
43
2
Question 6
-inf
9
2
Question 7
[]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[2]
Question 8
False
True
False
False
False
Question 9
[]
[]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[2]
[2]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[3, 6, 1, 0]
[3, 6, 1, 0]
'''