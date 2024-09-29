""" print("2 * 1 = 2")
print("2 * 2 = 4")
print("2 * 3 = 6")
print("2 * 4 = 8")
print("2 * 5 = 10")
print("2 * 6 = 12")
print("2 * 7 = 14")
print("2 * 8 = 16")
print("2 * 9 = 18")
print("2 * 10 = 20") """

def print_table(num, t_range):
    for i in range(1, t_range + 1):
        print(f"{num} * {i} = {i*num}")

print_table(7,10)

def multiply(num1, num2) -> int:
    return num1*num2