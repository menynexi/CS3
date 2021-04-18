# Program to solve the Towers of Hanoi
import numpy as np 

class stackRecord(object):
    # Constructor
    def __init__(self, first, last):  
        self.first = first
        self.last = last
        
    def display(self):
        print(self.first, self.last)

def display_stack(S):
    print('Stack contents:')
    for s in S[::-1]:
        s.display()

def quicksort(L):
    if len(L)<2:
        return L[:]
    p = L[0]
    small = [i for i in L[1:] if i < p]
    large = [i for i in L[1:] if i >= p]
    return quicksort(small) + [p] + quicksort(large)

def quicksort_stack(L,debug=False):
    L_sorted = L.copy()
    S = [stackRecord(0,len(L))]
    while len(S)!=0:
        if debug: # Set debug to True to see the stack contents in every iteration
            display_stack(S)
        p = S.pop()
        if p.last - p.first >1:
            pivot = L_sorted[p.first]
            small = [i for i in L_sorted[p.first+1:p.last] if i < pivot]
            large = [i for i in L_sorted[p.first+1:p.last] if i >= pivot]
            L_sorted[p.first+len(small)] = pivot
            L_sorted[p.first:p.first+len(small)]=small
            L_sorted[p.first+len(small)+1:p.last]=large
            S.append(stackRecord(p.first,p.first+len(small)))
            S.append(stackRecord(p.first+len(small)+1,p.last))
    return L_sorted              



if __name__ == "__main__":  
    debug =  False
   
    L = list(np.random.permutation(93)*2)
    
    print(L)
    Ls = quicksort(L)
    print(Ls)
    print(sorted(L)==Ls)

    print(L)
    Ls = quicksort_stack(L,debug = debug)
    print(Ls)
    print(sorted(L)==Ls)