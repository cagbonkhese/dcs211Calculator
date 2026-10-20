#Updated through github
def mySum(a, b):
    return a+b

def mul(a, b):
    return a*b

def main():
    x = int(input("Enter the value of first number: "))
    y = int(input("Enter the value of second number: "))
    sumResult = mySum(x, y)
    mulResult = mul(x, y)
    print(f"the sum of {x} and {y} is: {sumResult}")
    print(f"the product of {x} and {y} is: {mulResult}")

main()
