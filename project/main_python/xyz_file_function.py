import pandas as pd
import numpy as np
import os
from enum import Enum

class FileExtensions(Enum):
    """
    Hold commonly used file extensions
    """
    SMI='.smi'
    XYZ='xyz'
    CSV='.csv'
    ZIP='.zip'
    PPT='.ppt'
    CIF='.cif'
    MOL='.mol'
    PDB='.pdb'

class XYZConstants(Enum):
    """
    Constants related to XYZ file processing
    """
    DF_COLUMNS=['atom','x','y','z']

def get_filename_list(file_identifier):
    """
    The function gets a file extension as input and returns a list of all files in the working directory
    ----------
    Parameters
    ----------
    file_extension : str.
        The wanted file identifier like 'txt','info','nbo'..
    -------
    Returns
    -------
    list
        A list of all files in the working directory with the chosen extension 
    --------
    Examples
    --------
    from os import listdir

    all_files_in_dir=listdir()
    print(all_files_in_dir)
        ['0_1106253-mod-mod.xyz', '0_1106253-mod.xyz', '1106253.cif', '1109098.cif', '1_1106253-mod.xyz', 'centered_0_BASCIH.xyz', 'cif_handler.py']
        
    xyz_files_in_dir=get_filename_list('.xyz')
    print(xyz_files_in_dir)
        ['0_1106253-mod-mod.xyz', '0_1106253-mod.xyz', '1_1106253-mod.xyz', 'centered_0_BASCIH.xyz']
    
    cif_files_in_dir=get_filename_list('.cif')
    print(cif_files_in_dir)
        ['1106253.cif', '1109098.cif']    
    """
    from os import listdir
    return [filename for filename in listdir() if file_identifier in filename] 

def get_file_lines(filename, encoding=None):
    """ 
    a function that recieves any text file and returns a string .

    parameters
    ---
    filename:str
    the name of the file

    encoding: specific way to organize the text

    returns
    ---
    lines:str, text file as string

    """
    with open(filename, 'r', encoding=encoding) as f:
        lines=f.readlines()
    return lines

    #old name - get instead of convert
def convert_tabular_text_to_matrix(filename, encoding=None, spliters=(',')):
    """ UPDATE DOC
    a function that recieves a tabular text file and returns a list as an iterator object .

    parameters
    ---
    filename:str
    the name of the file

    encoding: specific way to organize the text

    returns
    ---
    splitted_file_lines:two dimentional datastructure containing the text file.

    examples
    ---
    filename= 'my_file_exmaple.pdb'
    ...
    ...
    ATOM   3508  N   THR B   3     120.279 122.945 136.234  1.00 11.70           N  
    ATOM   3509  CA  THR B   3     119.995 122.162 135.043  1.00 11.70           C  
    ATOM   3510  C   THR B   3     120.450 120.735 135.291  1.00 11.70           C
    ...
    ...
    
    splitted_file_lines=convert_tabular_text_to_matrix(file_lines)
    OUTPUT:
    [['ATOM', '3508', 'N', 'THR', 'B', '3', '120.279', '122.945', '136.234', '1.00', '11.70', 'N'],
    ['ATOM', '3509', 'CA', 'THR', 'B', '3', '119.995', '122.162', '135.043', '1.00', '11.70', 'C'],
    ['ATOM', '3510', 'C', 'THR', 'B', '3', '120.450', '120.735', '135.291', '1.00', '11.70', 'C']]
     
    """
    file_lines=get_file_lines(filename, encoding=encoding)
    splitted_file_lines=[]
    for line in file_lines:
        split_results=[line.split(spliter) for spliter in spliters]
        splitted_file_lines.append(split_results[0])
    # Old version - didn't cover more than one split
    # splitted_file_lines=[line.split(',') for line in file_lines]
    return splitted_file_lines

