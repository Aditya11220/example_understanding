class Calculator:

    @staticmethod
    def add(a,b):
        return a +b
    
    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def calculator(a, b):
        if "+":
            return Calculator.add(a,b)
        elif "-":
            return Calculator.sub(a,b)
           
def main(a,b):
    sum_result = Calculator.calculator(a,b)
    return sum_result
        
if __name__ == "__main__":
    a = 10
    b = 5
    print(main(a,b))