import sys
##path_to_add=r'C:\Users\avishayk\Documents\GitHub\learning_python'
path_to_add=r'C:\Users\עדן\Documents\GitHub\learning_python\python_stuff'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import os
import math
from enum import Enum
from os import listdir
import xyz_file_function as xyz
import function_reviewed as fr
import csv

class Variables(Enum):
    ATOMIC_DICT={'atom':{ '1':'H', '5':'B', '6':'C', '7':'N', '8':'O', '9':'F', '14':'Si', '15':'P', '16':'S', '17':'Cl', '35':'Br', '53':'I', '27':'Co', '28':'Ni'}}

def xyz_file_generatonr(my_path):
    os.chdir(my_path)
    list_of_molecules=[file for file in os.listdir(my_path) if file.endswith('csv')]
    
    for molecule in list_of_molecules:
        xyz_file=fr.filename_to_dataframe(molecule,columns=['atom','x','y','z'])
        xyz_file.replace(Variables.ATOMIC_DICT.value,inplace=True)
        num_of_atoms=pd.Series([xyz_file.shape[0]],name='number_of_atoms')
        xyz_file=pd.concat([num_of_atoms, xyz_file],axis=1)
        xyz_file.fillna('',inplace=True)

       
    return xyz_file
                       
def xyz_file_generator_library(parent_dir, directory_name):
    path=os.path.join(parent_dir,directory_name)
    os.mkdir(path)
    os.chdir(path)
    molecules=[file for file in listdir(parent_dir) if os.my_path.isfile(join(path, file))]
    for molecule in molecules:
        xyz_file_generatonr(molecule)

def get_angle_between_coordinates(p1, p2): ###works, name in R: 'angle' 
    dot_product=np.dot(p1, p2)
    norm_x=np.linalg.norm(p1)
    norm_y=np.linalg.norm(p2)
    thetha=np.arccos(dot_product/(norm_x*norm_y))
    return thetha
  
        
    

if __name__=='__main__':
##    xyz_file_generator_library(r'C:\Users\עדן\Documents\GitHub\learning_python','new_directory')
        
    df=xyz_file_generatonr(r'C:\Users\עדן\Documents\GitHub\learning_python\project\main_python')
    
    print(df)
  

