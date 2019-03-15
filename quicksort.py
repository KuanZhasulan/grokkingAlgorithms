def quicksort(arr):
  if len(arr)< 2:
    return arr
  else:
    point = arr[0]
    lesser =  [i for i in arr[1:] if i <= point]
    greater =  [i for i in arr[1:] if i > point]
    return quicksort(lesser) + [point] + quicksort(greater)


myArray = [1, 5, 8, 9, 10, 14, 54, 84, 23, 54, 12, 8, 9, 5, 4, 7, 5, 63, 54, 25, 29, 98, 87, 84, 51, 102, 36]
print quicksort(myArray)
