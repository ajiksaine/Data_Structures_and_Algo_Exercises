from binary_search import Binary_Search
from test import Tests
from test_cases import TestCases

def first_positions(cards,query):
    
    def condition(mid):

        mid_num = cards[mid]     

        if mid_num == query:
            if mid > 0 and cards[mid -1] == query:
                return 'left'
            return 'found'
        elif mid_num < query:
            return 'right'
        else:
            return 'left'

    return Binary_Search.search(0,len(cards)-1,condition)

def last_positions(cards,query):
    
    def condition(mid):

        mid_num = cards[mid]     

        if mid_num == query:
            if mid < len(cards) -1 and cards[mid + 1] == query:
                return 'right'
            else:
                return 'found'

        elif mid_num < query:
                return 'right'
        else:
                return 'left'

    return Binary_Search.search(0,len(cards)-1,condition)

def first_and_last_position(cards,query):
    return first_positions(cards,query),last_positions(cards,query)

def main():
    
    tests = TestCases.first_last_postion_test_cases()
    solution = Tests.evaluate_test_cases(first_and_last_position,tests)
    
    for result in solution:
        print('expected_output: ',result['expected_output'])
        print('return_val: ',result['return_val'])
        print('pass: ',result['pass'])
        print('excecution time: ',result['excecution_time'])
        print(' ')


if __name__ == "__main__":
    main()