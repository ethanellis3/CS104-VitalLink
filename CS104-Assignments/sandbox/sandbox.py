number = input("Enter an integer: ")

try:
    number = int(number)
    print("You entered the integer:", number)
except ValueError:
    print("You did not enter a valid integer.")
    exit()

print("Welcome to VitalLink! Let's get you signed up for our healthcare services.")
print()
name = input("Please enter your full name: ")
age = input("Please enter your age: ")
print()
print("Thank you for signing up! We have created a new record for " + name + ", age " + age + ".")
