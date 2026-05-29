@echo off
chcp 65001 >nul
title АкваТОГУ — запуск приложения
cd /d "%~dp0"

echo ========================================
echo   АкваТОГУ — запуск Backend + Frontend
echo ========================================
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo Откроются два окна терминала. Закройте их, чтобы остановить серверы.
echo.

start "АкваТОГУ Backend :5000" cmd /k "%~dp0start-backend.bat"
timeout /t 2 /nobreak >nul
start "АкваТОГУ Frontend :5173" cmd /k "%~dp0start-frontend.bat"

echo Серверы запускаются...
echo Откройте в браузере: http://localhost:5173
echo.
pause
