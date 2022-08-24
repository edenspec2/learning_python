from enum import Enum
import numpy as np
import dis

import comp_set

import sys
folder_path=r'C:\Users\\itaro\OneDrive\Documents\GitHub\learning_python\project\main_python.'
sys.path.insert(0, folder_path)
import translated_r_to_python as base_module

def get_function_inner_calls(function):
    used_functions={}
    bytecode=dis.Bytecode(function)
    instrs=list(reversed([instr for instr in bytecode]))
    for ix, instr in enumerate(instrs):
        if instr.opname=='CALL_FUNCTION':
            long_func_instr=instrs[ix+instr.arg+1]
            used_functions.update({long_func_instr.argval: ix})
    return used_functions

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

def get_module_function_inner_calls(module):
    function_module_dict=get_module_function_dict(module)
    function_inner_calls={}
    for function_name, actual_function in function_module_dict.items():
        inner_calls=get_function_inner_calls(actual_function)
        if len(inner_calls)>0:
            function_inner_calls.update({function_name: inner_calls})
    return function_inner_calls

def reverse_nested_dictionaries(nested_dict):
    from collections import defaultdict
    flipped=defaultdict(dict)
    for key, val in nested_dict.items():
        for subkey, subval in val.items():
            flipped[subkey][key]=subval
    return dict(flipped)

def get_module_function_outer_calls(module):
    function_inner_calls=get_module_function_inner_calls(module)
    function_outer_calls={}
    reversed_function_inner_calls=reverse_nested_dictionaries(function_inner_calls)
    for key, val in reversed_function_inner_calls.items():
        if isinstance(val, int):
            continue
        if isinstance(val, dict):
            if key!=1:
                function_outer_calls.update({key: list(val.keys())})
    return function_outer_calls
        
class ValidationData(Enum):
    """
    Holds validation referral dictionary, where every key is the name of the function, and the value is the input data to validate the function works well
    """
    DATA_DICT={'coordination_transformation': [],
               'get_norm': [],
               'get_npa_dipole': [],} 

def get_building_block(building_block_name='function_name', module=None):
    """
    The function gets a building block name and returns the corresponding old building block actual function 
    """
    function_dict=get_module_function_dict(module)
    actual_building_block=function_dict.get(building_block_name)
    return actual_building_block

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
    old_building_block=get_building_block(new_building_block_name, module)
    if check_input_validity(old_building_block,(validation_data)):
        if check_input_validity(new_building_block,(validation_data)):
            return compare_output_results(old_building_block(*validation_data), new_building_block(*validation_data))
    else:
        return False

###Assumption - Output -> Input in automation cycles
##def run_automation_cycle(module, automation_cycle, validation_data):
##    """
##    goes trough every function in the automation_cycle, where the output of the first function is
##    the output of the next function and so on..
##    """
##    function_dict=get_module_function_dict(module)
##    first_function=function_dict.get(automation_cycle[0])
##    mid_results=first_function(*validation_data)
##    for function_name in automation_cycle[1:]:
##        actual_function=function_dict.get(function_name)
##        mid_results=actual_function(mid_results)
##    return mid_results

def check_building_block_integration(module, new_building_block_name, automation_cycle,validation_data): 
    """
    The function get a building block, it's name and the automation cycle wanted for testing.
    The function will run the automation cycle as is and with the new building block - and checks whether the results are identical.
    The function will return True if the operation is identical and False otherwise
    use dictionary of new and old names to change between the 
    """
    automated_results=run_automation_cycle(module, automation_cycle,validation_data)
    return automated_results

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
        self.original_building_block_code=get_building_block(self.new_building_block_name, self.module).__code__
##        self.function_dict=get_module_function_dict(module)
        
##        self.old_building_block_name=get_building_block_name(new_building_block_name)
##        self.old_building_block=get_building_block(new_building_block_name, module)
        
        
 
##        BuildingBlockFunctions.FUNCTION_USE_DICT.value.update({self.new_building_block_name:self.new_building_block})

                    
##        ValidationData.DATA_DICT.value.update({self.new_building_block_name:self.new_building_block.__code__.co_varnames})
##        ValidationData.DATA_DICT.value.update({self.old_building_block_name:self.old_building_block.__code__.co_varnames})
        
    def switch_building_block_code(self):
        get_building_block(self.new_building_block_name, self.module).__code__=self.new_building_block.__code__

    def revert_building_block_code(self):
        get_building_block(self.new_building_block_name, self.module).__code__=self.original_building_block_code        
        
    def test_building_block(self,validation_data):
        """
        The method tests the building block both individually and as part of the automation cycles it intends to replace.
        """
        test_results=[] #[True, False, ..] for every QA test ran
        test_results.append(check_building_block_solely(self.new_building_block_name, self.new_building_block, validation_data, self.module)) #test_soley
        if test_results[0]==False:
            print('function failed single operation')
            return False
        self.switch_building_block_code() #Temp switch the old function with the new funtion
        for module in CustomModules.INNERMODULES.value:
            outer_calls=get_module_function_outer_calls(module)
            print(outer_calls)        
        self.revert_building_block_code() #After testing - revert into the old function
        

            #test keys if values contains the new function name
            
##        for automation_cycle in AutomationCycles:
##            for single_block in automation_cycle.value:
##                if BuildingBlockFunctions.FUNCTION_DICT.value.get(self.new_building_block_name) == single_block:
##                    test_results.append(check_building_block_integration(module,self.new_building_block_name, automation_cycle.value, validation_data))
        return all(test_results)

def test_function_3(x):
    return x+6
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
    validation_result=0.66217


    function_module=base_module
    function_module_dict=get_module_function_dict(base_module)
    qa_tester=QATester(new_building_block_name=new_building_block_name,
                       new_building_block=calc_angle, #test_function_1
                       module=base_module,
                       )

    print(qa_tester.test_building_block(validation_data))


##    validation_data_1=((2,-2),(4,5))
##    validation_data_2=(4,2)
##    validation_data_3=(2)

##    print(qa_tester.test_building_block(comp_set,(2,3)))






 



