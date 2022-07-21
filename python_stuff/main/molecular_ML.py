import sys
path_to_add=r'C:\Users\edenspec\Documents\GitHub'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import xyz_file_function as xyz
import os
import json

def json_file_to_text(filename):
    f=open('pubChem_p_00000001_00025000.json')
    data_file=json.load(f)
    return data_file

if __name__=='__main__':
    file_txt=json_file_to_text('pubChem_p_00000001_00025000.json')
##    df=xyz.get_dataframe_from_splitted_lines(file_txt)
##    #column_headlines=['En','atoms','shapeM']
##    first_atom=df.iloc[0]['atoms']
##    second_atom=df.iloc[1]
##    print(first_atom,second_atom)
##    print(file_txt[0])
##    first_molecule=file_txt[0]['atoms']
##    splits = np.array_split(first_molecule, len(first_molecule))
##    print(splits[0][0].values())
##    split_lines=splits[0][0].values()
##    split_list=list(split_lines)
##    print(split_list[1:])
##    xyz_first=split_list[1:]
##    print(xyz_first[0][0])
    print(file_txt[0]['atoms'][0]['xyz'][0])

    

    

