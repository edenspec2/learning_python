import sys
##path_to_add=r'C:\Users\avishayk\Documents\GitHub\learning_python'
path_to_add=r'C:\Users\עדן\Documents\GitHub\learning_python\python_stuff'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import os
import json
import math
from collections import Counter
from enum import Enum
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
 

class MLConstants(Enum):
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
    column_names=['id','number_of_atoms', 'max_lenght', 'dipole_data','mw','type_count']
    shapeM_names=['shapeM_0','shapeM_1','shapeM_2','shapeM_3','shapeM_4','shapeM_5','shapeM_5','shapeM_6','shapeM_7','shapeM_8','shapeM_9','shapeM_10','shapeM_11','shapeM_12']

    
def json_file_to_text(filename='pubChem_p_00000001_00025000.json'):
    """
    a function that recives a jason file and turns it to the equivalent python object.
    parameters
    ---
    filename:str
    the name of the json file

    returns
    ---
    data_file:the equivalent python object
    """
    
    
    f=open(filename)
    data_file=json.load(f)
    f.close()
    return data_file


def get_atom_type_count(molecule):
    """
    a function that recives a molecule data and returns the molecule's empirical formula .
    parameters
    ---
    molecule: a dictionary containing data for single molecule.
    

    returns
    ---
    new_counter:dictionary, representation of the molecule empirical formula.

    examples
    ---
    molecule_1 =
    {'En': 37.801, 'atoms':
    [{'type': 'O', 'xyz': [0.3387, 0.9262, 0.46]},
    {'type': 'O', 'xyz': [3.4786, -1.7069, -0.3119]},
    {'type': 'C', 'xyz': [1.8428, -1.4073, 1.2523]},
    {'type': 'N', 'xyz': [0.4166, 2.5213, -1.2091]}}
    
    molecule_1_atom_type_count=get_atom_type_count(molecule_1)

    OUTPUT:
    {'O':2, 'C':1, 'N':1}
    """
    molecule_string=json.dumps(molecule)
    counter=Counter(molecule_string)
    new_counter={}
    for key,value in counter.items():
        if key in MLConstants.periodic_table.value:
            new_counter[key]=value
    return new_counter


def get_atoms_type_count(molecules):
    """
    a function that recives molecules data and returns the molecules empirical formula .
    parameters
    ---
    molecules: a list of dictionarys containing data for multiple molecules.
    

    returns
    ---
    atoms_counter:list of dictionaries, each dictionary containing the empirical formula of a molecule

    examples
    ---
    molecule_1&2 =
    [{'En': 37.801, 'atoms':
    [{'type': 'O', 'xyz': [0.3387, 0.9262, 0.46]},
    {'type': 'O', 'xyz': [3.4786, -1.7069, -0.3119]},
    {'type': 'C', 'xyz': [1.8428, -1.4073, 1.2523]},
    {'type': 'N', 'xyz': [0.4166, 2.5213, -1.2091]},
    {'En': 37.801, 'atoms':
    [{'type': 'P', 'xyz': [0.3387, 0.9262, 0.46]},
    {'type': 'N', 'xyz': [3.4786, -1.7069, -0.3119]},
    {'type': 'N', 'xyz': [1.8428, -1.4073, 1.2523]},
    {'type': 'H', 'xyz': [0.4166, 2.5213, -1.2091]}]
    
    molecule_1&2_atom_type_count=get_atoms_type_count(molecule_1&2)

    OUTPUT:
    [{'O':2, 'C':1, 'N':1},{'P':1, 'N':2, 'H':1}]
    """
    atoms_counter=[get_atom_type_count(molecule) for molecule in molecules]
    return atoms_counter


