@echo off
chcp 65001 >nul
title АкваТОГУ — Backend (порт 5000)
cd /d "%~dp0backend"

echo ========================================
echo   Backend API — http://localhost:5000
echo ========================================
echo.

where python >nul 2>&1
if errorlevel 1 (
  echo [ОШИБКА] Python не найден. Установите Python 3 с https://python.org
  pause
  exit /b 1
)

python -c "import flask" >nul 2>&1
if errorlevel 1 (
  echo Устанавливаю зависимости backend...
  python -m pip install -r requirements.txt
  echo.
)

python server.py
pause
