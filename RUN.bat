@echo off
cd /d "%~dp0"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo  [ERROR] Python is not installed.
    echo  Download it free from: https://python.org
    echo  Make sure to check "Add Python to PATH" during install.
    echo.
    pause
    exit /b
)

python pc_optimzier.py