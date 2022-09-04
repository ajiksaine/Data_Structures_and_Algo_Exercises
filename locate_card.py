from binary_search import Binary_Search
from test import Tests
from test_cases import TestCases

def locate_card(cards,query):
    
    def condition(mid):

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


    return Binary_Search.search(0,len(cards)-1,condition)

def main():
    
    tests = TestCases.test_cases()
    solution = Tests.evaluate_test_cases(locate_card,tests)
    
    for result in solution:
        print('expected_output: ',result['expected_output'])
        print('return_val: ',result['return_val'])
        print('pass: ',result['pass'])
        print('excecution time: ',result['excecution_time'])
        print(' ')


if __name__ == "__main__":
    main()