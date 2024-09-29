#print("Please enter a value for Fahrenheit:")
x = input("Please enter a value for Fahrenheit:")
#Validation of the User Input
#print(type(x))
x = int(x) # Convert the str into int
#print(type(x))
print("The Centigrade Equivalent for the given Fahrenheit is: ", 5/9*(x-32))
print(f"{x}F = {5/9*(x-32)}C")
