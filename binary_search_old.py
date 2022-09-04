

class Binary_Search:

    def test_location(array,query,mid):

        mid_num = array[mid]     

        if mid_num == query:
            if mid -1 >=0 and array[mid -1] == query:
                return 'left'
            else:
                return 'found'
        elif mid_num < query:
                return 'left'
        else:
                return 'right'

    def search(array,low,high,condition):

        while low <= high:

            mid = (low + high) // 2

            result = Binary_Search.test_location(array,condition,mid)
            
            if result == 'found':
                return mid
            elif result == 'left':
                high = mid - 1
            elif result == 'right':
                low = mid + 1
        return -1

