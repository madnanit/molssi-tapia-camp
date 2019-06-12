import os
import numpy
import sys

def calculate_distance(coords1,coords2):
# this function has two parameters. It returns the distance b/w atoms.
    """
    this function has two parameters. It returns the distance b/w atoms.
    """
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    xy_distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return xy_distance

def bond_check2(blength, minimum=0, maxmimum=1.5):
    if blength > minimum and blength < maxmimum:
        return True
    else:
        return False
# a function that checks the distance within a range and returns whether it is true or false
# it is based on the distance and we can define the min and max and their default value as well

position_file = sys.argv[1]
# This is an alternative way to read the file. When we run the code, we need to type the full path to the file.

positions = numpy.genfromtxt(fname=position_file, dtype='unicode', skip_header=2)
atoms = positions[:,0]
data = positions[:,1:]
data = data.astype(numpy.float)
atom_num = len(atoms)

for atm1 in range(0,atom_num):
    for atm2 in range(0, atom_num):
        if atm2 > atm1:

            xy_distance = calculate_distance(data[atm1], data[atm2])

            if bond_check2(xy_distance, maxmimum=2) is True:

                print(F'{atoms[atm1]} to {atoms[atm2]} = {xy_distance:.3f}')
