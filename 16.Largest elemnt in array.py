def find_largest(arr):
  if not arr:
    return "Array is empty"

  largest = arr[0]
  for element in arr:
    if element > largest:
      largest = element
  return largest

array = [10, 20, 30, 99]
result = find_largest(array)
print(f"The largest element in the array is: {result}")