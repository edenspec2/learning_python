import numpy as np

def get_xyz_df(x, y):
    return x+y

def align_molecules(b):
    return b*3-10

def run_calculation(z):
    return np.array([z, z+1, z+2])

def get_ml_model(a):
    return a**2

if __name__=='__main__':
    print('all good')
