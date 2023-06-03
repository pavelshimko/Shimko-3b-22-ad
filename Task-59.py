arr = ["apple", "orange", "banana", "pineapple", "grape"]

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if len(array[j]) < len(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

arr =bubble_sort(arr)
print(arr)