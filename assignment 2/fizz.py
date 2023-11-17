#Name==Gokul_Sathiyamurthy
for i in range(1, 31):               # 1 to 30
    if i % 3 == 0 and i % 5 == 0:    #multiple of 3 and 5
        print("FizzBuzz")            #print FizzBuzz
    elif i % 3 == 0:                 #multiple of 3
        print("Fizz")                #print Fizz
    elif i % 5 == 0:                 #multiple of 5
        print("Buzz")                #print Buzz
    else:                            #not multiple of 3 and 5
        print(i)                     #print i