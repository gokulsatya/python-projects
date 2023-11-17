#name==Gokul_Sathiyamurthy
def shortest_word(words):                 #defining the function of shortest word
    shortest = min(words, key=len)        #finding the shortest word
    return shortest, len(shortest)        #returning the shortest word and length of the shortest word

words = ['apple', 'banana', 'pen', 'orange']         #assigning the values to the words
shortest, length = shortest_word(words)              #calling the function of shortest word
print(f"Shortest word: {shortest}")                  #printing the shortest word
print(f"Length of the Shortest word: {length}")      #printing the length of the shortest word
