from enum import Enum

def function_1(x):
    return x**2

def function_2(x):
    return x+2

def check_input_validity(my_function, function_input):
    try:
        value=my_function(function_input)
        return True
    except TypeError:
        return False

class QAConstants(Enum):
    TEST_INPUT=[5.0, 6, 'A']
    UNVALID_INPUT_FLAG='Not Valid'
    

class QATester():
    """
    An object aimed at comparing two funtions or objects proper excution and output
    the objective is to test a new funcion that suppose to give the same results as the original and identify bugs if it doesnt
    """
    
    def __init__(self, original_function):
        self.original_function=original_function
            
    def verify_input_format(self, test_function, test_input):
        return check_input_validity(self.original_function, test_input)==check_input_validity(test_function, test_input)

    def verify_single_function_run(self, test_function, test_input):
        return self.original_function(test_input)==test_function(test_input)

    def verify_single_file_run(self):
        pass

    def verify_multi_file_run(self):
        pass

    def verify_output(self):
        pass

    def run_single_evaluation(self, test_function, test_input):
        if check_input_validity(self.original_function, test_input):
            return self.verify_input_format(test_function, test_input) and self.verify_single_function_run(test_function, test_input)
        else:
            return QAConstants.UNVALID_INPUT_FLAG.value

    def run_full_evaluation(self, test_function, test_inputs):
        evaluation_results=[]
        for input_value in test_inputs:
            test_result=self.run_single_evaluation(test_function, test_input=input_value)
            if test_result==True or test_result==QAConstants.UNVALID_INPUT_FLAG.value:
                evaluation_results.append(True)
            else:
                evaluation_results.append(False)
        return evaluation_results
                
                          
if __name__=='__main__':
    qa_tester=QATester(function_1)
    self_qa_results=qa_tester.run_full_evaluation(function_1, test_inputs=QAConstants.TEST_INPUT.value)
    external_qa_results=qa_tester.run_full_evaluation(function_2, test_inputs=QAConstants.TEST_INPUT.value)
    print('expecting True: ', self_qa_results)
    print('expecting False: ', external_qa_results)
    
    
