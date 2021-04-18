import numpy as np
import matplotlib.pyplot as plt
import math

def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=1.0,color='b') # Draw rectangle
        i1 = [1,2,3,0,1]
        q = p*(1-w) + p[i1]*w
        draw_squares(ax,n-1,q,w)

def draw_four_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=1.0,color='b')
        draw_four_circles(ax,n-1,[center[0],center[1]+radius],radius/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-radius],radius/2)
        draw_four_circles(ax,n-1,[center[0]+radius,center[1]],radius/2)
        draw_four_circles(ax,n-1,[center[0]-radius,center[1]],radius/2)

def draw_tree(ax,n,x0,y0,dx,dy):
    if n>0:
        x = [x0-dx,x0,x0+dx]
        y = [y0-dy,y0,y0-dy]
        ax.plot(x,y,linewidth=1.0,color='b')
        draw_tree(ax,n-1,x0-dx,y0-dy,dx/2,dy)
        draw_tree(ax,n-1,x0+dx,y0-dy,dx/2,dy)

def draw_four_squares(ax,n,center,size):
    if n>0:
        x = center[0] + np.array([-size,-size,size,size,-size])
        y = center[1] + np.array([-size,size,size,-size,-size])
        ax.plot(x,y,linewidth=1.0,color='b')
        for i in range(4):
            draw_four_squares(ax,n-1,[x[i],y[i]],size/2)

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

if __name__ == "__main__":

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

    