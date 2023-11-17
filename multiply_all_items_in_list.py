def multiply_list(lst):
    """
    This function takes a list as input and returns the product of all the elements in the list.
    """
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage
my_list = [1, 2, 3, 4, 5]
print(multiply_list(my_list)) # Output: 120
