
import sys
##path_to_add=r'C:\Users\avishayk\Documents\GitHub\learning_python'
path_to_add=r'C:\Users\edens\Documents\GitHub\learning_python\python_stuff'
sys.path.insert(0, path_to_add)

import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import os
import math
from enum import Enum
import xyz_file_function as xyz_lib
import function_reviewed as fr
import csv

class GeneralConstants(Enum):
    """
    Holds constants for calculations and conversions
    1. covalent radii from Alvarez (2008) DOI: 10.1039/b801115j
    2. atomic numbers
    2. atomic weights
    """
    COVALENT_RADII= {
            'H': 0.31, 'He': 0.28, 'Li': 1.28,
            'Be': 0.96, 'B': 0.84, 'C': 0.76, 
            'N': 0.71, 'O': 0.66, 'F': 0.57, 'Ne': 0.58,
            'Na': 1.66, 'Mg': 1.41, 'Al': 1.21, 'Si': 1.11, 
            'P': 1.07, 'S': 1.05, 'Cl': 1.02, 'Ar': 1.06,
            'K': 2.03, 'Ca': 1.76, 'Sc': 1.70, 'Ti': 1.60, 
            'V': 1.53, 'Cr': 1.39, 'Mn': 1.61, 'Fe': 1.52, 
            'Co': 1.50, 'Ni': 1.24, 'Cu': 1.32, 'Zn': 1.22, 
            'Ga': 1.22, 'Ge': 1.20, 'As': 1.19, 'Se': 1.20, 
            'Br': 1.20, 'Kr': 1.16, 'Rb': 2.20, 'Sr': 1.95,
            'Y': 1.90, 'Zr': 1.75, 'Nb': 1.64, 'Mo': 1.54,
            'Tc': 1.47, 'Ru': 1.46, 'Rh': 1.42, 'Pd': 1.39,
            'Ag': 1.45, 'Cd': 1.44, 'In': 1.42, 'Sn': 1.39,
            'Sb': 1.39, 'Te': 1.38, 'I': 1.39, 'Xe': 1.40,
            'Cs': 2.44, 'Ba': 2.15, 'La': 2.07, 'Ce': 2.04,
            'Pr': 2.03, 'Nd': 2.01, 'Pm': 1.99, 'Sm': 1.98,
            'Eu': 1.98, 'Gd': 1.96, 'Tb': 1.94, 'Dy': 1.92,
            'Ho': 1.92, 'Er': 1.89, 'Tm': 1.90, 'Yb': 1.87,
            'Lu': 1.87, 'Hf': 1.75, 'Ta': 1.70, 'W': 1.62,
            'Re': 1.51, 'Os': 1.44, 'Ir': 1.41, 'Pt': 1.36,
            'Au': 1.36, 'Hg': 1.32, 'Tl': 1.45, 'Pb': 1.46,
            'Bi': 1.48, 'Po': 1.40, 'At': 1.50, 'Rn': 1.50, 
            'Fr': 2.60, 'Ra': 2.21, 'Ac': 2.15, 'Th': 2.06,
            'Pa': 2.00, 'U': 1.96, 'Np': 1.90, 'Pu': 1.87,
            'Am': 1.80, 'Cm': 1.69
    }

    ATOMIC_NUMBERS ={
    'atom':{ '1':'H', '5':'B', '6':'C', '7':'N', '8':'O', '9':'F', '14':'Si',
             '15':'P', '16':'S', '17':'Cl', '35':'Br', '53':'I', '27':'Co', '28':'Ni'}}
        

    ATOMIC_WEIGHTS = {
            'H' : 1.008,'He' : 4.003, 'Li' : 6.941, 'Be' : 9.012,
            'B' : 10.811, 'C' : 12.011, 'N' : 14.007, 'O' : 15.999,
            'F' : 18.998, 'Ne' : 20.180, 'Na' : 22.990, 'Mg' : 24.305,
            'Al' : 26.982, 'Si' : 28.086, 'P' : 30.974, 'S' : 32.066,
            'Cl' : 35.453, 'Ar' : 39.948, 'K' : 39.098, 'Ca' : 40.078,
            'Sc' : 44.956, 'Ti' : 47.867, 'V' : 50.942, 'Cr' : 51.996,
            'Mn' : 54.938, 'Fe' : 55.845, 'Co' : 58.933, 'Ni' : 58.693,
            'Cu' : 63.546, 'Zn' : 65.38, 'Ga' : 69.723, 'Ge' : 72.631,
            'As' : 74.922, 'Se' : 78.971, 'Br' : 79.904, 'Kr' : 84.798,
            'Rb' : 84.468, 'Sr' : 87.62, 'Y' : 88.906, 'Zr' : 91.224,
            'Nb' : 92.906, 'Mo' : 95.95, 'Tc' : 98.907, 'Ru' : 101.07,
            'Rh' : 102.906, 'Pd' : 106.42, 'Ag' : 107.868, 'Cd' : 112.414,
            'In' : 114.818, 'Sn' : 118.711, 'Sb' : 121.760, 'Te' : 126.7,
            'I' : 126.904, 'Xe' : 131.294, 'Cs' : 132.905, 'Ba' : 137.328,
            'La' : 138.905, 'Ce' : 140.116, 'Pr' : 140.908, 'Nd' : 144.243,
            'Pm' : 144.913, 'Sm' : 150.36, 'Eu' : 151.964, 'Gd' : 157.25,
            'Tb' : 158.925, 'Dy': 162.500, 'Ho' : 164.930, 'Er' : 167.259,
            'Tm' : 168.934, 'Yb' : 173.055, 'Lu' : 174.967, 'Hf' : 178.49,
            'Ta' : 180.948, 'W' : 183.84, 'Re' : 186.207, 'Os' : 190.23,
            'Ir' : 192.217, 'Pt' : 195.085, 'Au' : 196.967, 'Hg' : 200.592,
            'Tl' : 204.383, 'Pb' : 207.2, 'Bi' : 208.980, 'Po' : 208.982,
            'At' : 209.987, 'Rn' : 222.081, 'Fr' : 223.020, 'Ra' : 226.025,
            'Ac' : 227.028, 'Th' : 232.038, 'Pa' : 231.036, 'U' : 238.029,
            'Np' : 237, 'Pu' : 244, 'Am' : 243, 'Cm' : 247
    }

