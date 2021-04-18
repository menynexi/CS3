import singly_linked_list as sll
import matplotlib.pyplot as plt

def remove_consonants(word):


def cumulative_sum(n):


def sum_digits_even(n):


def palindrome(word):


def palindrome_helper(word,i,j):

    
def multiply(a,b):


def num_ways(n):


def remove_first_and_last(L):
    
        
def return_kth_to_last(head,k):


def reverse(L):


def substract_data(L,n):

    
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
    
    
    
    
