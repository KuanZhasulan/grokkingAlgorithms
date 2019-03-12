def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if(arr[i] < smallest):
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr

print selectionSort([1, 8, 9, 4, 3, 5, 7, 8, 9, 6, 5, 7])
#output - [1, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9]
