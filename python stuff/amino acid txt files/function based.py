import pandas as pd
import numpy as np
import os

def text_to_matrix(file_name):
    """
    a function that recieves a text file and returns a matrix with it's contant .

    parameters
    ---
    file_name:str
    the name of the file

    returns
    ---
    matrix:two dimentional datastructure containing the text file as strings split by ' '

    examples
    ---
    'my_file_exmaple.pdb'
    ...
    ...
    ATOM   3508  N   THR B   3     120.279 122.945 136.234  1.00 11.70           N  
    ATOM   3509  CA  THR B   3     119.995 122.162 135.043  1.00 11.70           C  
    ATOM   3510  C   THR B   3     120.450 120.735 135.291  1.00 11.70           C
    ...
    ...
    pdb_filename='my_file_exmaple.pdb'
    matrix=text_to_matrix(pdb_filename)
    OUTPUT:
    [['ATOM', '3508', 'N', 'THR', 'B', '3', '120.279', '122.945', '136.234', '1.00', '11.70', 'N'],
    ['ATOM', '3509', 'CA', 'THR', 'B', '3', '119.995', '122.162', '135.043', '1.00', '11.70', 'C'],
    ['ATOM', '3510', 'C', 'THR', 'B', '3', '120.450', '120.735', '135.291', '1.00', '11.70', 'C']]
     
    """
    with open(file_name,'r') as my_file:
        matrix=my_file.readlines()
        my_matrix=[line.split() for line in matrix]
    return my_matrix

def matrix_to_dataframe(matrix, columns=None):
    """
    a function that recieves a matrix and returns it as DataFrame.

    parameters
    ---
    matrix: an array with similar data type.

    columns: adds columns headlines. diffult option as none.

    returns
    ---
    DataFrame: an array that can contain different classes of data.

    examples:
    ---
    matrix
    ...
    [['ATOM', '3508', 'N', 'THR', 'B', '3', '120.279', '122.945', '136.234', '1.00', '11.70', 'N'],
    ['ATOM', '3509', 'CA', 'THR', 'B', '3', '119.995', '122.162', '135.043', '1.00', '11.70', 'C'],
    ['ATOM', '3510', 'C', 'THR', 'B', '3', '120.450', '120.735', '135.291', '1.00', '11.70', 'C']]
    ...
    pdb_file_columns=['Kind','', 'Atom name','Amino acid name', 'chain_number','place in chain','x','y','z','relative place','','Atom']
    dataframe=matrix_to_dataframe(matrix,pdb_file_columns)
    
    OUTPUT:
    Kind        Atom name Amino acid name  ...        z relative place        Atom
0    ATOM   3508         N             THR  ...  136.234           1.00  11.70    N
1    ATOM   3509        CA             THR  ...  135.043           1.00  11.70    C
2    ATOM   3510         C             THR  ...  135.291           1.00  11.70    C  
    """
    
    if columns:
        database=pd.DataFrame(matrix, columns=columns)
    else:
        database=pd.DataFrame(matrix)
    return database

def text_to_dataframe(file_name, columns=None):
    """
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
    matrix=text_to_matrix(pdb_filename)
    my_df=matrix_to_dataframe(matrix, columns=columns)
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

def normalize_coordinates(dataframe):
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
        -5.702893 -5.508459  1.756151  N  
        -4.299893 -5.269459  2.069151  C  
        -3.743893 -4.105459  1.260151  C

    """
    avg_xyz=dataframe.astype(float).mean()
    dataframe=(dataframe.astype(float)-np.array(avg_xyz))
    return dataframe

def customize_columns(dataframe,specific_columns):
    """
     a function that recieves a dataframe and specific column names and returns the dataframe with only the relevant columns.

    parameters
    ---
    dataframe: an array that can contain different classes of data.

    specific_columns:str, the specific columns we want in our new dataframe

    returns
    ---
    dataframe: the same dataframe containing only the specified columns.

    examples:
    ---
    my_dataframe'example_data_frame.pdb'
    ...
    Kind        Atom name Amino acid name  ...        z relative place        Atom
    0    ATOM   3508         N             THR  ...  136.234           1.00  11.70    N
    1    ATOM   3509        CA             THR  ...  135.043           1.00  11.70    C
    2    ATOM   3510         C             THR  ...  135.291           1.00  11.70    C

    my_dataframe=customize_columns(my_dataframe,specific_columns)

    OUTPUT:
    Amino acid name chain_number place in chain  ...         y         z  Atom
0               THR            B              3  ... -5.508459  1.756151     N
1               THR            B              3  ... -5.269459  2.069151     C
2               THR            B              3  ... -4.105459  1.260151     C

    """
    new_dataframe=dataframe[specific_columns]
    return new_dataframe

def create_mask_from_column(dataframe,column_name,column_value):
    mask=dataframe[column_name]==column_value
    return mask
#                                      [name_1, name_2 ..] [value_1, value_2, ..]
def create_mask_from_columns(dataframe, column_names, column_values):
    mask_list=[create_mask_from_column(dataframe, column_name, column_values[column_index]) for column_index, column_name in enumerate(column_names)]
    total_mask=mask_list[0]
    for mask in mask_list[1:]:
        total_mask=total_mask&mask
    return total_mask

def dataframe_to_xyz(dataframe, output_name='xyz file', comment_line='XYZ file'):
    output_filename=output_name
    number_of_atoms=dataframe.shape[0]
    atoms_np_array=dataframe.to_numpy()
    with open(output_filename, 'w') as xyz_file:
        xyz_file.write("{}\n{}\n".format(number_of_atoms, comment_line))
        for atom_np_array in atoms_np_array:
           xyz_file.write("{:4} {:11.6f} {:11.6f} {:11.6f}\n".format(*atom_np_array))

def change_filetype (filename,new_type):
    split_result=filename.split('.')
    if new_type.startswith('.'):
        new_filename=split_result[0]+new_type
    else:
        new_filename=split_result[0]+'.'+new_type
    return new_filename

            

pdb_file_columns=['Kind','', 'Atom name','Amino acid name', 'chain_number','place in chain','x','y','z','relative place','','Atom']
specific_columns=['Amino acid name','chain_number','place in chain','x','y','z', 'Atom']
column_names=['chain_number','Amino acid name','place in chain']

if __name__=='__main__':
    
    list_of_files=os.listdir(r'C:\Users\עדן\Desktop\python stuff\amino acid txt files')
    list_of_pdb_files=[filename for filename in list_of_files if filename.endswith('pdb')]
    print(list_of_pdb_files)
    for pdb_filename in list_of_pdb_files:
        my_database=text_to_dataframe(pdb_filename,columns=pdb_file_columns)
        amino_acid_chain, amino_acid_name, amino_acid_place=pdb_filename_to_identifiers(pdb_filename)
        new_database=customize_columns(my_database,specific_columns)
        total_mask=create_mask_from_columns(new_database, column_names, [amino_acid_chain, amino_acid_name, amino_acid_place])
        new_database.loc[:, ['x','y','z']]=normalize_coordinates(new_database[['x','y','z']].copy())
        output_filename=change_filetype(pdb_filename, 'xyz')
        dataframe_to_xyz(new_database[total_mask][['Atom','x','y','z']],output_filename)
        print(new_database[total_mask][['Atom','x','y','z']])
    matrix=text_to_matrix('B_THR_127_5Angs_noHOH.pdb')
    dataframe=matrix_to_dataframe(matrix,pdb_file_columns)
    dataframe[['x','y','z']]=normalize_coordinates(new_database[['x','y','z']])
    print(customize_columns(dataframe,specific_columns))
    print(list_of_pdb_files)


