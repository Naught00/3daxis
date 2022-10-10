import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def main():
    plt.rcParams['toolbar'] = 'None'
    fig = plt.figure(num='3D Political Axis', figsize=(10,10))

#    plt.axes.set_xlim(10)
#    fig.set_ylim3d(10)
#    fig.set_zlim3d(10)


    ax = plt.axes(projection ='3d')

    cords = get_cords()

    party_cords = get_party_cords()

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)

    ax.plot3D(cords[0], cords[1], cords[2], 'blue')
    ax.scatter3D(cords[0], cords[1], cords[2],  c=cords[2], cmap = 'cividis')

    ax.plot3D(party_cords[0], party_cords[1], party_cords[2], 'blue')
    ax.scatter3D(party_cords[0], party_cords[1], party_cords[2],  c=party_cords[2], cmap = 'cividis')

    plt.show()


def plot(cords):
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    ax.plot3D(cords, 'blue')

    ax.scatter3D(x, y, z, c=z, cmap = 'cividis')
    plt.show()
    
def get_cords():
    x = input("Economic (X):")
    y = input("AL (Y):")
    z = input("Social (Z):")

    x = int(x)
    y = int(y)
    z = int(z)

    return [x, y, z]

def get_party_cords():
    x = input("Party Economic (X):")
    y = input("Party AL (Y):")
    z = input("Party Social (Z):")

    x = int(x)
    y = int(y)
    z = int(z)

    return [x, y, z]

main()