def molecule_to_coordinates_list(molecule):
    """
    a function that recives a molecule data and returns a list with xyz coordinates.
    parameters
    ---
    molecule: a dictionary containing data for single molecule.
    

    returns
    ---
    xyz_coordinates:list, xyz coordinates for each atom in the molecule.

    examples
    ---
    molecule_1 =
    {'En': 37.801, 'atoms':
    [{'type': 'O', 'xyz': [0.3387, 0.9262, 0.46]},
    {'type': 'O', 'xyz': [3.4786, -1.7069, -0.3119]},
    {'type': 'C', 'xyz': [1.8428, -1.4073, 1.2523]},
    {'type': 'N', 'xyz': [0.4166, 2.5213, -1.2091]}}
    
    molecule_1_coordinates=molecule_to_coordinates_list(molecule_1)

    OUTPUT:
    [0.3387, 0.9262, 0.46]
    [3.4786, -1.7069, -0.3119]
    [1.8428, -1.4073, 1.2523]
    [0.4166, 2.5213, -1.2091]
    """
    xyz_coordinates=[atom['xyz'] for atom in molecule] ## instead of creating a list , then a loop with append.
    return xyz_coordinates

def molecules_to_coordinates_array(molecules,column='atoms'):
    """
    a function that recives molecules data and returns an array with xyz coordinates for all molecules.
    parameters
    ---
    molecules: a list of dictionarys containing data for multiple molecules.
    

    returns
    ---
    xyz_coordinates:list, xyz coordinates for each atom in all the molecules.

    examples
    ---
    molecule_1&2 =
    [{'En': 37.801, 'atoms':
    [{'type': 'O', 'xyz': [0.3387, 0.9262, 0.46]},
    {'type': 'O', 'xyz': [3.4786, -1.7069, -0.3119]},
    {'type': 'C', 'xyz': [1.8428, -1.4073, 1.2523]},
    {'En': 44.1107, 'atoms':
    [{'type': 'O', 'xyz': [-0.3716, -0.9039, -0.2836]},
    {'type': 'O', 'xyz': [-1.6132, 3.0213, 0.1787]},
    {'type': 'O', 'xyz': [-1.9869, 1.2054, -1.1367]}]
    
    molecule_1&2_coordinates=molecules_to_coordinates_array(molecule_1&2)

    OUTPUT:
    array[0.3387, 0.9262, 0.46]
         [3.4786, -1.7069, -0.3119]
         [1.8428, -1.4073, 1.2523]
    array[-0.3716, -0.9039, -0.2836]
         [-1.6132, 3.0213, 0.1787]
         [-1.9869, 1.2054, -1.1367]
    
    
    """
    xyz_coordinates=[np.array(molecule_to_coordinates_list(molecule[column])) for  molecule in molecules]
    return xyz_coordinates

def sum_atoms_in_molecule(molecule_string):
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

def get_data_from_shapeM(molecules):
    shapeM_data=[(molecule['shapeM']) for molecule in molecules]
    return shapeM_data

def get_sorted_dataframe_from_molecules(molecules,column_names='none'):
    df=pd.DataFrame(molecules)
    shapeM_df=pd.DataFrame(get_data_from_shapeM(molecules), columns=MLConstants.shapeM_names.value)
    df=df.drop(['En','atoms','shapeM'], axis=1)
    ## adding all the new parameters
    df['molecule max lenght'],df['MW']=molecules_max_lenght(molecules_to_coordinates_array(molecules)),get_mw_many_molecules(molecules)
    df=pd.concat([df, pd.DataFrame(get_atoms_type_count(molecules)).fillna(0),shapeM_df], axis=1)
    df=df.set_index('id')
    return df
    

def get_mw_single_molecule(molecule): 
    counter=get_atom_type_count(molecule)
    mw=0
    for key,value in counter.items():
        mw+=(MLConstants.periodic_table.value[key][1]*value)
    return mw

def get_mw_many_molecules(molecules):
    mw=[get_mw_single_molecule(molecule) for molecule in molecules]
    return mw


def double_bond_count():
    pass


if __name__=='__main__':

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

    pd.set_option('display.max_column', None)
    y_train=pd.DataFrame(file_txt[0:100])['En']
    x_df_train=get_sorted_dataframe_from_molecules(file_txt[0:100])
    x_df_test=get_sorted_dataframe_from_molecules(file_txt[101:200])
    regr = LinearRegression().fit(x_df_train, y_train)
    y_predict=regr.predict(x_df_test)
    y_true=pd.DataFrame(file_txt[101:200])['En']
    print(x_df_train.head())
    print(regr.score(x_df_train, y_train))
    print(r2_score(y_true,y_predict))
    print(file_txt[0])
    print(file_txt[1])
    



    
    

    



    


    



    

        




    
    

    



    


    

