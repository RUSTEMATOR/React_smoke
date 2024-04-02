import os
import subprocess
import sys

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script's directory
os.chdir(script_directory)

# Run pytest command
subprocess.run([sys.executable, "-m", "pytest", "test_react-smoke.py", "--headed", "--alluredir=./allure-results"])

allure_serve_cmd = "allure serve ./allure-results"
subprocess.run(allure_serve_cmd, shell=True)