##class Variables(Enum):
##    ATOMIC_DICT={'atom':{ '1':'H', '5':'B', '6':'C', '7':'N', '8':'O', '9':'F', '14':'Si', '15':'P', '16':'S', '17':'Cl', '35':'Br', '53':'I', '27':'Co', '28':'Ni'}}

def delete_type_files(file_type='xyz'): ## my help function to delete xyz files
    """
    a function that gets a directory path and file type, and deletes all the files of said type.
    """
    list_of_molecules=[file for file in os.listdir() if file.endswith(file_type)]
    for molecule in list_of_molecules:
        os.remove(os.path.abspath(molecule))
        
def convert_csv_to_xyz_df(csv_filename):
    xyz_df=fr.csv_filename_to_dataframe(csv_filename) ### adding columns not working
    xyz_df.rename(columns={0:'atom',1:'x',2:'y',3:'z'},inplace=True)
    xyz_df.replace(GeneralConstants.ATOMIC_NUMBERS.value,inplace=True)
    return xyz_df
   
class XYZHandler():
    """
    A data handler for XYZ files
    """

    def __init__(self):
        self.opened_xyz_files=[]

    def open_xyz_data_from_csv(self, csv_filename):
        xyz_df=convert_csv_to_xyz_df(csv_filename)
        self.opened_xyz_files.append(xyz_df)

def xyz_file_generator(folder_path):###works, name in R:'xyz_file_generator'-currently the R function generates filename without 'xyz_'.
    """
    a function that gets a directory path as folder_path, makes xyz files from all csv files in the same directory.
    This is a void function
    """
    os.chdir(folder_path)
    list_of_csv_files=xyz_lib.get_filename_list('xyz_') #changed to 'xyz_' from .csv
    for csv_filename in list_of_csv_files:
        xyz_df=convert_csv_to_xyz_df(csv_filename)
        new_filename=xyz_lib.change_filetype(csv_filename, new_type=xyz_lib.FileExtensions.XYZ.value)
        xyz_lib.dataframe_to_xyz(xyz_df, new_filename.replace('xyz_','txt_'))
    os.chdir('../')
    return 

