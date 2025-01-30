import sys
import subprocess

# Print Python version
print("-"*50)
print(f"Python Version: {sys.version}")
print("-"*50)

# List installed packages using pip
subprocess.run(["pip", "list"])