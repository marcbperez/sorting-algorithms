"""

From MIT OpenCourseWare, available at:

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/
6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
lecture-slides-code/MIT6_0001F16_Lec12.pdf

"""


def merge(left, right):
    """Merges an integer list that has two sorted sublists."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        # Left and right sublists are ordered, move indices for sublists depending on
        # which sublist holds next smallest element.
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        # When right sublist is empty.
        result.append(left[i])
        i += 1
    while j < len(right):
        # When left sublist is empty.
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):
    """Takes in an integer list and merge-sorts it."""
    if len(L) < 2:
        # Base case.
        return L[:]
    else:
        # Divide...
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        # and conquer with the merge step.
        return merge(left, right)


"""

Usage example:
Creating a random unsigned integer list and merge-sorting it.

"""


from random import seed
from random import shuffle


# Create a list of signed integers.
integers = [i for i in range(-20, 21)]
# Randomly shuffle the list.
seed(1)
shuffle(integers)
# Show the randomly shuffled list.
print "Unsorted list:"
print integers
# Merge-sort and show the list.
print "Sorted list:"
print merge_sort(integers)
