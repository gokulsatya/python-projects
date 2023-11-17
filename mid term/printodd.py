#name==Gokul_Sathiyamurthy
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # list of numbers
result = []                           # empty list to store result

for num in lst:                       # iterate over the list
    if num % 2 != 0 and num !=1:      # check if the number is odd & not equal to 1 as per the expected output
        result.append(num)            # append to the result list

print(result)                         # print the result
