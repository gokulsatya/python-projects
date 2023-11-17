def double_char(s):
    return ''.join([char * 2 for char in s])

# Example usage:
print(double_char('The'))  # Output: 'TThhee'
print(double_char('Hi-There'))  # Output: 'HHii--TThheerree'