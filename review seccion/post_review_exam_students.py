import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def even_rows_and_reverse(I):
    return I[::2,::-1]

def not_multiples(L,k):
    arr = []
    if len(L) > 0:
        if(k%L[0] == 0):
            return 1 + not_multiples(L[1::], k)
        return 0 + not_multiples(L[1::], k)
    return 0
    
def swap_first_and_third(L):
   if(L.head == None):
       return L
   if(L.head.next == None):
       return L
   if(L.head.next.next == None):
       return L
   first = L.head.data
   third = L.head.next.next.data
   L.head.data, L.head.next.next.data = third,first
   return L
                
def can_divide(nums, target):
  return False

def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()
    
def top_bottom_circles(ax,n,center,radius):
    x,y = circle(center,radius)
    ax.plot(x,y,linewidth=1,color='r')

if __name__ == "__main__":  
    
    plt.close('all')

    print('\nQuestion 1')
    A1 = np.arange(20).reshape(4,5)
    A2 = np.arange(20).reshape(2,10)
    A3 = np.arange(15).reshape(3,5)
    for A in [A1,A2,A3]:
        print('Original array:\n',A)
        print('Result:\n',even_rows_and_reverse(A))
        
    L1 = [2,5,7,4,1,6]
    L2 = [2302]
    L3 = []
    
    print('\nQuestion 2')
    print(not_multiples(L1,2))  
    print(not_multiples(L1,3)) 
    print(not_multiples(L2,2)) 
    print(not_multiples(L3,3)) 
    
    print('\nQuestion 3')
    L4 = [7, 4, 1, 2]    
    for i in range(len(L4)+1):
        L = sll.List()
        L.extend(L4[:i])
        print('Original list:',end=' ')
        L.print()
        print('Resulting list:',end=' ')
        swap_first_and_third(L)
        L.print()   
        
    print('\nQuestion 4')
    print(can_divide([4,4],4))
    print(can_divide([4,8,12],12))
    print(can_divide([1,2,3,4,6],6))
    print(can_divide([1,2,3,4,5],10))
    
    print('\nExtra Question')
    
    fig, ax = plt.subplots()
    top_bottom_circles(ax, 2, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('top_bottom_circles1.png')

    fig, ax = plt.subplots()
    top_bottom_circles(ax, 3, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('top_bottom_circles2.png')

    fig, ax = plt.subplots()
    top_bottom_circles(ax, 4, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('top_bottom_circles3.png')
        
'''
Program output:
    
Question 1
Original array:
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
Result:
 [[ 4  3  2  1  0]
 [14 13 12 11 10]]
Original array:
 [[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]]
Result:
 [[9 8 7 6 5 4 3 2 1 0]]
Original array:
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
Result:
 [[ 4  3  2  1  0]
 [14 13 12 11 10]]
 
Question 2
3
5
0
0
 
Question 3
Original list: 
Resulting list: 
Original list: 7 
Resulting list: 7 
Original list: 7 4 
Resulting list: 7 4 
Original list: 7 4 1 
Resulting list: 1 4 7 
Original list: 7 4 1 2 
Resulting list: 1 4 7 2 

Question 4
True
True
False
False
 
'''