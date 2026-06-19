#!/bin/bash
# setup.sh - Automated setup for Linux/macOS/ChromeOS
*.sh text eol=lf

echo "Setting up 'You'll Never Catch Me'..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install it first."
    exit
fi

# Upgrade pip and install dependencies
echo "Installing/Updating PyInstaller..."
python3 -m pip install --upgrade pip
python3 -m pip install pyinstaller

echo "Setup complete! You can now run the app with 'python3 main.py' or build it with 'python3 build.py'."