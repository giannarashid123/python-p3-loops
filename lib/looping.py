# 1. Countdown from 10 to 1, then "Happy New Year!"
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

# 2. Return a new list with each integer squared
def square_integers(int_list):
    return [num ** 2 for num in int_list]

# 3. Print numbers 1 to 100 with FizzBuzz logic
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
