import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

################### 1
def even_cols(I):
    return I[::1,::2]

################### 2
def greater_than(L,k):
    gt = []
    if len(L)>0:
        if L[0]>k:
            gt.append(L[0])
        return gt + greater_than(L[1:],k)
    return gt

################### 3
def all_equal(L):
   if len(L) <= 1:
       return True
   if(L[0] != L[-1]):
       return False
   if(L[0]!= L[1]):
       return False
   return all_equal(L[1:])
    
################### 4  

def swap_second_and_last(L):
    if type(L) == sll.List:
        return swap_second_and_last(L.head)
    #if(L.head == None):
    #    return L
    #if(L.next != None):
       # first = L.head
      #  second = L.next
      #  last = L.tail
     #   L.head.next = last
    #    last.next = second
   # return L
    
################### 5  
def find(L,k):
    t = L.head
    while t!=None:
        if t.data == k:
            return True
        t = t.next
    return False

################### 6      
def first_n_list(L,n):
    return []
    
if __name__ == "__main__":  
   
    print('\nQuestion 1')
    A1 = np.arange(20).reshape(4,5)
    A2 = np.arange(20).reshape(2,10)
    A3 = np.arange(15).reshape(3,5)
    for A in [A1,A2,A3]:
        print('Original array:\n',A)
        print('Result:\n',even_cols(A))
   
    
    print('\nQuestion 2')
    L2a = []
    L2b = [1301]
    L2c = [2, 7, 9, 4, 0, 8, 5, 6, 3, 1]
    
    k =5
    for L in [L2a, L2b, L2c]:
        print('Input:',L,k,'Result:',greater_than(L,k))
    L = L2c
    for k in range(10):
        print('Input:',L,k,'Result:',greater_than(L,k))
     
    print('\nQuestion 3')
    L1 = [5,5,5,6,5,5,8]
    for i in range(len(L1)+1):
        L = L1[:i]
        print('Input list:',L,'Result:',all_equal(L))
   
    
    print('\nQuestion 4')
    L4 = [7, 4, 1, 2, 8, 9, 3]    
    for i in range(len(L4)+1):
        L = sll.List()
        L.extend(L4[:i])
        print('Original list:',end=' ')
        L.print()
        print('Resulting list:',end=' ')
        swap_second_and_last(L)
        L.print()    
       
        
    print('\nQuestion 5')
    L5 = sll.List()
    L5.extend([7, 5, 4, 1, 2])
    print('Input list:',end=' ')
    L5.print()
    for k in range(10):
        print('k:',k,'Result:',find(L5,k))
        
    print('\nQuestion 6')
    L6 = sll.List()
    L6.extend([0, 5, 4, 6, 9, 3, 8, 2, 1, 7])
    print('Input list:',end=' ')
    L6.print()
    for n in range(10):
        print('n:',n,'Result:',first_n_list(L6,n))

'''
Program output:
    
Question 1
Original array:
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
Result:
 [[ 0  2  4]
 [ 5  7  9]
 [10 12 14]
 [15 17 19]]
Original array:
 [[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]]
Result:
 [[ 0  2  4  6  8]
 [10 12 14 16 18]]
Original array:
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
Result:
 [[ 0  2  4]
 [ 5  7  9]
 [10 12 14]]

Question 2
Input: [] 5 Result: []
Input: [1301] 5 Result: [1301]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 5 Result: [7, 9, 8, 6]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 0 Result: [2, 7, 9, 4, 8, 5, 6, 3, 1]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 1 Result: [2, 7, 9, 4, 8, 5, 6, 3]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 2 Result: [7, 9, 4, 8, 5, 6, 3]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 3 Result: [7, 9, 4, 8, 5, 6]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 4 Result: [7, 9, 8, 5, 6]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 5 Result: [7, 9, 8, 6]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 6 Result: [7, 9, 8]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 7 Result: [9, 8]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 8 Result: [9]
Input: [2, 7, 9, 4, 0, 8, 5, 6, 3, 1] 9 Result: []

Question 3
Input list: [] Result: True
Input list: [5] Result: True
Input list: [5, 5] Result: True
Input list: [5, 5, 5] Result: True
Input list: [5, 5, 5, 6] Result: False
Input list: [5, 5, 5, 6, 5] Result: False
Input list: [5, 5, 5, 6, 5, 5] Result: False
Input list: [5, 5, 5, 6, 5, 5, 8] Result: False

Question 4
Original list: []
Resulting list: []
Original list: [7]
Resulting list: [7]
Original list: [7, 4]
Resulting list: [7, 4]
Original list: [7, 4, 1]
Resulting list: [7, 1, 4]
Original list: [7, 4, 1, 2]
Resulting list: [7, 2, 1, 4]
Original list: [7, 4, 1, 2, 8]
Resulting list: [7, 8, 1, 2, 4]
Original list: [7, 4, 1, 2, 8, 9]
Resulting list: [7, 9, 1, 2, 8, 4]
Original list: [7, 4, 1, 2, 8, 9, 3]
Resulting list: [7, 3, 1, 2, 8, 9, 4]

Question 5
Input list: [7, 5, 4, 1, 2]
k: 0 Result: False
k: 1 Result: True
k: 2 Result: True
k: 3 Result: False
k: 4 Result: True
k: 5 Result: True
k: 6 Result: False
k: 7 Result: True
k: 8 Result: False
k: 9 Result: False

Question 6
Input list: [0, 5, 4, 6, 9, 3, 8, 2, 1, 7]
n: 0 Result: []
n: 1 Result: [0]
n: 2 Result: [0, 5]
n: 3 Result: [0, 5, 4]
n: 4 Result: [0, 5, 4, 6]
n: 5 Result: [0, 5, 4, 6, 9]
n: 6 Result: [0, 5, 4, 6, 9, 3]
n: 7 Result: [0, 5, 4, 6, 9, 3, 8]
n: 8 Result: [0, 5, 4, 6, 9, 3, 8, 2]
n: 9 Result: [0, 5, 4, 6, 9, 3, 8, 2, 1]
'''