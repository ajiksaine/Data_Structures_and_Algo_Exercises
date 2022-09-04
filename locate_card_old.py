import time

def locate_card_brutforce(cards,query):
    position = 0
    
    while True:
        
        if len(cards) <= 0:
            return -1
            
        if cards[position] == query:
            return position
                
        position += 1
            
        if position == len(cards):
            return -1

def binary_search(cards,query,high,low):
    
    if high >= low:
        
        mid = (high + low)//2
        
    
        if cards[mid] == query:
            return mid
        elif cards[mid] > query:
            return binary_search(cards,query,high, mid + 1)
        else:
            return binary_search(cards,query,mid -1, low)
            
            
    else:
        return -1 

def test_location(cards,query,mid):

    mid_num = cards[mid]     

    if mid_num == query:
        if mid -1 >=0 and cards[mid -1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_num < query:
            return 'left'
    else:
            return 'right'

def locate_card_recusive(cards,query):
    
    return binary_search(cards,query,len(cards)-1,0)

def locate_card(cards,query):
    
    low,high = 0, len(cards) -1

    while low <= high:

        mid = (low + high) // 2
        
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def locate_card_with_multiple_occurence(cards,query):
    
    low,high = 0, len(cards) -1

    while low <= high:

        mid = (low + high) // 2

        result = test_location(cards,query,mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
    return -1
    

def evaluate_test_case(my_function,test_cases):
    
    test_results = []
    
    for test_case in test_cases:
        start = time.time()
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
def test_cases():

    ts1= {
        'input':{
            'cards':[15, 13, 7,6,5,3,2,1],
            'query':5
        },
        'output': 4 
    }
    ts2= {
        'input':{
            'cards':[],
            'query':5
        },
        'output': -1 
    }
    ts3= {
        'input':{
            'cards':[15, 13, 7,6,5,5,5,5,5,5,2,1],
            'query':5
        },
        'output': 4 
    }

    ts4= {
        'input':{
            'cards':[20, 17, 15, 12, 9, 8, 7, 5, 1],
            'query':15
        },
        'output': 2 
    }

    ts5= {
        'input':{
            'cards':[20, 17, 15, 12, 9, 8, 7, 5, 1],
            'query':7
        },
        'output': 6 
    }

    large_testcase= {
        'input':{
            'cards':list(range(10000000,0,-1)),
            'query':2
        },
        'output': 9999998
    }
    
    tests = []
    
    tests.append(ts1)
    tests.append(ts2)
    tests.append(ts3)
    tests.append(ts4)
    tests.append(ts5)
    tests.append(large_testcase)

    return tests

def main():
    
    tests = test_cases()
    solution = evaluate_test_case(locate_card_with_multiple_occurence,tests)
    #solution = evaluate_test_case(locate_card_with_multiple_occurence,tests)
    
    for result in solution:
        print('expected_output: ',result['expected_output'])
        print('return_val: ',result['return_val'])
        print('pass: ',result['pass'])
        print('excecution time: ',result['excecution_time'])
        print(' ')


if __name__ == "__main__":
    main()