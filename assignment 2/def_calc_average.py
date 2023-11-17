def calc_average(arr):
    if not arr:
        return None 
    total = 0 
    count = 0  
    for num in arr:
        total = total + num  
        count = count + 1   
    average = total / count 
    return average

i = [1, 2, 3, 4, 5]
average_value = calc_average(i)
print(f"The average value of the array is: {average_value}")
