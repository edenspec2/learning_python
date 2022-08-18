import comp_set
from enum import Enum

import inspect as an
import numpy as np

def get_module_function_dict(module):
    """
    takes a module and returns a dictionary where every key is the name of the function,
    and the values are the actual functions
    Example:
    get_module_function_dict(comp_set)
    {'align_molecules': <function align_molecules at 0x000002DCE736AB88>,
    'get_ml_model': <function get_ml_model at 0x000002DCE736AEE8>,
    'get_xyz_df': <function get_xyz_df at 0x000002DCE73198B8>,
    'run_calculation': <function run_calculation at 0x000002DCE736AC18>}
    """
    from inspect import getmembers, isfunction
    function_dict=dict(getmembers(module, isfunction)) #getmembers()- return information on an object class,function etc, isfunction is the condition to return info only on functions
    return function_dict

class BuildingBlockFunctions(Enum):
    """
    NAME_TO_FUNCTION_NAME_DICT-Holds a function referral dictionary,
    where every key is the name of the new function, and the value is the name of the old function
    """
                                # Name in R : Name in python
                                # Spoken name : Actual name
    NAME_TO_FUNCTION_NAME_DICT={'xyz_file_generator' : 'xyz_file_generator',
                                'xyz_file_generator_library' : 'xyz_file_generator_library',
                                'name_changer' : 'change_file_name',
                                'angle' : 'get_angle',
                                'swapper' : 'molecule_atom_swapper',
                                'corr_trans' : 'coordination_transformation',
                                'dipole' : 'get_npa_dipole',
                                }

#Assumption - Output -> Input in automation cycles
class AutomationCycles(Enum):
    """
    Hold iterables of common automation cycles
    Automation cycle is defined as a sequence of functions that generally run togather
    """
    COMP_SET=('align_molecules','get_xyz_df', 'run_calculation', 'get_ml_model')
    GET_ANGLE_FROM_XYZ=('xyz_file_generator', 'get_angle_between_two_atoms', 'get_angle')

class ValidationData(Enum):
    """
    Holds validation referral dictionary, where every key is the name of the function, and the value is the input data to validate the function works well
    """
    DATA_DICT={} ##updated when a qa_tester object is created

def get_building_block_name(building_block_name='function_name'):
    """
    The function gets a new building block name and returns the corresponding old building block function name
    """
    return BuildingBlockFunctions.NAME_TO_FUNCTION_NAME_DICT.value.get(building_block_name)

def get_building_block(building_block_name='function_name', module=None):
    """
    The function gets a building block name and returns the corresponding old building block actual function 
    """
    building_block_actual_name=get_building_block_name(building_block_name)
    function_dict=get_module_function_dict(module)
    actual_building_block=function_dict.get(building_block_actual_name)
    return actual_building_block

def check_building_block_many_input(new_building_block_name, validation_data=None):# right now not working with (x,y) but work with ((x,y),(a,b))
    """
    a function that is similar to check_building_block_solely, but gets an iter of validation data and checks them all.
    """
    try:
        iter(validation_data) 
        reults=[check_building_block_solely(new_building_block_name,data) for data in validation_data]
        return reults
    except:
        return check_building_block_solely(new_building_block_name,validation_data)


## for use in check_building_block_solely
def check_input_validity(building_block, validation_data):
    """
    a function that checks the validity of the arguments the function gets
    """
    try:
        value=building_block(*validation_data)
        return True
    except:
        return False

def relative_error(number_1, number_2):
    return 100*abs(number_1-number_2)/min(number_1, number_2)

def compare_numeric_results(number_1, number_2, error_percentage=1):
    if relative_error(number_1, number_2)<=error_percentage:
        return True
    return False

# Assumes that the output types is identical
def compare_output_results(output_1, output_2, error_percentage=1):
    if isinstance(output_1, float) or isinstance(output_1, int): 
        return compare_numeric_results(output_1, output_2, error_percentage)
            
def check_building_block_solely(new_building_block_name, new_building_block, validation_data=None, module=None):
    """
    The function a new building block and validation data, and checks whether the operation of the new building block
    is identical to the old building block it suppose to replace.
    The function will return True if the operation is identical and False otherwise
    """
    ## works with iter or single value
    # Check all validation data on building_block_1 -> if failed -> return False
    # Check all validation data on building_block_2 -> if failed -> return False
    # If the results from both run are identical -> return True
    old_building_block=get_building_block(new_building_block_name, module)
    if check_input_validity(old_building_block,(validation_data)):
        if check_input_validity(new_building_block,(validation_data)):
            return compare_output_results(old_building_block(*validation_data), new_building_block(*validation_data))
    else:
        return False

def get_new_automation_cycle_test(new_building_block_name,automation_cycle):
    """
    help function to create new automation cycle with the new building block to check integration
    """
    old_function_name=BuildingBlockFunctions.FUNCTION_DICT.value.get(new_building_block_name)
    new_automation_cycle=[]
    for function_name in automation_cycle:
        if function_name==old_function_name:
            new_automation_cycle.append(new_building_block_name)
        else:
            new_automation_cycle.append(function_name)
    return new_automation_cycle
    
