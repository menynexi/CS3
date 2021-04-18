# Example of convertion of recursive function to stack-based non-recursive function
# Programmed by Olac Fuentes
# Last modified Sept. 5, 2020
import numpy as np 

class stackRecord(object):
    # Constructor
    def __init__(self, comb_so_far, list_of_lists):  
        self.comb_so_far = comb_so_far
        self.list_of_lists = list_of_lists
    
    def display(self):
        print(self.comb_so_far, self.list_of_lists)
    
def display_stack(S):
    print('Stack contents:')
    for s in S[::-1]:
        s.display()
        
def combinations(comb_so_far, list_of_lists):
    if len(list_of_lists)==0:
        for item in comb_so_far:
            print(item, end = ' ')
        print()    
    else:
        for i in list_of_lists[0]:
            combinations(comb_so_far+[i], list_of_lists[1:])

def combinations_stack(L,debug=False):
    S = [stackRecord([],L)]  # Initial call
    while len(S)!=0:
        if debug: # Set debug to True to see the stack contents in every iteration
            display_stack(S)
        p = S.pop()
        if len(p.list_of_lists)== 0:
            for item in p.comb_so_far:
                print(item, end = ' ')
            print()    
        else:
            for i in p.list_of_lists[0][::-1]: # Items must be inserted in reverse to the stack
                S.append(stackRecord(p.comb_so_far+[i], p.list_of_lists[1:]))

if __name__ == "__main__":  
    debug =  True
    '''
    print('--- Recursive function')
    combinations([],[['salad', 'soup', 'pasta'],['steak', 'fish','lasagna'], ['cake', 'ice cream']])
    '''
    
    print('--- Stack function')
    combinations_stack([['salad', 'soup', 'pasta'],['steak', 'fish','lasagna'], ['cake', 'ice cream']],debug = debug)
    
    '''
    print('--- Recursive function')
    combinations([],[['Dodgers', 'Braves', 'Mets','Padres'],['Yankees', 'Astros','Red Sox','Blue Jays']])
    print('--- Stack function')
    combinations_stack([['Dodgers', 'Braves', 'Mets','Padres'],['Yankees', 'Astros','Red Sox','Blue Jays']],debug = debug)
    '''

