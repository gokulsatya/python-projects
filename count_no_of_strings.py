def count_strings(lst):
    count = 0
    for string in lst:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# example usage
lst = ['level', 'hello', 'noon', 'world', 'pop']
print(count_strings(lst)) # output: 3
