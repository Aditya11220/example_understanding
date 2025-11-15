class Calculator:

    @staticmethod
    def add(a,b):
        ans= a+b
        return ans
    
    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def mul(a,b):
        return a * b
    
    @staticmethod
    def calculator(a, b):
        if "+":
            return Calculator.add(a,b)
        elif "-" :
            return Calculator.sub(a,b)
        elif "*":
            return Calculator.mul(a,b)
           
def main(a,b):
    sum_result = Calculator.add(a,b)
    mul_result = Calculator.mul(a,b)

    return sum_result
        
if __name__ == "__main__":
    a = 10
    b = 5
    print(main(a,b))