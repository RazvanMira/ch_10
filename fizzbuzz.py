# fizz_buzz(5) -> 1 2 Fizz 4 Buzz
# if the number is divisible by 3 print Fizz
# if the number is divisible by 5 print Buzz
# if the number is divisible by 3 and 5 print FizzBuzz

def fizz_buzz(up_to: int):
    for i in range(1, up_to + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end= " ")
        elif i % 3 == 0:
            print("Fizz", end= " ")
        elif i % 5 == 0:
            print("Buzz", end= " ")
        else:
            print(i, end= " ")

fizz_buzz(25)

