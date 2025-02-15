# Implementation of linear search algorithm 
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

if __name__ == "__main__": # Driver code
    arr = [2, 4, 6, 8, 10] # Input array
    target = 6
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")