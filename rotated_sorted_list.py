from turtle import right
from binary_search import Binary_Search
from test import Tests
from test_cases import TestCases

def linear_search(numbers):
    position = 0
    smallest = 0

    while position <= len(numbers)-1:
        if numbers[smallest] > numbers[position]:
            smallest = position

        if position == len(numbers)-1:
            return smallest
        
        position += 1
    return -1

def count_rotation_brutforce(numbers):
     
     position = linear_search(numbers)

     return position

def search_smallest(numbers):
    def condition(mid,):
        mid_num = numbers[mid]

        if  numbers[mid -1] < numbers[mid] :
            return 'left'
        elif numbers[mid -1] > numbers[mid] :
            return 'found'
        else:
            return 'right'

    return Binary_Search.search(0,len(numbers)-1,condition)

def count_rotation(numbers):

    return search_smallest(numbers)

def main():
    
    tests = TestCases.rotated_sorted_list_test_cases()
    solution = Tests.evaluate_test_cases(count_rotation,tests)
    
    for result in solution:
        print('expected_output: ',result['expected_output'])
        print('return_val: ',result['return_val'])
        print('pass: ',result['pass'])
        print('excecution time: ',result['excecution_time'])
        print(' ')


if __name__ == "__main__":
    main()