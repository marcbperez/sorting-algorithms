class Stack(list):
    ''' creating stack '''
    push = list.append

def quicksort(array):
    """
    Iterative quicksort implementation

    :param items: array 
    :type items: list
    :return: sorted array of items
    :rtype: list 
    """
    n = len(array)
    if n < 2:
        return array
    stack = Stack([(0, n - 1)])
    while stack:
        elem_idx, pivot_idx = low, high = stack.pop()
        elem = array[elem_idx]
        pivot = array[pivot_idx]
        while pivot_idx > elem_idx:
            if elem > pivot:
                array[pivot_idx] = elem
                pivot_idx -= 1
                array[elem_idx] = elem = array[pivot_idx]
            else:
                elem_idx += 1
                elem = array[elem_idx]
        array[pivot_idx] = pivot

        lsize = pivot_idx - low
        hsize = high - pivot_idx
        if lsize <= hsize:
            if 1 < lsize:
                stack.push((pivot_idx + 1, high))
                stack.push((low, pivot_idx - 1))
        else:
            stack.push((low, pivot_idx - 1))
        if 1 < hsize:
            stack.push((pivot_idx + 1, high))
    return array
