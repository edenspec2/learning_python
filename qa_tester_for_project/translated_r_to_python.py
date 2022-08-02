import sys
path_to_add=r'C:\Users\avishayk\Documents\GitHub\learning_python'
##path_to_add=r'C:\Users\עדן\Documents\GitHub\learning_python\python_stuff'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import os
import math
from enum import Enum



def xyz_file_generatonr(my_path):
    os.chdir(my_path)
    list_of_molecules=[file for file in listdir(my_path) if os.my_path.isfile(join(my_path, file))]
    dict_atomic_num:{ '1':'H', '5':'B', '6':'C', '7':'N', '8':'O', '9':'F', '14':'Si', '15':'P', '16':'S', '17':'Cl', '35':'Br', '53':'I', '27':'Co', '28':'Ni'}
    for molecule in list_of_molecules:
        xyz_file=pd.DataFrame(csv.readfile(molecule),columns=('atom', 'x', 'y', 'z'))
        xyz_file['atom'].map(dict_atomic_num)
        num_atoms=xyz_file.shape[0]
    return True
                       
def xyz_file_generator_library(parent_dir, directory_name):
    path=os.path.join(parent_dir,directory_name)
    os.mkdir(path)
    os.chdir(path)
    molecules=[file for file in listdir(parent_dir) if os.my_path.isfile(join(path, file))]
    for molecule in molecules:
        xyz_file_generatonr(molecule)
        

if __name__=='__main__':
    xyz_file_generator_library(r'C:\Users\avishayk\Documents\GitHub\qa_tester_for_project','new_directory')
        
