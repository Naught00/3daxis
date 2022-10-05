import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def main():
    fig = plt.figure()
    ax = plt.axes(projection ='3d')

    cords = get_cords()

    party_cords = get_party_cords()

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
    y = input("GALTAN (Y):")
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
