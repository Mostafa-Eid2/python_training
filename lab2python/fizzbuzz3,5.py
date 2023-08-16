def fizzbuzz(inputnum):
    if inputnum % 3 == 0 and inputnum % 5 == 0:
        print("FizzBuzz")
    elif inputnum % 5 == 0:
        print("Buzz")    
    elif inputnum % 3 == 0:
        print("Fizz")    
    else:
        print("please try again, No Fizzes or Buzzes")

inputnum = int(input("Enter the number: "))
fizzbuzz(inputnum)