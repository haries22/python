def quick_sort(arr):
    if len(arr) <= 1:  
        return arr
    else:
        pivot = arr[len(arr) // 2]  
        less = [x for x in arr if x < pivot]  
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)

data = [29, 10, 14, 37, 13]
sorted_data = quick_sort(data)
print("Sebelum diurutkan:", data)
print("Setelah diurutkan:", sorted_data)
