# worst case time complexity is O(log(n))
# continuously finding the middle and checking if it is the target
# MUST BE A SORTED LIST!!!!

def binary_search(array, target):

    left = 0
    right = len(array)-1
    while left<right:
        mid = left + (right-left)//2
        val = array[mid]
        if val == target:
            return mid
        if val < target:
            left = mid + 1
        else:
            right = mid - 1


def binary_search_recursive(array, left, right, target):
    if left > right:
        return -1

    mid = left + (left+right)//2

    if target > array[mid]:
        return binary_search_recursive(array, mid + 1, right, target)
    if target < array[mid]:
        return binary_search_recursive(array, left, mid - 1, target)
    return mid