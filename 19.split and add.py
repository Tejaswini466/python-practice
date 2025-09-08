def split_and_add(arr, k):
  if k <= 0 or k >= len(arr):
    return arr  
  first_part = arr[:k]
  second_part = arr[k:]
  result = second_part + first_part
  return result
arr = [1, 2, 3, 4, 5]
k = int(input("Split and add from: "))
result = split_and_add(arr, k)
print("Original Array:", arr)
print("Array after splitting and adding:", result)