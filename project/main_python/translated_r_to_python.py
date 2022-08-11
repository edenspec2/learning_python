import sys
##path_to_add=r'C:\Users\avishayk\Documents\GitHub\learning_python'
path_to_add=r'C:\Users\עדן\Documents\GitHub\learning_python\python_stuff'
sys.path.insert(0, path_to_add)

import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import os
import math
from enum import Enum

import xyz_file_function as xyz
import function_reviewed as fr
import csv


class Variables(Enum):
    ATOMIC_DICT={'atom':{ '1':'H', '5':'B', '6':'C', '7':'N', '8':'O', '9':'F', '14':'Si', '15':'P', '16':'S', '17':'Cl', '35':'Br', '53':'I', '27':'Co', '28':'Ni'}}

def xyz_file_generatonr(my_path):###works, name in R:'xyz_file_generator'-currently the R function generates filename without 'xyz_'.
    """
    a function that gets a directory path as my_path,makes xyz files from all csv files in the same directory.
    """
    os.chdir(my_path)
    list_of_molecules=[file for file in os.listdir(my_path) if file.endswith('csv')]
    for molecule in list_of_molecules:
        xyz_file=fr.csv_filename_to_dataframe(molecule,columns=['atom','x','y','z'])
        xyz_file.replace(Variables.ATOMIC_DICT.value,inplace=True)
        new_filename=xyz.change_filetype(molecule)
        xyz.dataframe_to_xyz(xyz_file,new_filename)

    return

def xyz_to_ordered_DataFrame(filename,columns=None):#my help function
    """
    a function witch gets a xyz file name and produces an organized dataframe.
    this function is simillar to fr.csv_filename_to_dataframe with works good on csv files.
    """
    split_lines=xyz.get_file_striped_lines(filename)
    ordered_lines=[line.split(' ') for line in split_lines]
    return pd.DataFrame(ordered_lines,columns=['atom','x','y','z']).fillna('')
    
def move_xyz_files_directory(current_directory,new_directory):#my help function
    """
    a function that moves xyz type files from one directory to another.
    help function for xyz_file_generator_library to move files to the new directory created
    """
    list_of_molecules=[file for file in os.listdir(current_directory) if file.endswith('xyz')]
    for molecule in list_of_molecules:
        current_path=os.path.join(current_directory,molecule)
        new_path=os.path.join(new_directory,molecule)
        os.replace(current_path,new_path)
    return
                       
def xyz_file_generator_library(files_directory_path, directory_name): ###works, name in R:'xyz_file_generator_library'
    path=os.path.join(files_directory_path,directory_name)
    os.mkdir(path)
    xyz_file_generatonr(files_directory_path)
    move_xyz_files_directory(files_directory_path,path)
    return

def change_file_name(files_directory_path,old_file_name,new_file_name):###works, name in R: 'name_changer' 
    """
    a function that gets a directory of the desired file, the name of the file to change, and changes it to a new specified name
    """
    os.chdir(files_directory_path)
    list_of_molecules=[file for file in os.listdir(files_directory_path) ]
    for molecule in list_of_molecules:
        if (molecule==old_file_name):
            os.rename(molecule,new_file_name)
    
    return

def get_angle(p1, p2): ###works, name in R: 'angle' 
    dot_product=np.dot(p1, p2)
    norm_x=np.linalg.norm(p1)
    norm_y=np.linalg.norm(p2)
    thetha=np.arccos(dot_product/(norm_x*norm_y))
    return thetha
                                                            #indexes=[2,4]
def molecule_atom_swapper(files_directory_path,molecule_file_name,indexes):###works, name in R:'swapper'
    """
    a function that gets directory path, molecule file name, and the indexes of the atoms to swap, and overwrite the xyz file with the swapped pair.
    """
    os.chdir(files_directory_path)
    list_of_molecules=[file for file in os.listdir(files_directory_path) if file.endswith('xyz')]
    index_1,index_2=(*indexes,)
    index_1+=-1
    index_2+=-1
    for molecule in list_of_molecules:
        if (molecule==molecule_file_name):
            xyz_file=fr.csv_filename_to_dataframe(molecule)
            xyz_file.drop([0,1],axis=0,inplace=True)
            b, c = xyz_file.iloc[index_1], xyz_file.iloc[index_2]
            temp = xyz_file.iloc[index_1].copy()
            xyz_file.iloc[index_1] = c
            xyz_file.iloc[index_2] = temp
            xyz.dataframe_to_xyz(xyz_file,molecule)
    return


