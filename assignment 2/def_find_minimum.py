def find_minimum(arr):
    if not arr:
        return None                                                
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

i = [1, 2, 3, 4, 5]
result = find_minimum(i)
print("minimum value :", result)
