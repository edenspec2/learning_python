from enum import Enum
import numpy as np
import dis
import time

import translated_r_to_python as base_module

class CustomModules(Enum):
    INNERMODULES=[base_module,]

class ValidationData(Enum):
    """
    Holds validation referral dictionary, where every key is the name of the function, and the value is the input data to validate the function works well
    """
    DATA_DICT={'coordination_transformation': (),
               'get_angles_df_from_csv': (),
               'get_norm': (),
               'get_npa_dipole': (),
               'get_angle': (np.array([0, -0.75545, 0.58895]), np.array([ 0, -1.5109, 0]), ), #0.66217
               } 

def get_validation_data(building_block_name):
    return ValidationData.DATA_DICT.value.get(building_block_name)

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
    function_dict=dict(getmembers(module, isfunction)) 
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
        
def get_building_block(building_block_name='function_name', module=None):
    """
    The function gets a building block name and returns the corresponding building block function 
    """
    function_dict=get_module_function_dict(module)
    building_block=function_dict.get(building_block_name)
    return building_block

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

def get_building_block_output_and_duration(building_block, validation_data, time_loop_number=100):
    if not check_input_validity(building_block, validation_data):
        return 0, 0
    start_time=time.time()
    for _ in range(time_loop_number):
        output=building_block(*validation_data)
    stop_time=time.time()
    avg_run_time=(stop_time-start_time)/time_loop_number
    return output, avg_run_time

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
            
def check_building_block_solely(building_block_1, building_block_2, validation_data=None):
    """
    The function a new building block and validation data, and checks whether the operation of the new building block
    is identical to the old building block it suppose to replace.
    The function will return True if the operation is identical and False otherwise
    """
    output_1, output_1_time=get_building_block_output_and_duration(building_block_1, validation_data)
    output_2, output_2_time=get_building_block_output_and_duration(building_block_2, validation_data)
    return compare_output_results(output_1, output_2)

def git_push(git_repo_path, commit_message):
    from git import Repo
    try:
        repo=Repo(git_repo_path) #local path
        repo.git.add(update=True)
        repo.index.commit(commit_message)
        origin=repo.remote(name='origin') # name?
        origin.push()
    except:
        print('Error pushing to github')

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

##def check_building_block_integration(module, new_building_block_name, automation_cycle,validation_data): 
##    """
##    The function get a building block, it's name and the automation cycle wanted for testing.
##    The function will run the automation cycle as is and with the new building block - and checks whether the results are identical.
##    The function will return True if the operation is identical and False otherwise
##    use dictionary of new and old names to change between the 
##    """
##    automated_results=run_automation_cycle(module, automation_cycle,validation_data)
##    return automated_results

class QATester():
    """
    The object get a potential new building block and it's name and tests wheather is equivalent for replace
    Consider check excuation times as well (solo run only?)
    Consider also doing the replacement if validation is ok - if so - leave testing results as documentation
    """
    def __init__(self, new_building_block, module):
        """
        Inital input:
        
        new_building_block_name - string
        name of the building block submitted for testing
        name must match one of the keys of BuildingBlockFunctions.FUNCTION_DICT

        new_building_block - function(instance)
        the actual function submitted for testing
        """
        self.new_building_block_name=new_building_block.__name__
        self.new_building_block=new_building_block
        self.module=module
        self.original_building_block=get_building_block(self.new_building_block_name, module)
        self.original_building_block_code=get_building_block(self.new_building_block_name, module).__code__
        
    def switch_building_block_code(self):
        get_building_block(self.new_building_block_name, self.module).__code__=self.new_building_block.__code__

    def revert_building_block_code(self):
        get_building_block(self.new_building_block_name, self.module).__code__=self.original_building_block_code        

    def test_parent_building_block(self, building_block_name):
        validation_data=get_validation_data(self.new_building_block_name)
        building_block=get_building_block(building_block_name, self.module)
        original_output, original_output_time=get_building_block_output_and_duration(building_block, validation_data)
        self.switch_building_block_code() #Temp switch the old function with the new funtion
        switched_output, switched_output_time=get_building_block_output_and_duration(building_block, validation_data)        
        self.revert_building_block_code() #After testing - revert into the old function
        return compare_output_results(original_output, switched_output)

    def test_building_block(self):
        """
        The method tests the building block both individually and as part of the automation cycles it intends to replace.
        """
        validation_data=get_validation_data(self.new_building_block_name)
        test_results=[] #[True, False, ..] for every QA test ran
        test_results.append(check_building_block_solely(self.original_building_block, self.new_building_block, validation_data)) #test_soley 
        if test_results[0]==False:
            print('function failed solo operation - fix function to match the output of the original function')
            return False

        for module in CustomModules.INNERMODULES.value:
            outer_calls=get_module_function_outer_calls(module)
            possible_parent_building_blocks=outer_calls.get(self.new_building_block_name)
            if possible_parent_building_blocks:
                for parent_building_block_name in possible_parent_building_blocks:
                    print(parent_building_block_name)
##                    test_results.append(self.test_parent_building_block(parent_building_block_name))               
        return all(test_results)

    
if __name__=='__main__':
    # filename='test_dipole'
    path=r"GitHub\learning_python\project\main_python\test_dipole"
    df=base_module.get_angles_df_from_csv([2,3,4])
    print(df)
    # dir with moledir -> in every dir there csv file of the xyz coord -> 'xyz_molecule_1.csv' -> return angles df
    # def get_angle(p1, p2):
    #     from scipy.spatial.distance import cosine
    #     cosine_theta=cosine(p1, p2)
    #     theta=np.arccos(1-cosine_theta)
    #     return 	theta

    # qa_tester=QATester(new_building_block=get_angle,
    #                   module=base_module,
    #                   )
    # print(qa_tester.test_building_block())







 



