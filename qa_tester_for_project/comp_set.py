import numpy as np

def get_xyz_df(x,y):
    return x+y

def align_molecules(b):
    return b+2

def run_calculation(z):
    return np.array([z, z+1, z+2])

def get_ml_model(a):
    return a**2

if __name__=='__main__':
    print('all good')


num1=get_xyz_df(2,3)
num2=align_molecules(num1)
num3=(run_calculation(num2))
num4=get_ml_model(num3)
print(num4)