def get_file_striped_lines(filename, encoding=None):
    """ UPDATE DOC
    a function that recieves a text file and returns a list with the text without start and end spaces, and new lines  .

    parameters
    ---
    filename:str
    the name of the file

    encoding: specific way to organize the text

    returns
    ---
    strip_lines:two dimentional datastructure containing the text file.

    examples
    ---
    filename='my_file_exmaple.pdb'
    ...
    ...
      ATOM   3508  N   THR B   3     120.279 122.945 136.234  1.00 11.70           N  
      ATOM   3509  CA  THR B   3     119.995 122.162 135.043  1.00 11.70           C

    strip_lines=get_file_striped_lines(filename)

    OUTPUT:
    ATOM   3508  N   THR B   3     120.279 122.945 136.234  1.00 11.70           N ATOM   3509  CA  THR B   3     119.995 122.162 135.043  1.00 11.70           C
    
    """
    file_lines=get_file_lines(filename, encoding=encoding)
    strip_lines=[line.strip().rstrip('\n') for line in file_lines]
    return strip_lines

def get_dataframe_from_splitted_lines(splitted_lines, columns=None):
    """
    a function that recieves splited lines in a matrix and returns it as DataFrame with an option to add columns headlines.

    parameters
    ---
    splitted_lines: an array with similar data type.

    columns: adds columns headlines. diffult option as none.

    returns
    ---
    df: an array that can contain different classes of data.

    examples:
    ---
    splitted_lines='my_file_exmaple.pdb'
    ...
    ...
    ATOM   3508  N   THR B   3     120.279 122.945 136.234  1.00 11.70           N  
    ATOM   3509  CA  THR B   3     119.995 122.162 135.043  1.00 11.70           C  
    ATOM   3510  C   THR B   3     120.450 120.735 135.291  1.00 11.70           C
    ...
    pdb_file_columns=['Kind','', 'Atom name','Amino acid name', 'chain_number','place in chain','x','y','z','relative place','','Atom']
    dataframe=get_dataframe_from_splitted_lines(splitted_lines,pdb_file_columns)
    
    OUTPUT:
    Kind        Atom name Amino acid name  ...        z relative place        Atom
0    ATOM   3508         N             THR  ...  136.234           1.00  11.70    N
1    ATOM   3509        CA             THR  ...  135.043           1.00  11.70    C
2    ATOM   3510         C             THR  ...  135.291           1.00  11.70    C  
    """
    
    if columns:
        df=pd.DataFrame(splitted_lines, columns=columns,dtype=float)
    else:
        df=pd.DataFrame(splitted_lines,dtype=float)
    return df

def get_normalize_coordinates(df,coordinates_normalize_parameter):
    """
     a function that recieves a dataframe containing xyz coordinates of amino acids and normalizes them by reduction of a normalization value.

    parameters
    ---
    dataframe: an array that can contain different classes of data.
    the name of the file

    coordinates_normalize_parameter:float, a numerical value to normalize the coordinates (can be mean, avr etc)

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
    df=(df.astype(float)-coordinates_normalize_parameter)
    return df

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
    my_dataframe='example_data_frame.pdb'
    ...
    Kind        Atom name Amino acid name  ...        z relative place        Atom
    0    ATOM   3508         N             THR  ...  136.234           1.00  11.70    N
    1    ATOM   3509        CA             THR  ...  135.043           1.00  11.70    C
    2    ATOM   3510         C             THR  ...  135.291           1.00  11.70    C

    new_dataframe=customize_columns(my_dataframe,specific_columns)

    OUTPUT:
    Amino acid name chain_number place in chain  ...         y         z  Atom
0               THR            B              3  ... -5.508459  1.756151     N
1               THR            B              3  ... -5.269459  2.069151     C
2               THR            B              3  ... -4.105459  1.260151     C

    """
    new_dataframe=dataframe[specific_columns]
    return new_dataframe

