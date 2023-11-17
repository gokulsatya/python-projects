def add_ing_ly(s):
    if s.endswith("ing"):
        return s + "ly"
    else:
        return s + "ing"
input_string = "read"
result = add_ing_ly(input_string)
print(result) 
input_string = "swimming"
result = add_ing_ly(input_string)
print(result) 