def get_specific_atom_df(molecule_file_name):
    pass

def get_norm(molecule):###help function
    """
    a function that gets xyz coordinates as dataframe and returns the sum of square roots.
    """
    norm=0
    for i in range(0,len(molecule)):
       norm+=(float(molecule[i]))**2
    return math.sqrt(norm)

                                                    #only the number of them
def coordination_transformation(molecule_file_name,base_atoms_indexes):#origin_atom, y_direction_atom, xy_plane_atom
    
    indexes=np.array(base_atoms_indexes)-1
    molecule=(xyz_to_ordered_DataFrame(molecule_file_name)).drop([0,1],axis=0)
    if (len(indexes)==4):
        new_origin=(molecule[['x','y','z']].iloc[indexes[0]].astype(float)+molecule[['x','y','z']].iloc[indexes[1]].astype(float))/2
        new_y=(molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin)/get_norm((molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin))
        coplane=(molecule[['x','y','z']].iloc[indexes[3]]-new_origin)-get_norm(((molecule[['x','y','z']].iloc[indexes[3]].astype(float)-new_origin)))
    else:
        new_origin=molecule[['x','y','z']].iloc[indexes[0]].astype(float)
        new_y=(molecule[['x','y','z']].iloc[indexes[1]].astype(float)-new_origin)/get_norm((molecule[['x','y','z']].iloc[indexes[1]].astype(float)-new_origin))
        coplane=((molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin)-get_norm((molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin)))
    cross_y_plane=pd.Series(np.cross(coplane,new_y),index=['x','y','z'])
    coef_mat=(pd.concat([new_y, coplane, cross_y_plane], axis=1)).T
    angle_new_y_coplane=get_angle(coplane,new_y)
    cop_ang_x=angle_new_y_coplane-(np.pi/2)
    result_vector=[0,np.cos(cop_ang_x),0]
    new_x=pd.Series(np.linalg.solve(coef_mat,result_vector),index=['x','y','z'])
    new_z=pd.Series(np.cross(new_x,new_y),index=['x','y','z'])
    new_basis=(pd.concat([new_x, new_y, new_z], axis=1)).T
    new_coordinates=[]
    transformed_coordinates=[]
    for i in range(0,(molecule.shape[0]-1)):
        x=(molecule[['x','y','z']].iloc[i].astype(float)-new_origin)
        new_coordinates.append(x)
        transformed_coordinates.append(np.dot(new_basis,x))
        

    transformed_coordinates_array=(np.vstack(transformed_coordinates)).round(4)
    new_coordinates_df=pd.DataFrame(new_coordinates)
    transformed_coordinates_df=pd.DataFrame(transformed_coordinates)
    return transformed_coordinates_array,coef_mat
        
        
     
    
    

        
    

if __name__=='__main__':
##    xyz_file_generator_library(r'C:\Users\עדן\Documents\GitHub\learning_python\project\main_python','new_directory') #works
    path=r'C:\Users\עדן\Documents\GitHub\learning_python\project\main_python\new_directory'
    os.chdir(path)
    change_file_name(path,'xyz_csv_file_for_r_1.xyz','xyz_csv_file_for_r_4.xyz')
    molecule_atom_swapper(path,'xyz_csv_file_for_r_2.xyz',[2,4])
  
    
    df=(xyz_to_ordered_DataFrame('xyz_csv_file_for_r_4.xyz')).drop([0,1],axis=0)
    three_molecules=df[['x','y','z']].iloc[3].astype(float)

##    print(three_molecules.iloc[1])
##    print((get_norm(three_molecules.iloc[1])))#first_molecule

    print(coordination_transformation('xyz_csv_file_for_r_4.xyz',[1,2,3]))
##    print(df[['x','y','z']].iloc[0])

   
              
    
    
 


    

   

