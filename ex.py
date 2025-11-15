def add(a,b):
    return a +b

def sub(a,b):
    return a - b


def main(a, b,op):
    if op == "+":

        output = add(a,b)
        return output
    if op == "-":
        output = sub(a,b)
        return output
    
    if op == "*":
        output = a * b
        return output
    
    if op == "/":
        output = a / b
        return output
    else: 
        return "Invalid operation"
    
if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    print(main(a,b,op))