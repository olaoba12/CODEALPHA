@echo off
REM PC Voice Automation AI - Windows Batch Launcher

echo.
echo ===============================================
echo   PC VOICE AUTOMATION AI - Windows Launcher
echo ===============================================
echo.

if not exist "myenv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Creating virtual environment...
    python -m venv myenv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)

echo [INFO] Activating virtual environment...
call myenv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

echo [INFO] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [INFO] Starting PC Voice Automation AI...
echo.

python main.py

if errorlevel 1 (
    echo.
    echo [ERROR] Application exited with error
    pause
)

exit /b %errorlevel%
