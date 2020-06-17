# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a_point = 0
    b_point = 0

    for i in range(len(merged_arr)):
        if a_point == len(arrA):
            merged_arr[i] = arrB[b_point]
            b_point += 1

        elif b_point == len(arrB):
            merged_arr[i] = arrA[a_point]
            a_point += 1

        else:
            if arrA[a_point] > arrB[b_point]:
                merged_arr[i] = arrB[b_point]
                b_point += 1
            else:
                merged_arr[i] = arrA[a_point]
                a_point += 1        

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        splitter = len(arr) // 2

        arr1 = merge_sort(arr[:splitter])
        arr2 = merge_sort(arr[splitter:])
        return merge(arr1, arr2)    


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