def get_new_module_dict_test(module,new_building_block_name): ## works
    """
    help function to create new dict of module functions with the new building block  replacing the old one to check integration
    """
    function_dict=get_module_function_dict(module)
    old_function_name=BuildingBlockFunctions.FUNCTION_DICT.value.get(new_building_block_name)
    new_dict={}
    for key,value in function_dict.items():
        if key==old_function_name:
            new_dict.update({new_building_block_name:BuildingBlockFunctions.FUNCTION_USE_DICT.value.get(new_building_block_name)})
        else:
            new_dict.update({key:value})
    return new_dict

#Assumption - Output -> Input in automation cycles
def run_automation_cycle(module, automation_cycle, validation_data):
    """
    goes trough every function in the automation_cycle, where the output of the first function is
    the output of the next function and so on..
    """
    function_dict=get_module_function_dict(module)
    first_function=function_dict.get(automation_cycle[0])
    mid_results=first_function(*validation_data)
    for function_name in automation_cycle[1:]:
        actual_function=function_dict.get(function_name)
        mid_results=actual_function(mid_results)
    return mid_results

def check_building_block_integration(module, new_building_block_name, automation_cycle,validation_data): 
    """
    The function get a building block, it's name and the automation cycle wanted for testing.
    The function will run the automation cycle as is and with the new building block - and checks whether the results are identical.
    The function will return True if the operation is identical and False otherwise
    use dictionary of new and old names to change between the 
    """
    automated_results=run_automation_cycle(module, automation_cycle,validation_data)
    return automated_results
##    new_automated_cycle=get_new_automation_cycle_test(new_building_block_name,automation_cycle)
##    new_module_dic=get_new_module_dict_test(module,new_building_block_name)
##    new_automated_results=run_new_automation_cycle(new_module_dic,new_automated_cycle,validation_data)
##    return (all(automated_results==new_automated_results))

    # Since this runs will take time - consider saving the output of known cycles
    # Think of how to store the automation cycles validation data
    # Check the run with the new building block
    # If the results from both run are identical -> return True AND save the new output(as in return new_automated_results)

class QATester():
    """
    The object get a potential new building block and it's name and tests wheather is equivalent for replace
    Consider check excuation times as well (solo run only?)
    Consider also doing the replacement if validation is ok - if so - leave testing results as documentatio
    """
    def __init__(self, new_building_block_name, new_building_block, module):
        """
        Inital input:
        
        new_building_block_name - string
        name of the building block submitted for testing
        name must match one of the keys of BuildingBlockFunctions.FUNCTION_DICT

        new_building_block - function(instance)
        the actual function submitted for testing
        """
        self.new_building_block_name=new_building_block_name
        self.new_building_block=new_building_block
        self.module=module
##        self.function_dict=get_module_function_dict(module)
        
        self.old_building_block_name=get_building_block_name(new_building_block_name)
        self.old_building_block=get_building_block(new_building_block_name, module)
        
        
 
##        BuildingBlockFunctions.FUNCTION_USE_DICT.value.update({self.new_building_block_name:self.new_building_block})

                    
##        ValidationData.DATA_DICT.value.update({self.new_building_block_name:self.new_building_block.__code__.co_varnames})
##        ValidationData.DATA_DICT.value.update({self.old_building_block_name:self.old_building_block.__code__.co_varnames})
        
        
        
    def test_building_block(self,validation_data):
        """
        The method tests the building block both individually and as part of the automation cycles it intends to replace.
        """
        test_results=[] #[True, False, ..] for every QA test ran
        test_results.append(check_building_block_solely(self.new_building_block_name, self.new_building_block, validation_data, self.module))
##        for automation_cycle in AutomationCycles:
##            for single_block in automation_cycle.value:
##                if BuildingBlockFunctions.FUNCTION_DICT.value.get(self.new_building_block_name) == single_block:
##                    test_results.append(check_building_block_integration(module,self.new_building_block_name, automation_cycle.value, validation_data))
        return all(test_results)

def test_function_2(x,y):
    return x*y
def test_function_1(x):
    return x+5
    
if __name__=='__main__':
    new_building_block_name='angle'
    def calc_angle(r_ij, r_kj):
        from scipy.spatial.distance import cosine
##        r_ij = xyzarr[i] - xyzarr[j]
##        r_kj = xyzarr[k] - xyzarr[j]
        cosine_theta = cosine(r_ij,r_kj)
        theta = np.arccos(1-cosine_theta)
        return 	theta

    i_x_y_z=np.array([0, 0, 0.39263333])
    j_x_y_z=np.array([0, 0.75545, -0.19631667])
    k_x_y_z=np.array([0, -0.75545, -0.19631667])
    r_ij=i_x_y_z-j_x_y_z
    r_kj=k_x_y_z-j_x_y_z
    validation_data=(r_ij, r_kj)
    validation_result=37.94003

    import sys
    folder_path=r'C:\Users\\itaro\OneDrive\Documents\GitHub\learning_python\project\main_python.'
    sys.path.insert(0, folder_path)
    import translated_r_to_python as base_module
    function_module=base_module

    qa_tester=QATester(new_building_block_name=new_building_block_name,
                       new_building_block=calc_angle, #test_function_1
                       module=base_module,
                       )
    print(get_module_function_dict(base_module).keys())
##    print(qa_tester.test_building_block(validation_data))


##    validation_data_1=((2,-2),(4,5))
##    validation_data_2=(4,2)
##    validation_data_3=(2)

##    print(qa_tester.test_building_block(comp_set,(2,3)))






 



