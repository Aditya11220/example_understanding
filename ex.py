def add(a,b):
    return a +b

def sub(a,b):
    return a - b


def main(a, b):
    if "+":

        output = add(a,b)
        return output
    if "-":
        output = sub(a,b)
        return output
    
    if "*":
        output = a * b
        return output
    
    if "/":
        output = a / b
        return output
    else: 
        return "Invalid operation"
    
if __name__ == "__main__":
    a = 10
    b = 5
    print(main(a,b))