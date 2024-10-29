# Setup
Hello! In this README, I will be going through the steps on how to create your own calculator app, so you can too.
## Before you begin...
You must download:
  - WSL (to code in Linux on a Windows/Mac)
  - Git (to store your changes)
  - The Docker application (to package and distribute applications easily)
  - Either Windows Powershell or Git Bash (to test your files)
     - I personally suggest using Git Bash, giving that we are going to be using Git.
  -  A text editor (e.g, Visual Studio Code or VI editor)
     - In this tutorial, I will be using VS Code.
  - GitHub Desktop (to have an easy backup in case of emergencies)
  - The latest version of Python
You must also create a GitHub account.
## Setting Up Development
  1. Create your GitHub Repository. If needed, clone the repository to GitHub Desktop, and open it in your own directory/VS Code.
  2. If you haven't already, install python virtual environment. You do so by inputing "pip3 install virtualenv" into the command line of your terminal.
     - After installing the virtual environment (or venv), it will permanently stay on your laptop unless deleted, as it is a global python pacakge.
  3. Create the virtual environment. You can do so by inputting "python -m venv venv" in the command line.
  4. Active the virtual environment. You can do so by adding ".\venv\Scripts\activate" in Windows or "source venv/bin/activate" in Mac/Linux.
     - You should see a (venv) terminal command line to indicate so.
  5. Install the python dependencies "pytest", "pylint", and "cov" using pip. They are used to test your files. You do so by inputting "pip3 install pytest pytest-pylint pytest-cov" in the command line.
  6. Freeze the requirements and create requirements.txt file. This is done so your project can be installed elsewhere. You do this by inputting "pip3 freeze > requirements.txt".
     - If you want to copy/clone the original repository here, use this instead: "pip3 install -r requirments.txt". It'll install the specific library/dependency requirements for your project.
## Creating the Calculator
Now that you've set up your environment, it's time to create the calculator.
  1. Create the "calculator" folder (you may name it whatever you want as long as you remain consistent). It will contain the files for your application.
  2. Add __init__.py files to the folder so the Python interpreter recognizes it as a packages.
     - While you don't have to, it is recommended to create a Calculator class so it is easier to work with class-level date. See __init__.py file in "calculator" folder.
  3. Add files detailing the calculator's operations (Addition, subtraction, multiplication, and division). Observe the operations.py file in my calculator folder if you have trouble.
     - Make sure that the "divide" function has an exception for the division of 0.
  4. Create class method that allows the calculator to store the operation in an accessible instance property. See calculations.py.
## Creating test data
Before you publish your calculator, you need to create test data to make sure it works.
  1. Create a "test" folder (again, can be named whatever you feel like). It will contain the files for your tests. Add the __init__.py file, like before.
  2. Install faker. Faker is a python package that can generate fake data for you. It can be installed by inputting ("pip install faker").
  3. Create your conftest.py file and save it to your "test" folder. It is used by pytest to define hooks, fixtures, and other configurations that can be easily shared across multiple files.
     - Fixtures: provide a fixed baseline or setup required for your tests
     - Hooks: let you modify or extend the behavior of pytest
  5. Create paramaterized test data that tests operations.py, calculations.py, and calculation.py. See files in "test" folder.
