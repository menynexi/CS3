#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:27:25 2020

@author: manuelgutierrez
"""

'''
Trace the execution of the following program. Draw the list after every change is performed. Verify your answers
using the code in the List class. No answer submission is necessary.
'''

import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    L = sll.List()
    for i in range(5):
        L.head = sll.ListNode(i,L.head)
    if L.tail == None:
        L.tail = L.head
        L.tail.data = 9
        L.head.data = 8
        L.head.next.data = 4
        L.head = L.head.next
        L.head.next = L.head.next.next
        L.head.next = L.tail
        L.append(-2)
        L.extend([2,4,0,1])
        L.print()
        print(L.head.data)