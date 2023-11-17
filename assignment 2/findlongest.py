def find_longest_word(words):
    longest_word = ""
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)
    return longest_word, longest_length

words = ["apple", "banana", "cherry", "exercises", "python"]
longest_word, length = find_longest_word(words)
print("Longest word:", longest_word)
print("Length of the longest word:", length)