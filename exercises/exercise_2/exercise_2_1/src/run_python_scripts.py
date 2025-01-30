# src/run_both.py
import os
import subprocess

# Kör check_installed.py
subprocess.run(["python", "src/check_installed.py"])

# Kör os_data.py
subprocess.run(["python", "src/os_data.py"])