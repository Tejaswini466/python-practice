def reverse_array(arr):
    n = len(arr)
    reversed_arr = [0] * n
    for i in range(n):
        reversed_arr[i] = arr[n-1-i]
    return reversed_arr

arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)
print("Reversed Array:", reverse_array(arr))
