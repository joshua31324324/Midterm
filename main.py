import sys
import pandas as pd
from calculator import Calculator
from decimal import Decimal, InvalidOperation

from calculator import App


history = pd.DataFrame(columns=["Operation", "Result"])

def add_to_history(operation, result):
    global history
    new_entry = pd.DataFrame({"Operation": [operation], "Result": [result]})
    history = pd.concat([history, new_entry], ignore_index=True)

def perform_calculation(expression):
    try:
        result = eval(expression)
        add_to_history(expression, result)
        return result
    except Exception as e:
        return f"Error: {e}"


def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    
    calculate_and_print(a, b, operation)
    if __name__ == "__main__":
        app = App().start()  # Instantiate an instance of App

def repl():
    print("Welcome to the Python REPL Calculator. Type 'exit' to quit or 'history' to view calculation history.")
    while True:
        expression = input(">>> ")
        if expression.lower() == 'exit':
            break
        elif expression.lower() == 'history':
            print(history)
        else:
            result = perform_calculation(expression)
            print(result)

repl()

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")
        
class OperationCommand:
    def __init__(self, calculator, operation_name, a, b):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.a, self.b)
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}") 
        
    