import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def zero2n(n):
    L=sll.List()
    if n < 0:
        return L
    for i in range(0,n+1):
        L.append(i)
    return L

def appears(t,x):
    if t==None:
        return False
    return appers_n(t.head,x) 

def appers_n(t,x):
    if t == None:
        return False
    if t.data == x:
        return True
    return appers_n(t.next, x)

def appears_loop(L,x):
   temp = L.head
   while(L.head != None):
       if(L.head.data == x):
           return True
       L.head = L.head.next
   L.head = temp
   return False
       

def insert_head(L,x):
   # sll gives you access to the singly_link_list class
   node = sll.ListNode(x)
   to_be_second_node = L.head
   L.head = node
   L.head.next = to_be_second_node
   return L

def remove_first(L):
    if(L.head == None):
        return L
    if(L.head.next == None):
        L.head = None
        return L
    second_node = L.head.next
    L.head = second_node
    return L
            
def remove_last(L):
    if(L.head == None):
        return L
    if(L.head.next == None):
        L.head = None
        return L
    return remove_last_Node(L.head)

def remove_last_Node(head):
    second_last = head 
    while(second_last.next.next): 
        second_last = second_last.next
    second_last.next = None
    return head 
  
def is_sorted(t):
    if(t.head == None or t.head.next == None):
        return True
    return is_sorted_n(t.head)

def is_sorted_n(t):
    if(t == None):
        return True
    if(t.next == None):
        return True
    if(t.data < t.next.data):
        return is_sorted_n(t.next)
    return False
    
def is_sorted_loop(L):
    if(L.head == None):
        return True
    if(L.head.next == None):
        return True
    while(L.head.next != None):
        if(L.head.data > L.head.next.data):
            return False
        L.head = L.head.next
    return True

if __name__ == "__main__":
    print('Question 1')
    L1 = zero2n(-9)
    L1.print()
    L1 = zero2n(0)
    L1.print()
    L1 = zero2n(1)
    L1.print()
    L1 = zero2n(5)
    L1.print()
    
    print('Question 2')
    L2 = sll.List()
    L2.extend([3,6,1,4,0,9,7,4,8,5,9,7,19])
    print(appears(L2,0))
    print(appears(L2,10))
    print(appears(L2,19))
    
    print('Question 3')
    L2 = sll.List()
    L2.extend([3,6,1,4,0,9,7,4,8,5,9,7,19])
    print(appears_loop(L2,0))
    print(appears_loop(L2,10))
    print(appears_loop(L2,19))
    
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    
    print('Question 4')   
    insert_head(L1,3)
    L1.print()
    insert_head(L2,4)
    L2.print()
    insert_head(L3,5)
    L3.print()
    insert_head(L4,1)
    L4.print()
    insert_head(L5,1)
    L5.print()
    
    
    print('Question 5')
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    remove_first(L1)
    L1.print()
    remove_first(L2)
    L2.print()
    remove_first(L3)
    L3.print()
    remove_first(L4)
    L4.print()
    remove_first(L5)
    L5.print()
    
    print('Question 6')
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    remove_last(L1)
    L1.print()
    remove_last(L2)
    L2.print()
    remove_last(L3)
    L3.print()
    remove_last(L4)
    L4.print()
    remove_last(L5)
    L5.print()
    
    print('Question 7')  
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
   
    print(is_sorted(L1))
    print(is_sorted(L2))
    print(is_sorted(L3))
    print(is_sorted(L4))
    print(is_sorted(L5))
    
    print('Question 8')  
    print(is_sorted_loop(L1))
    print(is_sorted_loop(L2))
    print(is_sorted_loop(L3))
    print(is_sorted_loop(L4))
    print(is_sorted_loop(L5))
    
    
'''
Question 1
[]
[0]
[0, 1]
[0, 1, 2, 3, 4, 5]
Question 2
True
False
True
Question 3
True
False
True
Question 4
[3]
[4, 2]
[5, 3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[1, 2, 3, 6, 7, 8, 9]
[1, 2, 3, 6, 7, 8, 9, 0]
Question 5
[]
[]
[6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[3, 6, 7, 8, 9]
[3, 6, 7, 8, 9, 0]
Question 6
[]
[]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7]
[2, 3, 6, 7, 8]
[2, 3, 6, 7, 8, 9]
Question 7
True
True
False
True
False
Question 8
True
True
False
True
False
'''