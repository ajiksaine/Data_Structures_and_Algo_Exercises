import sys
import math
from contextlib import redirect_stdout

def binary_search(arr, low, high, sm):
    
    if high >= low:
 
        mid = (high + low) // 2

        val = arr[mid] 

        if sm == 0:
            sm = val
        if abs(val) < abs(sm):
            sm = val 
            if val > 0:
                return binary_search(arr, low, mid - 1, sm) 
            else:
                return binary_search(arr, mid + 1, high, sm)

        elif abs(val) == abs(sm):
                
            if val > 0:
                sm = val 
                return binary_search(arr, low, mid - 1, sm) 
            else:
                return binary_search(arr, mid + 1, high, sm)
        else:
            if val > 0:
                return binary_search(arr, low, mid - 1, sm) 
            else:
                return binary_search(arr, mid + 1, high, sm)
    # elif high == low:
    #      return  sm
    else:
        return sm

def compute_closest_to_zero(ts):
    mylist = sorted(ts)
    print(mylist)
    return binary_search(mylist,0,len(mylist)-1,0)


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    # n = int(input())
    # ts = [int(i) for i in input().split()]
    ts=[-4,-1,-15,-2,1,-8,7,9]
    # with redirect_stdout(sys.stderr):
    solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()