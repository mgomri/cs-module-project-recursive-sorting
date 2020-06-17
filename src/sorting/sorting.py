# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    minA = 0
    minB = 0
    i = 0
    while minA < len(arrA) and minB < len(arrB):
        if arrA[minA] <= arrB[minB]:
            merged_arr[i] = arrA[minA]
            minA += 1
        else:
            merged_arr[i] = arrB[minB]
            minB +=1
        i += 1

    if minA == len(arrA):
        while minB < len(arrB):
            merged_arr[i] = arrB[minB]
            minB += 1
    
    elif minB == len(arrB):
        while minA < len(arrA):
            merged_arr[i] = arrA[minA]
            minA += 1
            i += 1
            
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

