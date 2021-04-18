import numpy as np
import matplotlib.pyplot as plt
import time
import singly_linked_list as sll

def index_of(L,k):
    count = 0
    t = L.head
    while t!=None:
        if t.data == k:
            return count
        t = t.next
        count +=1
    return -1

def random_list(n):
    L = sll.List()
    L.extend(list(np.random.randint(0, high=10*n, size=n, dtype=int)))
    return L

def length_of_L(L,k):
    count = 0
    t = L.head
    while t!=None:
        t = t.next
        count +=1
    return element_k(L,count-k)

def element_k(L,count):
    t = L.head
    tempCount = 1
    while t!= None:
        if(tempCount == count):
            return t.data
        tempCount+=1
        t = t.next
    return -1
    

def selectionsort(L):    
    temp = L.head
    while (temp != None): 
        least_in_list = temp 
        next_element = temp.next
        
        while (next_element != None): 
            if (least_in_list.data > next_element.data): 
                least_in_list = next_element 
            next_element = next_element.next
            
        swap_variable = temp.data 
        temp.data = least_in_list.data 
        least_in_list.data = swap_variable
        temp = temp.next

    return L

def select_selectionsort(L,k):    
    L = selectionsort(L)        
    return length_of_L(L, k)
    
def select_min(L,k):
    L = selectionsort(L)
    replaceCounterForK = k
    prev = L.head
    current = L.head.next
    while(replaceCounterForK != 0):
        L.head,prev = None,current
        current = current.next
    return current.data

'''
This was my attempt to quicksorting with a link list and it will take a long tiem because a link list has pointers and quicsort is rather random 
def partician(start,end):
    if(start == end or start == None or end == None):
        return start
    
    pivot_prev = start
    current_node = start
    pivot = end.data
    counter = start.data
    
    while(start != end):
        if(pivot > counter):
            pivot_prev.data,current_node.data,start.data = current_node,start,current_node
        start = start.data
    
    temp = current_node
    current_node.data = pivot
    end.data = temp
    
    return pivot_prev
    
def quicksort(start,end):
    if(start == end):
        return
    
    pivot_prev = partician(start, end)
    quicksort(start, pivot_prev)
    
    if(pivot_prev != None and pivot_prev == start):
        quicksort(pivot_prev.next, end)
        
    elif(pivot_prev != None and pivot_prev.next != None):
        quicksort(pivot_prev.next.next, end)
        
    return
'''

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while start!= 0:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def quicksort(arr, start, end):
    if start >= end or start == 0 or end ==0:
        return

    part = partition(arr, start, end)
    quicksort(arr, start, part-1)
    quicksort(arr, part+1, end)

def select_quicksort(L,K):
    arr = []
    t = L.head
    while(t != None):
        arr.append(t.data)
        t = t.next
        
    quicksort(arr,0,len(arr)-1)
    
    L = sll.List()
    for i in arr:
        L.append(i)
    return length_of_L(L, k)
    
def select_modified_quicksort(L,k):
    arr = []
    t = L.head
    while(t != None):
        arr.append(t.data)
        t = t.next
    quicksort_one_call(arr,0,len(arr)-1)

    L = sll.List()
    for i in arr:
        L.append(i)
    return length_of_L(L, k)
    

def quicksort_one_call(arr,start,end):
    while(start < end):
        part = partition(arr, start, end)
        quicksort_one_call(arr, start, part)
        end = part+1
    

if __name__ == "__main__":          
    reps = 3
    first_n, last_n, step_n = 10, 20, 1
    times, sizes = [], []
    for n in range(first_n, last_n, step_n):
        sum_time = 0
        results = []
        for r in range(reps):
            np.random.seed(seed=n+r) # To obtain the same results in every experiment 
            L = random_list(n)
            start = time.time()
            index = index_of(L,2302)
            results.append(index)
            #select_selectionsort(L,k). Sort L using selection sort, then return the element in position k.
            k = 0
            kth_sorting_smallest = select_selectionsort(L, k)
            print('kth_smallest element in list using select_selectionsort',kth_sorting_smallest)
            kth_smallest = select_min(L,k)
            elapsed_time = time.time() - start
            print('kth_smallest element in list using select_min',kth_smallest)
            sum_time += elapsed_time
            kth_smallest_quicksort = select_quicksort(L, k)
            print("Kth_sallest elemtn in the list using quicksort",kth_smallest_quicksort)
            #kth_smallest_select_modofied_quicksort = select_modified_quicksort(L, k)
            #print("Kth_sallest elemtn in the list using select odofied quicksort",kth_smallest_select_modofied_quicksort)
        times.append(sum_time/reps) # Display average time per repetition
        sizes.append(n)
        print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
        print('Results:',results) # Print results to verify that all algorithms return the same value for the same input
        
    #plt.close('all')  # Uncomment to close all previous figures prior to drawing a new one
    fig, ax = plt.subplots()
    plt.plot(sizes,times)
    ax.set_xlabel('n')
    ax.set_ylabel('running time (seconds)')
    fig.suptitle('Running time for index_of function', fontsize=16)  # Replace by your fuction's name
    
    
