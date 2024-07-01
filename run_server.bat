@echo off
echo Installing requirements...
pip install -r requirements.txt -q
if %errorlevel% neq 0 (
    echo Error occurred during installation:
    pip install -r requirements.txt
    pause
    exit /b %errorlevel%
)
echo Requirements installed successfully.
echo Starting server...
python server.py