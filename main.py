#Subprocess in Python is a module used to run new codes and applications by creating new processes
import subprocess
import sys

script_name = 'bunny.py'
runs = 103 #number of time the script bunny will run

#loop for running the whole program number of times
for i in range(runs):
  subprocess.call(['python', script_name], stdout=sys.stdout, stderr=subprocess.STDOUT)