def xyz_to_ordered_DataFrame(filename,columns=None):#my help function
    # Im sure that this fucntion is redundent
    """
    a function witch gets a xyz file name and produces an organized dataframe.
    this function is simillar to fr.csv_filename_to_dataframe which works good on csv files.
    """
    strip_lines=xyz_lib.get_file_striped_lines(filename)
    split_lines=[line.split(' ') for line in strip_lines]
    ordered_df=pd.DataFrame(split_lines,columns=xyz_lib.XYZConstants.DF_COLUMNS.value).fillna('') #adding columns work
    return ordered_df

def move_xyz_files_directory(current_directory,new_directory):#my help function
    """
    a function that moves xyz type files from one directory to another.
    help function for xyz_file_generator_library to move files to the new directory created
    A void function
    """
    os.chdir(current_directory)
    list_of_xyz_files=xyz_lib.get_filename_list(xyz_lib.FileExtensions.XYZ.value)
    for xyz_filename in list_of_xyz_files:
        current_path=os.path.join(current_directory, xyz_filename)
        new_path=os.path.join(new_directory, xyz_filename)
        os.replace(current_path,new_path)
    return
                       
def xyz_file_generator_library(files_directory_path, directory_name): ###works, name in R:'xyz_file_generator_library'
    """
    a void function
    """
    path=os.path.join(files_directory_path,directory_name)
    try:
        os.mkdir(path)
        xyz_file_generator(files_directory_path)
        move_xyz_files_directory(files_directory_path,path)
    except FileExistsError:
        xyz_file_generator(files_directory_path)
        move_xyz_files_directory(files_directory_path,path)
    os.chdir('../')
    return

def change_file_name(files_directory_path,old_file_name,new_file_name):###works, name in R: 'name_changer' 
    """
    a function that gets a directory of the desired file, the name of the file to change, and changes it to a new specified name
    A void function
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
    A function that gets directory path, molecule file name, and the indexes of the atoms to swap, and overwrite the xyz file with the swapped pair.
    A void function
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
            c = xyz_file.iloc[index_2]
            temp = xyz_file.iloc[index_1].copy()
            xyz_file.iloc[index_1] = c
            xyz_file.iloc[index_2] = temp
            xyz_lib.dataframe_to_xyz(xyz_file,molecule)
    return 


def get_specific_molecule_df(molecule_file_name):
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
def coordination_transformation(molecule_file_name,base_atoms_indexes,return_variables=False):#origin_atom, y_direction_atom, xy_plane_atom
    indexes=np.array(base_atoms_indexes)-1
    try:
        molecule=(xyz_to_ordered_DataFrame(molecule_file_name)).drop([0,1],axis=0)
        molecule=molecule.reset_index()

    except: #this way it works on csv file as well
        molecule=convert_csv_to_xyz_df(molecule_file_name)
    if (len(indexes)==4):
        new_origin=(molecule[['x','y','z']].iloc[indexes[0]].astype(float)+molecule[['x','y','z']].iloc[indexes[1]].astype(float))/2
        new_y=(molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin)/get_norm((molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin))
        coplane=((molecule[['x','y','z']].iloc[indexes[3]].astype(float)-new_origin)/get_norm((molecule[['x','y','z']].iloc[indexes[3]].astype(float)-new_origin)))
    else:
        new_origin=molecule[['x','y','z']].iloc[indexes[0]].astype(float)
        new_y=(molecule[['x','y','z']].iloc[indexes[1]].astype(float)-new_origin)/get_norm((molecule[['x','y','z']].iloc[indexes[1]].astype(float)-new_origin))
        coplane=((molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin)/get_norm((molecule[['x','y','z']].iloc[indexes[2]].astype(float)-new_origin)))
    cross_y_plane=pd.Series(np.cross(coplane,new_y),index=['x','y','z'])
    coef_mat=(pd.concat([new_y, coplane, cross_y_plane], axis=1)).T
    angle_new_y_coplane=get_angle(coplane,new_y)
    new_origin=molecule[['x','y','z']].iloc[indexes[0]].astype(float) ### check with shahar cause this line make no sense for 4 atom coor. this line exists in R.
    cop_ang_x=angle_new_y_coplane-(np.pi/2)
    result_vector=[0,np.cos(cop_ang_x),0]
    new_x=pd.Series(np.linalg.solve(coef_mat,result_vector),index=['x','y','z'])
    new_z=pd.Series(np.cross(new_x,new_y),index=['x','y','z'])
    new_basis=(pd.concat([new_x, new_y, new_z], axis=1)).T
    new_coordinates=[]
    transformed_coordinates=[]
    for i in range(0,(molecule.shape[0])):
        x=(molecule[['x','y','z']].iloc[i].astype(float)-new_origin)
        new_coordinates.append(x)
        transformed_coordinates.append(np.dot(new_basis,x))
    transformed_coordinates_array=(np.vstack(transformed_coordinates)).round(4)
    atom_array=molecule['atom'].to_numpy()
    transformed_array=np.column_stack((atom_array,transformed_coordinates_array))
    new_filename=xyz_lib.change_filetype(molecule_file_name,'_tc.xyz')
    if return_variables==False:
        with open(new_filename, 'w') as xyz_file:
            xyz_file.write("{}\n{}\n".format(transformed_array.shape[0],''))
            for atom in transformed_array:
                xyz_file.write("{:} {:1.4} {:1.4} {:1.4}\n".format(*atom))
    else:
        return transformed_coordinates_array
     

     
def coordination_transformation_entire_dir(files_directory_path,base_atoms_indexes):
    os.chdir(files_directory_path)
    list_of_molecules=[file for file in os.listdir(files_directory_path) if file.endswith('xyz')]
    for molecule in list_of_molecules:
        coordination_transformation(molecule,base_atoms_indexes)
    os.chdir('../')
    
    
def get_npa_dipole(base_atoms_indexes,sub_atoms=None, file_type='npa', center_of_mass=False):##working- possible to add subunits without xyz files ???
    """
    *this function runs on get_npa_dipole so doesnt need path consider adding option for single molecule_dir like in R
    Parameters
    ----------

    base_atoms_indexes : list
        indexes of atoms in file, works with 3 or 4 numbers. example:[2,3,4].
    file_type : stf, optional
        DESCRIPTION. The default is 'npa'.currently not relevant here(R-list.files) *check
    center_of_mass : bool, optional
        currently not relevant.

    Returns
    -------
    dip_df : pd.DataFrame
        output:            dip_x     dip_y     dip_z     total
