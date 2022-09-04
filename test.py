import time

class Tests:
    def evaluate_test_cases(my_function,test_cases):
    
        test_results = []
        
        for test_case in test_cases:
            start = time.time()
            if len(test_case['input'])-1 <= 0:
                result = my_function(test_case['input']['num'])
            else:
                result = my_function(**test_case['input'])
            end = time.time()

            test_outcome = {
                'input': test_case['input'],
                'expected_output' : test_case['output'],
                'return_val': result,
                'pass' : result ==test_case['output'],
                'excecution_time': str((end-start) * 10**3) + ' ms'
            }
            test_results.append(test_outcome)
        
        return test_results