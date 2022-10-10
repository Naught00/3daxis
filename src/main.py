#!/bin/python3
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
first = True

def main():
    plt.rcParams['toolbar'] = 'None'
    fig = plt.figure(num='3D Political Axis', figsize=(10,10))

#    plt.axes.set_xlim(10)
#    fig.set_ylim3d(10)
#    fig.set_zlim3d(10)


    ax = plt.axes(projection ='3d')

    cords = get_cords(isparty=False)

    party_cords = get_cords(isparty=True)


    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)


    val = [10,0,0]
    labels = ['Y: A/L', 'X: Economic', 'Z: Social']
    colours = ['black', 'black', 'black']


    for v in range(3):
        x = [val[v-0], -val[v-0]]
        y = [val[v-1], -val[v-1]]
        z = [val[v-2], -val[v-2]]
        ax.plot(x,y,z,'k-', linewidth=1)
        ax.text(val[v-0], val[v-1], val[v-2], labels[v], color=colours[v], fontsize=15)

        ax.plot(10,5,5,'k-', linewidth=1)


    ax.plot3D(cords[0], cords[1], cords[2], 'red')
    ax.scatter3D(cords[0], cords[1], cords[2],  c=cords[2], cmap = 'cividis', s=200)

    ax.plot3D(party_cords[0], party_cords[1], party_cords[2], 'red')
    ax.scatter3D(party_cords[0], party_cords[1], party_cords[2],  c='red', cmap = 'cividis', s=200)

    plt.show()


def plot(cords):
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    ax.plot3D(cords, 'blue')

    ax.scatter3D(x, y, z, c=z, cmap = 'cividis')
    plt.show()
    
def get_cords(isparty):
   
    global first
    if first:
        print("Enter value between 1 and 10")
    if isparty:
        x = input("Party Economic (X):")
        y = input("Party AL (Y):")
        z = input("Party Social (Z):")
    else:
        x = input("Economic (X):")
        y = input("AL (Y):")
        z = input("Social (Z):")

    first = False
    x = int(x)
    y = int(y)
    z = int(z)

    if x > 10 or y > 10 or z > 10:
        print("Values must be below 10!")
        exit(-1)
    if x < 1 or y < 1 or z < 1:
        print("Values must be greater than 0!")
        exit(-1)
    return [x, y, z]

main()
