import sys
path_to_add=r'C:\Users\edenspec\Documents\GitHub'
sys.path.insert(0, path_to_add)

import pandas as pd
import numpy as np
import os

##import learning_python.python_stuff.main.xyz_file_function as eden_script
##eden_script.get_file lines()
##
##from learning_python.python_stuff.main.xyz_file_function import get_file lines
##get_file_lines()
##
##from learning_python.python_stuff.main.xyz_file_function import * # import all
##get_file_lines()

import xyz_file_function as xyz_lib
##from learning-python.python_stuff.main.xyz_file_function import *


def csv_filename_to_dataframe(filename, columns=None):
    """UPDATED DOC
    a function that recieves a text and returns it as DataFrame.

    parameters
    ---
    file_name:str
    the name of the file

    columns: adds columns headlines. diffult option as none.

    returns
    ---
    DataFrame: an array that can contain different classes of data.

    examples:
    ---
    'my_file_exmaple.pdb'
    ...
    ATOM   3508  N   THR B   3     120.279 122.945 136.234  1.00 11.70           N  
    ATOM   3509  CA  THR B   3     119.995 122.162 135.043  1.00 11.70           C  
    ATOM   3510  C   THR B   3     120.450 120.735 135.291  1.00 11.70           C

    pdb_file_columns=['Kind','', 'Atom name','Amino acid name', 'chain_number','place in chain','x','y','z','relative place','','Atom']
    pdb_filename='my_file_exmaple.pdb'

    dataframe=text_to_dataframe(pdb_file_columns,pdb_file_columns)
    
    OUTPUT:
     Kind        Atom name Amino acid name  ...        z relative place        Atom
    0    ATOM   3508         N             THR  ...  136.234           1.00  11.70    N
    1    ATOM   3509        CA             THR  ...  135.043           1.00  11.70    C
    2    ATOM   3510         C             THR  ...  135.291           1.00  11.70    C 
    """
    splitted_lines=xyz_lib.convert_tabular_text_to_matrix(filename)
    my_df=xyz_lib.get_dataframe_from_splitted_lines(splitted_lines, columns=columns)
    return my_df


def pdb_filename_to_identifiers(pdb_filename):
    """
    a function that recieves a pdb_filename and returns the relevant identifiers from the name as parameters.

    parameters
    ---
    pdb_filename:str
    the name of the file

    returns
    ---
    amino_acid_chain:str, the alphabetical representation of the chain
    amino_acid_name:str, the name of the amino acid
    amino_acid_place:str, the place of the amino acid in the chain

    examples:
    ---
    pdb_filename='B_THR_127_5Angs_noHOH.pdb'
    amino_acid_chain, amino_acid_name, amino_acid_place=pdb_filename_to_identifiers(pdb_filename)

    OUTPUT:
    amino_acid_chain: 'B'
    amino_acid_name: 'THR'
    amino_acid_place: '127'

    """
    split_result=pdb_filename.split('_') # ['A', 'THR', '13', ...]
    amino_acid_chain, amino_acid_name, amino_acid_place=split_result[:3]
    return amino_acid_chain, amino_acid_name, amino_acid_place

def get_normalize_coordinates(dataframe,coordinates_normalize_parameter):
    """
     a function that recieves a dataframe containing xyz coordinates of amino acids and normalizes them to origin coordinates.

    parameters
    ---
    dataframe: an array that can contain different classes of data.
    the name of the file

    returns
    ---
    dataframe: the same dataframe with normalized coordinates by deduction of the column average of each coordinate.

    examples:
    ---
    'example_data_frame.pdb'
        x         y      z 
        120.279 122.945 136.234  N  
        119.995 122.162 135.043  C  
        120.450 120.735 135.291  C

    nomalized_dataframe=normalize_coordinates(dataframe)

    OUTPUT:
        -5.702893 -5.508459  1.756151  N  5
        -4.299893 -5.269459  2.069151  C  
        -3.743893 -4.105459  1.260151  C

    """
    dataframe=(dataframe.astype(float)-coordinates_normalize_parameter)
    return dataframe



pdb_file_columns=['Kind','', 'Atom name','Amino acid name', 'chain_number','place in chain','x','y','z','relative place','','Atom']
specific_columns=['Amino acid name','chain_number','place in chain','x','y','z', 'Atom']
column_names=['chain_number','Amino acid name','place in chain']

if __name__=='__main__':
    list_of_files=os.listdir(r'C:\Users\עדן\Documents\GitHub\learning_python\python_stuff\amino_acid_txt')
    list_of_pdb_files=[filename for filename in list_of_files if filename.endswith('pdb')]
    print(list_of_pdb_files)
    for pdb_filename in list_of_pdb_files:
        my_database=filename_to_dataframe(pdb_filename,columns=pdb_file_columns)
        normlize_point=my_database[['x','y','z']].astype(float).mean()
        amino_acid_chain, amino_acid_name, amino_acid_place=pdb_filename_to_identifiers(pdb_filename)
        new_database=xyz_lib.customize_columns(my_database,specific_columns)
        total_mask=xyz_lib.search_multiple_vaules_in_columns(new_database, column_names, [amino_acid_chain, amino_acid_name, amino_acid_place])
        new_database.loc[:, ['x','y','z']]=xyz_lib.get_normalize_coordinates(new_database[['x','y','z']].copy(),normlize_point)
        output_filename=xyz_lib.change_filetype(pdb_filename, 'xyz')
        xyz_lib.dataframe_to_xyz(new_database[total_mask][['Atom','x','y','z']],output_filename)
        new_database[total_mask][['Atom','x','y','z']].to_csv(xyz_lib.change_filetype(pdb_filename, 'csv'))
##        print(new_database[total_mask][['Atom','x','y','z']])


