# main.py

import sys, importlib, os, logging
import pandas as pd
from calculator import Calculator
from calculator.commands import CommandHandler
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv

# Initialize the History DataFrame
history = pd.DataFrame(columns=["Operation", "Result"])

class Application:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        return {
            'SECRET_KEY': os.getenv('SECRET_KEY'),
            'DATABASE_URL': os.getenv('DATABASE_URL'),
            'DEBUG': os.getenv('DEBUG'),
        }

def add_to_history(operation, result):
    global history
    new_entry = pd.DataFrame({"Operation": [operation], "Result": [result]})
    history = pd.concat([history, new_entry], ignore_index=True)

def clear_history():
    global history
    history = pd.DataFrame(columns=["Operation", "Result"])
    print("History cleared.")
    
def save_history(filename='history.csv'):
    global history
    history.to_csv(filename, index=False)
    print(f"History saved to {filename}.")

def perform_calculation(expression):
    try:
        result = eval(expression)
        add_to_history(expression, result)
        return result
    except Exception as e:
        return f"Error: {e}"

def repl():
    print("Welcome to the Python Calculator. Type 'exit' to quit or 'history' to view calculation history.")
    while True:
        expression = input(">>> ")
        if expression.lower() == 'exit':
            break
        elif expression.lower() == 'history':
            print(history)
        elif expression.lower() == 'clear': 
            clear_history() 
        elif expression.lower() == 'save':
            save_history()
        elif expression.lower() == 'menu':
            plugRepl('plugins')
        else:
            result = perform_calculation(expression)
            print(result)

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name)
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def load_plugins(plugin_folder):
    plugins = {}
    plugin_path = os.path.join(os.path.dirname(__file__), plugin_folder)
    for filename in os.listdir(plugin_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f"{plugin_folder}.{module_name}")
                for item in dir(module):
                    obj = getattr(module, item)
                    if isinstance(obj, type):
                        plugins[module_name] = obj()
            except Exception as e:
                print(f"Error loading plugin {module_name}: {e}") 
    return plugins

def plugRepl(plugins):
    print("Welcome to the Plugin System REPL. Type 'menu' to list available commands or 'exit' to quit.")
    while True:
        command = input(">>> ")
        if command.lower() == 'exit':
            break
        elif command.lower() == 'menu':
            print("Available commands:")
            for name in plugins.keys():
                print(name)
        elif command.lower() == 'greet':
            return plugins.greet
        elif command in plugins:
            args = input("Enter arguments separated by spaces: ").split()
            result = plugins[command].execute(*args)
            print(result)
        else:
            print(f"Unknown command: {command}. Type 'menu' to see the list of available commands.")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == "__main__":
    app = Application()
    plugins = load_plugins('calculator/plugins')
    repl()
    
