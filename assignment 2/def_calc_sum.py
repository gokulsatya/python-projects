def calc_sum(arr):
    total = 0  
    for num in arr:
        total = total + num 
    return total

i = [1, 2, 3, 4, 5]
sum_value = calc_sum(i)
print(f"The sum of the array is: {sum_value}")