xyz_csv_file_for_r_1.csv  0.097437 -0.611775  0.559625  0.834831
    """
    atom_indexes=np.array(base_atoms_indexes)-1
    charges=fr.csv_filename_to_dataframe(xyz_lib.get_filename_list('npa')[0]).astype(float) 
    xyz_df_tc=pd.DataFrame(coordination_transformation(xyz_lib.get_filename_list('xyz_')[0],atom_indexes,return_variables=True)) 
    dip_comp_mat=pd.concat([xyz_df_tc,charges],axis=1).astype(float)
    dip_comp_mat.columns = range(dip_comp_mat.shape[1])
    dip_vector=[]
    dip_comp_mat[4],dip_comp_mat[5],dip_comp_mat[6]=0,0,0 ### create empty new column-checked as empty
    for i in range(0,dip_comp_mat.shape[0]):
        dip_comp_mat[4].iloc[i]=dip_comp_mat[0].iloc[i]*dip_comp_mat[3].iloc[i]
        dip_comp_mat[5].iloc[i]=dip_comp_mat[1].iloc[i]*dip_comp_mat[3].iloc[i]
        dip_comp_mat[6].iloc[i]=dip_comp_mat[2].iloc[i]*dip_comp_mat[3].iloc[i]
    for i in range(4,7):
        dip_vector.append(sum(dip_comp_mat[i]))
    vec_norm=get_norm(dip_vector)
    data=[[dip_vector[0]],[dip_vector[1]],[dip_vector[2]],[vec_norm]]
    dip_df=pd.DataFrame(data,index=['dip_x','dip_y','dip_z','total']).T
    dip_df.rename(index={0:xyz_lib.get_filename_list('xyz_')[0]},inplace=True)
    return dip_df

def get_npa_dipole_df(molecules_dir_path): 
    """
    a function that take path to directory containing molecule dirs with xyz and npa csv 
    and return a dataframe of molecules and dipol info
    
    Parameters
    ----------
    molecules_dir_path : str
        path the the directory contaning molecules dirs.
        
    *this function takes parameters for get_npa_dipole with input commmand
    
    Returns
    -------
    dipole_df : dataframe
        molecules dipole parameters.
        
        Output:
                       dip_x     dip_y     dip_z    total
