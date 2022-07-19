import pandas as pd
import numpy as np

def text_to_matrix(file_name):
    with open(file_name,'r') as my_file:
        matrix=my_file.readlines()
    return matrix

pdb_filename='A_THR_13_5Angs_noHOH.pdb'
file_lines=text_to_matrix(pdb_filename)

split_result=pdb_filename.split('_') # ['A', 'THR', '13', ...]
##amino_acid_chain=split_result[0]
##amino_acid_name=split_result[1]
##amino_acid_place=split_result[2]
amino_acid_chain, amino_acid_name, amino_acid_place=split_result[:3]

my_file=[line.split() for line in file_lines]
##my_file=[]
##for lines in file:
##    my_file.append(lines.split())

pdb_file_columns=['Kind','', 'Atom name','Amino acid name', 'chain_number','place in chain','x','y','z','relative place','','Atom']

my_database=pd.DataFrame(my_file,columns=pdb_file_columns)
new_database=my_database[['Amino acid name','chain_number','place in chain','x','y','z', 'Atom']]
mask_1=new_database['chain_number']==amino_acid_chain
mask_2=new_database['Amino acid name']==amino_acid_name
mask_3=new_database['place in chain']==amino_acid_place
total_mask=mask_1&mask_2&mask_3

avg_xyz=new_database[['x','y','z']].astype(float).mean()
##print(avg_xyz)
new_database[['x','y','z']]=(new_database[['x','y','z']].astype(float)-np.array(avg_xyz))
##print(new_database[total_mask].shape[0])

output_filename="output_xyz.xyz"
number_of_atoms=new_database[total_mask].shape[0]
atoms_np_array=new_database[total_mask][['Atom', 'x','y','z']].to_numpy()
print(atoms_np_array)
with open(output_filename, 'w') as xyz_file:
    xyz_file.write("{}\n{}\n".format(number_of_atoms,'title'))
    for atom_np_array in atoms_np_array:
       xyz_file.write("{:4} {:11.6f} {:11.6f} {:11.6f}\n".format(*atom_np_array)) # *unpacking iterables
    
##if __name__=='__main__':
##    pass
