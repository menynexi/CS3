import singly_linked_list as sll
import matplotlib.pyplot as plt

def remove_consonants(word):
    if len(word) == 0:
        return ''
    if word[0] == ' ':
        return ' ' + remove_consonants(word[1:])
    if word[0] not in ('A','a','E','e','I','i','O','o','U','u'):
        return '' + remove_consonants(word[1:])
    return word[0] + remove_consonants(word[1:])

def cumulative_sum(n):
    if n == 0:
        return 0
    return n + cumulative_sum(n-1)

def sum_digits_even(n):
    if n < 10 and n % 2 == 0:
        return n
    last = n%10  
    rest = n//10
    if last % 2 == 0:
        return last + sum_digits_even(rest)
    return sum_digits_even(rest)

def palindrome(word):
    return palindrome_helper(word.lower(),0,len(word)-1)

def palindrome_helper(word,i,j):
    if i >= j:
        return True
    if word[i] in ('?',',','.',' '):
        return palindrome_helper(word,i+1,j)
    if word[j] in ('?',',','.',' '):
        return palindrome_helper(word,i,j-1)
    if word[i] != word[j]:
        return False
    else:
        return palindrome_helper(word,i+1,j-1)
    
def multiply(a,b):
    if b == 0:
        return 0
    return a + multiply(a,b-1)

def num_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return num_ways(n-1) + num_ways(n-2) + num_ways(n-3)

def remove_first_and_last(L):
    if L.head is None or L.head.next is None:
        L.head = None
    L.head = L.head.next
    t = L.head
    while t.next is not L.tail:
        t = t.next
    L.tail = t
    t.next = None
    
        
def return_kth_to_last(head,k):
    if head is None:
        return 0
    index = return_kth_to_last(head.next,k) + 1
    if index == k:
        print('Kth element to last is: ',head.data)
    return index

def reverse(L):
    if L.head is None: # List is empty
        return
    curr_node = L.head
    prev_node = None
    next_node = next 
    tail = L.head # Variable that keeps a reference to head
    while curr_node is not None:
        next_node = curr_node.next # Saves next node of the curr node in the next pointer.
        curr_node.next = prev_node # Changes the next of the curr node to prev node.
        prev_node = curr_node # Makes prev point to curr
        curr_node = next_node # Makes curr to next
    L.head = prev_node # Sets head to be the last node we reached
    L.tail = tail # Sets tail to the first element we visit. For instance, the head of the original list.

def substract_data(L,n):
    if L.head is None:
        return
    else:
        t = L.head 
        while t != None:
            t.data = t.data - n
            t = t.next
    
if __name__ == "__main__":
    
    plt.close('all')

    print('~~~~~~~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~~')
    print(remove_consonants('')) # ' '
    print(remove_consonants('Hello, World!')) # eo o
    print(remove_consonants('Diego Aguirre')) # ieo Auie
    print(remove_consonants('Computer Science')) # oue iee
    
    print('~~~~~~~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~~')
    print(cumulative_sum(0)) # 0
    print(cumulative_sum(3)) # 6
    print(cumulative_sum(10)) # 55
    
    print('~~~~~~~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~~')
    print(sum_digits_even(222)) # 6
    print(sum_digits_even(101)) # 0
    print(sum_digits_even(102)) # 2
    print(sum_digits_even(274)) # 6
    
    print('~~~~~~~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~~')
    print(palindrome('Racecar')) # True
    print(palindrome('12121')) # True
    print(palindrome('Anne')) # False
    print(palindrome('Was it a cat I saw?')) # True
    print(palindrome('Cs2302')) # False
    
    print('~~~~~~~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~~')
    print(multiply(2,3)) # 6
    print(multiply(10,12)) # 120
    print(multiply(27,98)) # 2646
    
    print('~~~~~~~~~~~~~~~ Problem 6 ~~~~~~~~~~~~~~~')
    print(num_ways(0)) # 1
    print(num_ways(2)) # 2
    print(num_ways(5)) # 13
    print(num_ways(10)) # 274
    
    print('~~~~~~~~~~~~~~~ Problem 7 ~~~~~~~~~~~~~~~')
    L1 = sll.List()
    L1.extend([3,6,1,0,9,7,4,8,5])
    print('Before: ',end='')
    L1.print()
    L1.draw()
    
    remove_first_and_last(L1) 
    print('After: ',end='')
    L1.print() # [6, 1, 0, 9, 7, 4, 8]
    L1.draw()
    
    print('~~~~~~~~~~~~~~~ Problem 8 ~~~~~~~~~~~~~~~')
    L2 = sll.List()
    L2.extend([5,2,8,4,1])
    L2.print()
    L2.draw()

    return_kth_to_last(L2.head,1) # 1
    return_kth_to_last(L2.head,2) # 4
    return_kth_to_last(L2.head,5) # 5
    
    print('~~~~~~~~~~~~~~~ Problem 9 ~~~~~~~~~~~~~~~')
    L3 = sll.List()
    L3.extend([3,2,1])
    print('Original: ',end='')
    L3.print()
    L3.draw()
    
    reverse(L3)
    print('Reversed: ',end='')
    L3.print()# 1 -> 2 -> 3
    L3.draw()
    
    print('~~~~~~~~~~~~~~~ Problem 10 ~~~~~~~~~~~~~~~')
    substract_data(L1,10)
    L1.print() # [-4, -9, -10, -1, -3, -6, -2]
    substract_data(L2,5)
    L2.print() # [0, -3, 3, -1, -4]
    substract_data(L3,20)
    L3.print() # [-19, -18, -17]
    
    
    
    