xyz_molecule_1.csv -0.752835  0.026260  0.236615  0.78958
xyz_molecule_2.csv  1.120679  2.329781 -1.416985  2.94816

    """
    molecules=[molecule_dir for molecule_dir in os.listdir(molecules_dir_path) if os.path.isdir(molecule_dir)]
    base_atoms_input=input('Enter atoms - origin atom, y axis atom and xy plane atom with spaces:')
    base_atoms_indexes=base_atoms_input.split()
    int_list=[int(i) for i in base_atoms_indexes]
    file_type=input('Charge type? (npa, Mulliken, APT):')
    com_bool=input('Use center of mass as origin? (y/n):')### need fixing maybe
    if com_bool=='y':
        com_bool=True
    else:   
        com_bool=False
    df_list=[]
    for molecule in molecules :
        os.chdir(os.path.abspath(molecule))
        single_dipole=get_npa_dipole(int_list,file_type,com_bool)
        df_list.append(single_dipole)
        os.chdir('../')
    dipole_df=pd.concat(df_list, axis=0)
    return dipole_df.round(3)

def get_angles_df_from_csv(atoms_indexes): #gets a list of atom indexes
    """
    a function that gets 3/4 atom indexes, and returns a df of angles-either agnle or dihedral
    """
    indexes=np.array(atoms_indexes)-1 #three atoms-angle four atoms-dihedral
    if len(indexes)==3:
        new_indexes=[indexes[0],indexes[1],indexes[1],indexes[2]]
        column_name=('Angle '+str(atoms_indexes))
    else:
        column_name=('Dihedral '+str(atoms_indexes))
    molecules=[molecule_dir for molecule_dir in os.listdir() if os.path.isdir(molecule_dir)]
    angle_df=pd.DataFrame(columns=[column_name])
    index_name=[]   
    for molecule in molecules:
        xyz_file_generator(os.path.abspath(molecule))
        os.chdir(os.path.abspath(molecule))     
                                 ##need fix-dont make xyz out of dipole/ currently npa-xsls type
        xyz_df=(xyz_to_ordered_DataFrame(xyz_lib.get_filename_list(xyz_lib.FileExtensions.XYZ.value)[0])).drop([0,1],axis=0)
        if(len(indexes)==3):
            first_bond=xyz_df[['x','y','z']].iloc[new_indexes[0]].astype(float)-xyz_df[['x','y','z']].iloc[new_indexes[1]].astype(float)
            second_bond=xyz_df[['x','y','z']].iloc[new_indexes[3]].astype(float)-xyz_df[['x','y','z']].iloc[new_indexes[2]].astype(float)
            angle_df.loc[len(angle_df.index)]=(get_angle(first_bond, second_bond))*(180/math.pi)
            index_name.append(xyz_lib.get_filename_list(xyz_lib.FileExtensions.XYZ.value)[0])
            
        else:
            first_bond=xyz_df[['x','y','z']].iloc[indexes[0]].astype(float)-xyz_df[['x','y','z']].iloc[indexes[1]].astype(float)
            second_bond=xyz_df[['x','y','z']].iloc[indexes[2]].astype(float)-xyz_df[['x','y','z']].iloc[indexes[1]].astype(float)
            third_bond=xyz_df[['x','y','z']].iloc[indexes[3]].astype(float)-xyz_df[['x','y','z']].iloc[indexes[2]].astype(float)
            first_cross=np.cross(first_bond,second_bond)
            second_cross=np.cross(third_bond,second_bond)
            angle_df.loc[len(angle_df.index)]=(get_angle(first_cross, second_cross))*(180/math.pi)
            index_name.append(xyz_lib.get_filename_list(xyz_lib.FileExtensions.XYZ.value)[0])
        delete_type_files() ## delete xyz files
        os.chdir('../')
    angle_df['molecule']=index_name
    angle_df.set_index('molecule',inplace=True)
    return angle_df

def get_angles_df_from_xyz(atoms_indexes): ### very similar to get_angles_df_from_csv only it works on xyz files
    pass
            
    


        
    

if __name__=='__main__':
    # xyz_file_generator_library(r'C:\Users\edens\Documents\GitHub\learning_python\project\main_python','new_directory') #works
    path=r'C:\Users\edens\Documents\GitHub\learning_python\project\main_python\test_dipole'
    os.chdir(path)
    df=get_angles_df_from_csv([2,3,4])
    # df_2=get_npa_dipole_df(path)


    