def array_stats(arr):
    # Initialize variables to calculate max, min, sum, and count
    max_val = arr[0]
    min_val = arr[0]
    array_sum = 0
    count = 0

    # Calculate max, min, sum, and count
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
        array_sum = array_sum + num
        count = count + 1

    # Calculate average
    average = array_sum / count

    # Calculate range
    array_range = max_val - min_val

    # Return the results as a list
    return [max_val, min_val, average, array_sum, array_range]

input_array = [1, 2, 3, 4, 5]
result = array_stats(input_array)
print(result)
