def answer_questions(questions_string):
    a = "write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the maximum value in the array. do not use the built-in max function\n"
    b = "write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the minimum value in the array. do not use the built-in min function\n."
    c = "write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the average value in the array. do not use the built-in average function\n"
    d = "write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the sum of all values of the array. do not use any built-in summing functions\n"
    e = "write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the range of the array (distance between the maximum and minimum values\n"

    return [a, b, c, d, e]

# Example usage:
questions = "1. write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the maximum value in the array. do not use the built-in max function\n2. write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the minimum value in the array. do not use the built-in min function\n3. write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the average value in the array. do not use the built-in average function\n4. write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the sum of all values of the array. do not use any built-in summing functions.\n5. write function that accepts an array of numbers (i=[1,2,3,4,5]) and returns the range of the array (distance between the maximum and minimum values"

answers = answer_questions(questions)
print(answers)
