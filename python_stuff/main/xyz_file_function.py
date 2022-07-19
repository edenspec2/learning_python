def get_file_lines(filename, encoding=None):
    with open(filename, 'r', encoding=encoding) as f:
        lines=f.readlines()
    return lines

def get_tabular_text_to_matrix(filename, encoding=None):
    """ UPDATE DOC
    a function that recieves a tabular text file and returns a matrix with it's contant .

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
    file_lines=get_file_lines(filename, encoding=encoding)
    splitted_file_lines=[line.split() for line in file_lines]
    return splitted_file_lines

def get_file_striped_lines(filename, encoding=None):
    file_lines=get_file_lines(filename, encoding=encoding)
    strip_lines=[line.strip().rstrip('\n') for line in file_lines]
    return strip_lines
