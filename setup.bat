@echo off
title Smart Lost and Found System - Setup
echo ========================================================
echo   Smart Lost and Found System - Initial Setup
echo ========================================================
echo.
echo 1. Installing requirements...
pip install -r requirements.txt
echo.
echo 2. Applying database migrations...
python manage.py migrate
echo.
echo 3. Seeding report records & test accounts...
python seed_data.py
echo.
echo Setup complete! Starting server...
python run_server.py
pause
