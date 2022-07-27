import sys
path_to_add=r'C:\Users\avishayk\Documents\GitHub\learning_python'
path_to_add=r'C:\Users\עדן\Documents\GitHub\learning_python\python_stuff'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import os
import json
import itertools
import math
from collections import Counter
from enum import Enum
 
"""
##parameters to find using xyz- avr/max radius, double and single bonds, average bond distance
##
dataframe_colums_exampe=['id','En','number_of_atoms','radius/diameter','double_bonds'?,'nof_atoms','dipol_data']

"""
class MLConstants(Enum):
    atoms=['H','C','N','O','S','F','Si','P','Cl','Br','I']

    
def json_file_to_text(filename='pubChem_p_00000001_00025000.json'):
    f=open(filename)
    data_file=json.load(f)
    f.close()
    return data_file


##def get_atom_type_count(molecule):
##        molecule_string=json.dumps(molecule)
##        carbon_count,hydrogen_count,nof_count,halogen_counter,other_couner=0,0,0,0,0
##        results=[]
##        nof=['N','O','F']
##        halogen=['F','Cl','Br','I']
##        other=['P','Si','S']
##        for atom in molecule_string:
##            if atom=='C':
##                carbon_count+=1
##            elif atom=='H':
##                hydrogen_count+=1
##            elif atom in nof:
##                nof_count+=1
##            elif atom in halogen:
##                halogen_count+=1
##            elif atom in other:
##                other_count+=1
##            results=[carbon_count,hydrogen_count,nof_count,halogen_counter,other_couner]
##        return results
##
##def get_atoms_type_count(molecules):
##    counter=[get_atom_type_count(atom) for atom in molecules]
##    return counter

def get_atom_type_count(molecule):
    molecule_string=json.dumps(molecule)
    counter=Counter(molecule_string)
    new_counter={}
    for key,value in counter.items():
        if key in MLConstants.atoms.value:
            new_counter[key]=value
    return new_counter

def get_atoms_type_count(molecules):
    atoms_counter=[get_atom_type_count(molecule) for molecule in molecules]
    return atoms_counter

        

##def atom_type_count(molecule_string):
##    my_count=Counter(molecule['atoms'] for molecule in molecule_string)
##    return my_count

def double_bond_count():
    pass

def molecule_to_coordinates_array(molecule):
    xyz_coordinates=[atom['xyz'] for atom in molecule] ## instead of creating a list , then a loop with append.
    return xyz_coordinates

def molecules_to_coordinates_array(molecule_string,column='atoms'):
    xyz_coordinates=[np.array(molecule_to_coordinates_array(molecule[column])) for  molecule in molecule_string]
    return xyz_coordinates

def sum_atoms_in_molecule(molecule_string): #not working
    count=[len(molecule['atoms']) for molecule in molecule_string]
    return count
    
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

def molecules_max_lenght(coordinates):
    max_lenght_array=[molecule_max_lenght(single_atom) for single_atom in coordinates]
    return max_lenght_array
    

def get_sorted_dataframe_from_molecules(molecules):
    pass

def get_mw_single_molecule(molecule):
    counter=get_atom_type_count(molecule)
    mw=0
    for key,value in counter.items():
        mw+=counter[key]*value
    return mw
    
    


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

    periodic_table = {
            'H':[1, 1.0079],
            'C':[6, 12.0107],
            'N':[7, 14.0067],
            'O':[8, 15.9994],
            'S':[16, 32.065],
            'F':[9, 18.9984],
            'Si':[14, 28.0855],
            'P':[15, 30.9738],
            'Cl':[17, 35.453],
            'Br':[35, 79.904],
            'I': [53, 126.9045]
            }


    file_txt=json_file_to_text('pubChem_p_00000001_00025000.json')
    string_molecule_1=json.dumps(file_txt[0])  



    xyz_all_molecules=molecules_to_coordinates_array(file_txt[0:3],'atoms')
    three_atoms=file_txt[0:2]
    atom_count=sum_atoms_in_molecule(three_atoms)

    
    molecule_1=file_txt[0]
    xyz_all_molecules=molecules_to_coordinates_array(file_txt[0:4])
    atom_test_veriable=file_txt[0:4]
    atom_count=sum_atoms_in_molecule(atom_test_veriable)

    print(atom_count)
##    for at in file_txt[0:3]:
##        print(at)
    print(xyz_all_molecules)



    print(molecules_max_lenght(xyz_all_molecules))
    counter=get_atoms_type_count(atom_test_veriable)
    print(counter)
    print(get_mw_single_molecule(molecule_1))




    
##    print(xyz_all_molecules)  #works
##    for at in atom_count:
##        print(at)

   
            

##  D = pdist(X) #ecludian distance
    
##    ind=0
##    molecule_energy,molecule_mltipoles,molecule_id=[],[],[]
##    for molecule in file_txt:
##        molecule_energy.append(molecule['En'])
##        molecule_mltipoles=molecule['shapeM']
##        molecule_id[ind]=molecule['id']
##    print(molecule_energy)

    


    

