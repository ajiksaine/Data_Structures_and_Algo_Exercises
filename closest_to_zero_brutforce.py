import sys
import math
from contextlib import redirect_stdout



def compute_closest_to_zero(ts):
    if len(ts) -1 < 0:
        return 0

    sm = 0

    for  val in ts:
        print("val:  " + str(val) +  " sm: " + str(sm))
        if sm == 0:
            sm = val
        elif abs(val) < abs(sm):
            sm = val
        elif abs(val) == abs(sm):
            if val > 0:
                sm = val

    return sm


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    # n = int(input())
    # ts = [int(i) for i in input().split()]
    ts=[-4,-1,-15,-2,1,0,-8,7,9]
    # with redirect_stdout(sys.stderr):
    solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()