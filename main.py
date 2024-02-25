from playsound import playsound

def FizzBuzzMethod(num):
        if num % 3 ==0:
            print("Fizz")
        if num % 5 ==0:
            print("Buzz")
        if num % 5 and num % 3==0:
            print("FizzBuzz")
i = 1
while i<100:
    FizzBuzzMethod(i)
    i+=1

