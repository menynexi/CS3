#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:28:25 2020

@author: manuelgutierrez
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def mysubset_sum(givenSet,givenNumber):
    subset = []
    returnset = []
    for i in range(len(givenSet)):
        for j in range(2,len(givenSet) - 1):
            # iterates by comapring the sum of the first number to all the other numbers in the array
            # comparing if the sum equals the givenNumber
            if(givenSet[i] + givenSet[j] == givenNumber):
                subset.append(givenSet[i])
                subset.append(givenSet[j])
                returnset.append(subset)
                subset = []
    returnset.append(givenNumber)
    return returnset


def draw_squares(ax,n,p,w):
    stack = [[n,p]]
    while len(stack)>0:
        n,p = stack.pop()
        if n>0:
            ax.plot(p[:,0],p[:,1],linewidth=1.0,color='b') # Draw rectangle
            i1 = [1,2,3,0,1]
            stack.append([n-1,p*(1-w) + p[i1]*w])

#helper method that creates a circle with a given center and radius
def circle(center,radius):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*radius*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+radius*np.sin(t)
    y = center[1]+radius*np.cos(t)
    return x,y

def draw_four_circles(ax,n,center,radius):
    stack = [[n,center,radius]]
    while len(stack)>0:
        n,center,radius = stack.pop()
        if n>0:
            x,y = circle(center,radius)
            ax.plot(x,y,linewidth=1.0,color='b')
            stack.append([n-1,[center[0],center[1]+radius],radius/2])
            stack.append([n-1,[center[0],center[1]-radius],radius/2])
            stack.append([n-1,[center[0]+radius,center[1]],radius/2])
            stack.append([n-1,[center[0]-radius,center[1]],radius/2])

def draw_tree(ax,n,x0,y0,dx,dy):
    stack = [[n,x0,y0,dx]] #dy is not needed because it never changes
    while len(stack)>0:
        n,x0,y0,dx = stack.pop()
        if n>0:
            x = [x0-dx,x0,x0+dx]
            y = [y0-dy,y0,y0-dy]
            ax.plot(x,y,linewidth=1.0,color='b')
            stack.append([n-1,x0-dx,y0-dy,dx/2])
            stack.append([n-1,x0+dx,y0-dy,dx/2])


def draw_four_squares(ax,n,center,size):
    if n>0:
        x = center[0] + np.array([-size,-size,size,size,-size])
        y = center[1] + np.array([-size,size,size,-size,-size])
        ax.plot(x,y,linewidth=1.0,color='b')
        for i in range(4):
            draw_four_squares(ax,n-1,[x[i],y[i]],size/2)


def draw_four_squares_stack(ax,n,center,size):
    stack = [[n,center,size]]
    while len(stack)>0:
        n,center,size = stack.pop()
        if n>0:
            x = center[0] + np.array([-size,-size,size,size,-size])
            y = center[1] + np.array([-size,size,size,-size,-size])
            ax.plot(x,y,linewidth=1.0,color='b')
            for i in range(4):
                stack.append([n-1,[x[i],y[i]],size/2])

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()


if __name__ == "__main__":
    print('Question 1')
    print(mysubset_sum([],0))
    print(mysubset_sum([1,3,4,6,7,9],7))
    print(mysubset_sum([1,3,4,6,7,9],10))
    print(mysubset_sum([1,3,4,6,7,9],13))
    print()
    
    print('Question 2')
    plt.close("all") # Close all figures
    orig_size = 1000.0
    p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
    
    fig, ax = plt.subplots()
    draw_squares(ax,6,p,.1)
    set_drawing_parameters_and_show(ax)
    fig.savefig('squares1.png')
    
    fig, ax = plt.subplots()
    draw_squares(ax,10,p,.2)
    set_drawing_parameters_and_show(ax)
    fig.savefig('squares2.png')

    fig, ax = plt.subplots()
    draw_squares(ax,5,p,.3)
    set_drawing_parameters_and_show(ax)
    fig.savefig('squares3.png')

    fig, ax = plt.subplots()
    draw_four_circles(ax, 2, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_circles1.png')

    fig, ax = plt.subplots()
    draw_four_circles(ax, 3, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_circles2.png')

    fig, ax = plt.subplots()
    draw_four_circles(ax, 4, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_circles3.png')

    fig, ax = plt.subplots()
    draw_tree(ax, 4, 0, 0, 500,200)
    set_drawing_parameters_and_show(ax)
    fig.savefig('tree1.png')

    fig, ax = plt.subplots()
    draw_tree(ax, 5, 0, 0, 500,200)
    set_drawing_parameters_and_show(ax)
    fig.savefig('tree2.png')

    fig, ax = plt.subplots()
    draw_tree(ax, 6, 0, 0, 500,200)
    set_drawing_parameters_and_show(ax)
    fig.savefig('tree3.png')
 
    #by takeing th esame parameters as a circle i was able to recreate the square drawings as the cordiantes would be simalar
    fig, ax = plt.subplots()
    draw_four_squares(ax, 2, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_squres1.png')
    
    fig, ax = plt.subplots()
    draw_four_squares(ax, 3, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_squares2.png')

    fig, ax = plt.subplots()
    draw_four_squares(ax, 4, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_squares3.png')

    fig, ax = plt.subplots()
    draw_four_squares_stack(ax, 2, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_squres1_stack.png')
    
    fig, ax = plt.subplots()
    draw_four_squares_stack(ax, 3, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_squares2_stack.png')

    fig, ax = plt.subplots()
    draw_four_squares_stack(ax, 4, [0,0], 100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('four_squares3_stack.png')
    print("Drawings....done")
    
    