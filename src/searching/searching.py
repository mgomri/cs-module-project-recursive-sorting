def binary_search(arr, target, start, end):
  mid = (start + end) // 2 
  if start > end:
      return -1

  if target == arr[mid]:
    return mid
  elif target < arr[mid]:
    end = mid - 1
  else:
    start = mid + 1
    
  return binary_search(arr, target, start, end)
        


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

