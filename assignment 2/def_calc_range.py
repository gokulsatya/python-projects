def calc_range(arr):
    if not arr:
        return None  
    min_val = min(arr)
    max_val = max(arr)
    array_range = max_val - min_val
    return array_range
input_array = [1, 2, 3, 4, 5]
result = calc_range(input_array)
print("The range of the array:", result)
