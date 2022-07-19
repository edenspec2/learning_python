import function based as fb
import pandas as pd
import numpy as np
import os

pdb_file_columns=['Kind','', 'Atom name','Amino acid name', 'chain_number','place in chain','x','y','z','relative place','','Atom']
specific_columns=['Amino acid name','chain_number','place in chain','x','y','z', 'Atom']
column_names=['chain_number','Amino acid name','place in chain']

list_of_files=os.listdir(r'C:\Users\עדן\Desktop\python stuff\amino acid txt files')
list_of_pdb_files=[filename for filename in list_of_files if filename.endswith('pdb')]
##    print(list_of_pdb_files)
for pdb_filename in list_of_pdb_files:
    my_database=text_to_dataframe(pdb_filename,columns=pdb_file_columns)
    amino_acid_chain, amino_acid_name, amino_acid_place=pdb_filename_to_identifiers(pdb_filename)
    new_database=customize_columns(my_database,specific_columns)
    total_mask=create_mask_from_columns(new_database, column_names, [amino_acid_chain, amino_acid_name, amino_acid_place])
    new_database.loc[:, ['x','y','z']]=normalize_coordinates(new_database[['x','y','z']].copy())
    output_filename=change_filetype(pdb_filename, 'xyz')