def search_a_value_in_column(dataframe,column_name,column_value):
    """
     a function that recieves a dataframe, a specific column name and a column value, and returns a list with True where the value is found and False otherwise .

    parameters
    ---
    dataframe: an array that can contain different classes of data.
    column_name:str, the specific column we want find our value in.
    column_value: str, the specific value we search for.

    returns
    ---
    mask: a list of True where the value is found and False otherwise
    examples:
    ---
        my_dataframe'example_data_frame.pdb'
    ...
    Kind        Atom name Amino acid name  ...        z relative place        Atom
    0    ATOM   3508         N             THR  ...  136.234           1.00  11.70    N
    1    ATOM   3509        CA             THR  ...  135.043           1.00  11.70    C
    2    ATOM   3510         C             THR  ...  135.291           1.00  11.70    C

    mask=create_mask_from_column(my_dataframe,'Amino','CA')

    OUTPUT:
    0      False
    1      True
    2      False
    
    """
    mask=dataframe[column_name]==column_value
    return mask

#                                      [name_1, name_2 ..] [value_1, value_2, ..]
def search_multiple_vaules_in_columns(dataframe, column_names, column_values):
    """
     a function that recieves a dataframe, specific columns and column values, and returns a list of the True for rows where the values were found in the colums and False otherwise  .

    parameters
    ---
    dataframe: an array that can contain different classes of data.
    column_names:str, the specific columns we want to find our values in.
    column_values: str, the specific values we search for .
    

    returns
    ---
    total_mask: a list of the True in rows where the values were found in the colums and False otherwise
    examples:
    ---
        my_dataframe='example_data_frame.pdb'
        
        Kind        Atom name Amino acid name  ...        z relative place        Atom
    0    ATOM   3508         N             THR  ...  136.234           1.00  11.70    N
    1    ATOM   3509        CA             THR  ...  135.043           1.00  11.70    C
    2    ATOM   3510         C             THR  ...  135.291           1.00  11.70    C
    total_mask=create_mask_from_columns(my_dataframe, column_names=['Amino acid name','Atom'], ['THR','N'])

    OUTPUT:
    0      True
    1      False
    2      False
    
        
    """
    mask_list=[search_a_value_in_column(dataframe, column_name, column_values[column_index]) for column_index, column_name in enumerate(column_names)]
    total_mask=mask_list[0]
    for mask in mask_list[1:]:
        total_mask=total_mask&mask
    return total_mask

def dataframe_to_xyz(dataframe, output_name, comment_line=''):
    """

     a function that recieves a dataframe, output name, and comment line and creates a xyz type file.
     
    parameters

    ---

    dataframe: an array that can contain different classes of data, needs to be 4 colums to run.

    output_name:str, the name for the file created.

    comment_line: str, the headline of the file .
    ---

    examples:
    ---
    """
    number_of_atoms=dataframe.shape[0]
    atoms_np_array=dataframe.to_numpy()
    with open(output_name, 'w') as xyz_file:
        xyz_file.write("{}\n{}\n".format(number_of_atoms, comment_line))
        for atom_np_array in atoms_np_array:
            try:
                xyz_file.write("{:1} {:11.20} {:11.20} {:11.20}".format(*atom_np_array))
            except:
                xyz_file.write("{:1}".format(*atom_np_array))

                               
def change_filetype (filename,new_type='xyz'):
    """
    a function that recieves a file name, and a new type, and changes the type-ending of the file's name to the new one.

    parameters
    ---
    filename: str, the file we want to change

    new_type:str, the new ending we want for the file

    returns
    ---
    the same file name with a new type ending

    examples
    ---
    filename='B_THR_127_5Angs_noHOH.pdb'
    new_filename=change_filetype(filename,'xyz')
    OUTPUT:'B_THR_127_5Angs_noHOH.xyz'
    
    """
    split_result=filename.split('.')
    if '.' in new_type:
        new_filename=split_result[0]+new_type
    else:
        new_filename=split_result[0]+'.'+new_type
    return new_filename
