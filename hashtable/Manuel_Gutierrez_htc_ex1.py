# Starter code for hash table exercise 1
# Rename this program as lastname_firstname_htc_ex1.py and submit it 

import hash_table_chain as htc

def load_factor(h):
    c = 0
    for i in h.bucket:
        c += len(i)
    return c/len(h.bucket)# / floats // integers

def longest_bucket(h):
    c = 0
    for i in h.bucket:#iterates trough the bukets 
        if len(i) > c:
            c = len(i)
    return c

def check(h):
    for i in range(len(h.bucket)):
        for j in h.bucket[i]:
            if h.h(j.key) != i:
                return False
    return True

# this implementation must be O(n) with hashtables
def has_duplicates(L):
    h = htc.HashTableChain(len(L))
    for i in L:
        if h.insert(i,[]) == -1:
            return True
    return False

if __name__ == "__main__":
    h = htc.HashTableChain(9)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]

    for i in range(len(players)):
        h.insert(numbers[i],players[i])
        
    h.print_table()

    print("question 1")
    print(load_factor(h))  # 0.66666666666666
    
    print("question 2")
    print(longest_bucket(h)) # 2
    
    print("question 3")
    print(check(h)) # True
    h.bucket[2][0].key = 2302
    h.print_table()
    print(check(h)) # False
    
    L1 = [1,4,2,5,6,7,8,39,20,45]
    L2 = [1,4,2,5,6,7,8,39,20,45,9,13,5,34]
    
    print(has_duplicates(L1)) # False
    print(has_duplicates(L2)) # True

