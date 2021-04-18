import matplotlib.pyplot as plt
import numpy as np
import btree

def smallest(T):
    return T.root.data[0]

def largest(T):
    return T.root.data[-1]

def numNodes(T):
    count = 1
    return count

def numItems(T):
    count = len(T.root.data)
    return count

def print_data(T):
    return 

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums =[38, 56, 14, 42, 32, 60, 52, 68, 20, 10, 24,  0, 40, 46, 44,  8, 48,
       36,  4, 16, 62, 30, 54, 34, 58, 28, 50, 64,  2, 66, 12, 26,  6, 18, 22]
    
    for num in nums:
        T.insert(num)
    T.draw()

    print_data(T)
    print()

    print(smallest(T))  
    print(largest(T))   
    print(numNodes(T))  
    print(numItems(T))  

'''
Program output:
0
68
11
35
0 2 4 6 8 0 2 4 6 20 0 2 4 6 32 34 36 38 40 42 44 40 42 56 40 42 62 64 66 68 
'''