

class Binary_Search:

    def search(low,high,condition):

        while low <= high:

            mid = (low + high) // 2

            result = condition(mid)
            
            if result == 'found':
                return mid
            elif result == 'left':
                high = mid - 1
            else:
                low = mid + 1
        return -1

