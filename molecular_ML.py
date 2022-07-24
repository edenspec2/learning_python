import sys
path_to_add=r'C:\Users\edenspec\Documents\GitHub'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import os
import json
import itertools
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
"""
##parameters to find using xyz- avr/max radius, double and single bonds, average bond distance
##
dataframe_colums_exampe=['id','En','number_of_atoms','radius/diameter','double_bonds'?,'nof_atoms','dipol_data']

"""
def json_file_to_text(filename):
    f=open('pubChem_p_00000001_00025000.json')
    data_file=json.load(f)
    return data_file


def atom_type_count(molecule_string):

        molecule_string=json.dumps(molecule_string)
        carbon_count,hydrogen_count,nof_count=0,0,0
        results=[]
        nof=['N','O','F']
        for atom in molecule_string:
            if atom=='C':
                carbon_count+=1
            elif atom=='H':
                hydrogen_count+=1
            elif atom in nof:
                nof_count+=1
            results=[carbon_count,hydrogen_count,nof_count]
        return results


def double_bond_count():
    pass

def molecule_to_coordinates_array(molecule):
    xyz_coordinates=[atom['xyz'] for atom in molecule] ## instead of creating a list , then a loop with append.
    return xyz_coordinates

def molecules_to_coordinates_array(molecule_string,column):
    xyz_coordinates=[np.array(molecule_to_coordinates_array(molecule[column])) for  molecule in molecule_string]
    return xyz_coordinates

def sum_atoms_in_molecule(molecule_string): #not working
    count=[len(molecule['atoms']) for molecule in molecule_string]
    return count
    

def atom_count_per_molecule(molecule):
    atom_count=sum(atom_type_count(json.dumps(molecule)))
    return atom_count

def distance_between_two_atoms(atom_a, atom_b):
    distance=math.sqrt(sum((np.array(atom_a)-np.array(atom_b))**2))
    return distance

def molecule_max_lenght(coordinates):
    max_lenght=0
    for point_a in coordinates:
        for point_b in coordinates:
            if distance_between_two_atoms(point_a,point_b)>max_lenght:
                max_lenght=distance_between_two_atoms(point_a,point_b)
    return max_lenght


def bond_count():
    pass

# we need to sort the xyz data by something with norm sum of square roots
def single_bond_lenght():
    pass

def average_bond_lenght():
    pass

def molecule_radius():
    pass


##def append_to_new_dataframe(dataframe_columns):
##    new_df=[values for values in dataframe_columns]
##    return new_df


if __name__=='__main__':

    periodic_table = {'H':[1, 1.0079],
            'C':[6, 12.0107],
            'N':[7, 14.0067],
            'O':[8, 15.9994],
            'S':[16, 32.065],
            'F':[9, 18.9984],
            'Si':[14, 28.0855],
            'P':[15, 30.9738],
            'Cl':[17, 35.453],
            'Br':[35, 79.904],
            'I': [53, 126.9045]}
         
    file_txt=json_file_to_text('pubChem_p_00000001_00025000.json')
    string_molecule_1=json.dumps(file_txt[0])  

##    ind=0
##    molecule_energy,molecule_mltipoles,molecule_id=[],[],[]
##    for molecule in file_txt:
##        molecule_energy[ind]=molecule['En']
##        molecule_mltipoles=molecule['shapeM']
##        molecule_id[ind]=molecule['id']
##        ind+=1
    

    xyz_all_molecules=molecules_to_coordinates_array(file_txt[0:1],'atoms')
    three_atoms=file_txt[0:2]
    atom_count=sum_atoms_in_molecule(three_atoms)
    print(atom_count)
##    for at in file_txt[0:3]:
##        print(at)

    print(molecule_max_lenght(xyz_all_molecules[0]))
    counter={x:i.count(x) for x in i}

    
##    print(xyz_all_molecules)  #works
##    for at in atom_count:
##        print(at)
##    print(atom_type_count(string_molecule_1))  #works
##    for ap in string_molecule_1:
##        print(ap)
            

##  D = pdist(X) #ecludian distance
    
    

    


    

