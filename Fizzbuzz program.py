# Fizzbuzz program
# if a number is divisable by 3, print out "Fizz"
# if a number is divisable by 5, print out "Buzz"
# if a number is divisable by 3 and 5, print out "FizzBuzz"
for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    else:
        print(str(fizzbuzz))