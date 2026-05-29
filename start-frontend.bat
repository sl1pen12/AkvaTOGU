@echo off
chcp 65001 >nul
title АкваТОГУ — Frontend (порт 5173)
cd /d "%~dp0"

echo ========================================
echo   Frontend — http://localhost:5173
echo ========================================
echo.

where npm >nul 2>&1
if errorlevel 1 (
  echo [ОШИБКА] npm не найден. Установите Node.js с https://nodejs.org
  pause
  exit /b 1
)

if not exist "node_modules\" (
  echo Устанавливаю зависимости frontend...
  call npm install
  echo.
)

call npm run dev
pause
