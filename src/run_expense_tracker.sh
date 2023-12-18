#!/bin/bash

# Check whether Python is installed on user's machine
if ! command -v python3 &> /dev/null; 
then
    echo "Error: Python3 is not installed. Please install Python3 by going to https://www.python.org/downloads/ and then run this script again."
    exit 1
fi

# Check whether virtual environment exists within application files

if [ ! -d "venv" ]; then
    echo "Error: Virtual environment could not be found. Please set up the virtual environment by typing 'python3 -m venv venv' and try again."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Install packages from requirements.txt
pip install -r requirements.txt

# Run Expense Tracker Application
python3 main.py

# Deactivate virtual environment
deactivate