def find_maximum(arr):
    if not arr:
        return None                                                
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

i = [1, 2, 3, 4, 5]
result = find_maximum(i)
print("maximum value :", result)
