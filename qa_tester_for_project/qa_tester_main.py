from enum import Enum

class BuildingBlockFunctions(Enum):
    """
    Holds a function referral dictionary, where every key is the name of function, and the value is the actual function
    """
    FUNCTION_DICT={'function_name': 'actual_function'}

class AutomationCycles(Enum):
    """
    Hold iterables of common automation cycles
    Automation cycle is defined as a sequence of functions that generally run togather
    """
    SET_COMP=()
    MODEL=()

class ValidationData(Enum):
    """
    Holds validation referral dictionary, where every key is the name of the function, and the value is the input data to validate the function works well
    """
    DATA_DICT={'function_name': 'validation_data'}
    
def get_old_building_block(building_block_name='function_name'):
    """
    The function gets a building block name and returns the corresponding function name
    """
    return BuildingBlockFunctions.FUNCTION_DICT.value.get(building_block_name)

## for use in check_building_block_solely
def check_input_validity(building_block, validation_data):
    try:
        value=building_block(validation_data)
        return True
    except TypeError:
         return False
    
def check_building_block_solely(building_block_1, building_block_2, validation_data=None):
    """
    The function get two building blocks and validation data, and checks whether the operation of the building blocks is identical on their own.
    The function will return True if the operation is identical and False otherwise
    """
    ## works with iter or single value
    try:
        iter(validation_data)
        test_results=[]
        for data in validation_data:
            if check_input_validity(building_block_1,data):
                if check_input_validity(building_block_2,data):
                    test_results.append(building_block_1(data)==building_block_2(data))
            else:
                test_results.append(False)
        return test_results
    except TypeError:
        if check_input_validity(building_block_1,validation_data):
                if check_input_validity(building_block_2,validation_data):
                    return (building_block_1(validation_data)==building_block_2(validation_data))
        else:
            return False
            
    # Check all validation data on building_block_1 -> if failed -> return False
    # Check all validation data on building_block_2 -> if failed -> return False
    # If the results from both run are identical -> return True

def check_building_block_integration(new_building_block_name, new_building_block, automation_cycle):
    """
    The function get a building block, it's name and the automation cycle wanted for testing.
    The function will run the automation cycle as is and with the new building block - and checks whether the results are identical.
    The function will return True if the operation is identical and False otherwise
    """
    # Since this runs will take time - consider saving the output of known cycles
    # Think of how to store the automation cycles validation data
    # Check the run with the new building block
    # If the results from both run are identical -> return True AND save the new output(?)
    return True

class QATester():
    """
    The object get a potential new building block and it's name and tests wheather is equivalent for replace
    Consider check excuation times as well (solo run only?)
    Consider also doing the replacement if validation is ok - if so - leave testing results as documentatio
    """
    def __init__(self, new_building_block_name, new_building_block):
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

        self.old_building_block=get_old_building_block(new_building_block_name)

    def test_building_block(self):
        """
        The method tests the building block both individually and as part of the automation cycles it intends to replace.
        """
        test_results=[] #[True, False, ..] for every QA test ran
        test_results.append(check_building_block_solely(self.new_building_block, self.old_building_block))
        for automation_cycle in AutomationCycles:
            if self.new_building_block_name in automation_cycle.value:
                test_results.append(check_building_block_integration(self.new_building_block_name, self.new_building_block, automation_cycle.value))
        return test_results

def test_function_1(x):
    return x**2

def test_function_2(x):
    return x+2 
    
if __name__=='__main__':
    new_building_block_name='function_name'
    building_block_1=test_function_1
    building_block_2=test_function_2
    qa_tester=QATester(new_building_block_name, building_block_1)
    print(qa_tester.test_building_block())
    print(qa_tester.old_building_block)
    print(check_building_block_solely(building_block_1,building_block_2,[2,4,'a']))
