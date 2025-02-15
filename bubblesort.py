#Function to implement bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n): # Traverse through all elements in the array
        for j in range(0, n-i-1): # Last i elements are already sorted
            if arr[j] > arr[j+1]: # Swap if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90] # Input array
    sorted_arr = bubble_sort(arr) 
    print("Sorted array is:", sorted_arr)