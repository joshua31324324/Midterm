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
