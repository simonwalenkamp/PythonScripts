for i in range(101):
    if(i % 5 == -i % 5 and i % 3 == -i % 3 and i != 0):
        print("FizzBuzz")

    elif(i % 3 == -i % 3 and i != 0):
        print("Fizz")

    elif(i % 5 == -i % 5 and i != 0):
        print("Buzz")

    else:
        print(str(i))
