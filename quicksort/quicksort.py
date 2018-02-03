def partition(array,first,last):
  pivotvalue = array[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      while leftmark <= rightmark and array[leftmark] <= pivotvalue:
          leftmark = leftmark + 1

      while array[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1

      if rightmark < leftmark:
          done = True
      else:
          temp = array[leftmark]
          array[leftmark] = array[rightmark]
          array[rightmark] = temp

  temp = array[first]
  array[first] = array[rightmark]
  array[rightmark] = temp

  return rightmark

def quickSortHelper(array,first,last):
  if first<last:
      splitpoint = partition(array,first,last)
      quickSortHelper(array,first,splitpoint-1)
      quickSortHelper(array,splitpoint+1,last)

def quickSort(array):
  quickSortHelper(array,0,len(array)-1)
  
array=[1,9,2,3,10,38,3,0,4]
quickSort(array)
print(array)
#[0, 1, 2, 3, 3, 4, 9, 10, 38]
