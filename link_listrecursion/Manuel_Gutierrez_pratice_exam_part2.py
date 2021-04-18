import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def crop(L):
    return L[:4]

def equal_neighbors(L):
    if len(L) <= 1:
        return False
    if L[0] == L[1]:
        return True
    return equal_neighbors(L[1:])

def sum_until(L,i):
    su = 0
    for j in range(len(L)):
        if(L[j]==i):
            return su
        su += L[j]
    return su

def next_to_last(L):
    if L.head == None:
        return None
    if L.head.next == None:
        return None
    return next_to_last_n(L.head)

def next_to_last_n(t):
    if(t.next.next == None):
        return t.data
    return next_to_last_n(t.next)

def all_equal(L):
    if L.head == None:
        return True
    if(L.head.data != L.tail.data):
        return False
    return all_equal_n(L.head)

def all_equal_n(t):
    if(t.next == None):
        return True
    if(t.data != t.next.data):
        return False
    return all_equal_n(t.next)


def sum_first_n(L,n):
    if type(L) == sll.List:
        return sum_first_n(L.head,n)
    if L == None or n==0:
        return 0
    return L.data + sum_first_n(L.next,n-1)

def sum_first_n_loop(L,n):
    if(L.head == None):
        return 0
    t = L.head
    sum_n = 0
    for i in range(n):
        if(t != None):
            sum_n += t.data
            t = t.next
    return sum_n
   
if __name__ == "__main__":  
    plt.close('all')
    L = [4,1,7,9,3,0,6,5,2,8,4,5,6,4]
   
    '''
    print('Question 1')
    A = np.arange(20).reshape(4,5)
    print(A)
    print(crop(A))
    A = np.arange(9).reshape(3,3)
    print(A)
    print(crop(A))
    A = np.arange(15).reshape(3,5)
    print(A)
    print(crop(A))
    '''
    
    print(crop(L))
    
    print('Question 2')
    print(equal_neighbors([]))
    print(equal_neighbors([1]))
    print(equal_neighbors([1,5,6,9,2,9,9]))
    print(equal_neighbors([1,5,6,9,2,9]))
    print(equal_neighbors([1,5,6,9,2,2,9,7]))
    
    print('Question 3')
    print(sum_until([],5))
    print(sum_until([1,5,6,9,2,3,7,8,4,2,9],6))
    print(sum_until([1,5,6,9,2,3,7,8,4,2,9],7))
    
    print('Question 4')
    L4 = sll.List()
    for i in range(7):
        L4.print()
        print(next_to_last(L4))
        L4.append(i*10)
        
    print('Question 5')
    L5 = sll.List()
    for i in range(7):
        L5.print()
        print(all_equal(L5))
        L5.append(10)
    L5.append(5)
    L5.print()
    print(all_equal(L5))
    L5 = sll.List()
    L5.extend([3,3,23,3])
    L5.print()
    print(all_equal(L5))
    
    print('Question 6')
    # Uncomment and fix
    L6 = sll.List()
    L6.print()
    print(sum_first_n(L6,2302))
    L6.extend([1,5,6,3,7,8,4,2,9])
    L6.print()
    for i in range(12):
        print(sum_first_n(L6,i))
    
    
    print('Question 7')
    # Uncomment and fix
    L7 = sll.List()
    L7.print()
    print(sum_first_n_loop(L7,2302))
    L7.extend([1,5,6,3,7,8,4,2,9])
    L7.print()
    for i in range(12):
        print(sum_first_n_loop(L7,i))
    L7 = sll.List()
    
    
'''
Program output:    
Question 1
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
[[ 6  7  8]
 [11 12 13]]
[[0 1 2]
 [3 4 5]
 [6 7 8]]
[[4]]
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
[[6 7 8]]
Question 2
False
False
True
False
True
Question 3
0
6
26
Question 4
[]
None
[0]
None
[0, 10]
0
[0, 10, 20]
10
[0, 10, 20, 30]
20
[0, 10, 20, 30, 40]
30
[0, 10, 20, 30, 40, 50]
40
Question 5
[]
True
[10]
True
[10, 10]
True
[10, 10, 10]
True
[10, 10, 10, 10]
True
[10, 10, 10, 10, 10]
True
[10, 10, 10, 10, 10, 10]
True
[10, 10, 10, 10, 10, 10, 10, 5]
False
[3, 3, 23, 3]
False
Question 6
[]
0
[1, 5, 6, 3, 7, 8, 4, 2, 9]
0
1
6
12
15
22
30
34
36
45
45
45
Question 7
[]
0
[1, 5, 6, 3, 7, 8, 4, 2, 9]
0
1
6
12
15
22
30
34
36
45
45
45    
'''