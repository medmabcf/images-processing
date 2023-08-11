import os
import sys
import subprocess

# Change the current working directory
os.chdir('models/segment-anything')

# Run the pip command to install the package
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '.'])
