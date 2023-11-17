def extra_end(s):
    last_two_chars = s[-2:]  # Get the last two characters of the string
    return last_two_chars * 3

# Example usage:
print(extra_end('Hello'))  # Output: 'lololo'
print(extra_end('ab'))  # Output: 'ababab'
print(extra_end('Hi'))  # Output: 'HiHiHi'
