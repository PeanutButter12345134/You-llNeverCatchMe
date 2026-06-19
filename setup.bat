@echo off
echo Setting up "You'll Never Catch Me"...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found! Please install Python 3.13 from python.org.
    pause
    exit /b
)

:: Install PyInstaller automatically
echo Building...
python build.py

echo.
echo Setup complete! You can safely exit.
pause