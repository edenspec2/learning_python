import sys
path_to_add=r'C:\Users\edenspec\Documents\GitHub'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import os
import json
import itertools
from scipy.spatial.distance import pdist

##parameters to find using xyz- avr/max radius, double and single bonds, average bond distance
##


def json_file_to_text(filename):
    f=open('pubChem_p_00000001_00025000.json')
    data_file=json.load(f)
    return data_file


def atom_type_count(molecule_string):
        carbon_count,hydrogen_count,nof_count,hologen_count=0,0,0,0
        halogen=['F','Cl','Br','I']
        nof=['N','O','F']
        for atom in molecule_string:
            if atom=='C':
                carbon_count+=1
            elif atom=='H':
                hydrogen_count+=1
            elif atom in nof:
                nof_count+=1
            elif atom in halogen:
                hologen_count+=1
        results=[carbon_count,hydrogen_count,nof_count,hologen_count]
        return results


def double_bond_count():
    pass

def xyz_one_molecule(molecule):
    xyz_coordinates=[atom['xyz'] for atom in molecule] ## instead of creating a list , then a loop with append.
    return xyz_coordinates

def xyz_to_array(molecule_string,column):
    xyz_coordinates=[np.array(xyz_one_molecule(molecule[column])) for  molecule in molecule_string]
    return xyz_coordinates

def total_type_count(molecule_string): #not working
    count=[np.array(atom_type_count(molecule)) for  molecule in molecule_string]
    return count
    

def atom_count_one_molecule(molecule):
    atom_count=sum(atom_type_count(molecule))
    return atom_count

def atom_count_molecules():
    pass

def bond_count():
    pass

# we need to sort the xyz data by something with norm sum of square roots
def single_bond_lenght():
    pass

def average_bond_lenght():
    pass

def sort_energy_id():
    pass

##def append_to_new_dataframe(dataframe_columns):
##    new_df=[values for values in dataframe_columns]
##    return new_df


if __name__=='__main__':
    
    file_txt=json_file_to_text('pubChem_p_00000001_00025000.json')
    string_molecule_1=json.dumps(file_txt[0])  
    
    sorted_data_molecule_1=[atom_type_count(string_molecule_1),atom_count_one_molecule(string_molecule_1)]
##    print(xyz_molecule)
##    print(sorted_data_molecule_1,type(sorted_data_molecule_1))
##    r = np.linalg.norm(atom_coordinates, axis= 1)
##    df=pd.DataFrame(file_txt)
##    dataframe_columns=[df['En'],df['id']]
##    print(dataframe_columns)

    xyz_all_molecules=xyz_to_array(file_txt[0:3],'atoms')
    atom_count=total_type_count(json.dumps(file_txt[0:3]))
    print(xyz_all_molecules)
    print(atom_count)

            


    
##    c = [list(x) for x in itertools.combinations(range(len(xyz_molecule)), 3 )]
##    distances = []
##    for i in c:    
##        distances.append(np.mean(pdist(xyz_molecule[i,:]))) # pdist: a method of computing all pairwise Euclidean distances in a condensed way.
##    ind = distances.index(max(distances)) # finding the index of the max mean distance
##    rows = c[ind] # these are the points in question
##    print(ind)


    


    

