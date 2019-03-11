def binary_search(item, list):
  #low and high set the search range
  low = 0  
  high = len(list) - 1
  while low<= high:
    mid = (low+high)/2
    guess = list[mid]
    if item == guess:
      return mid
    if guess > item:
      high = mid -1
    else:
      low = mid + 1

  return None

my_list = [1, 2, 4, 5, 6, 7, 8, 9, 11, 15, 17, 21, 23, 25]
print binary_search(7, my_list)  
print binary_search(-6, my_list)
