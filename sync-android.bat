@echo off
chcp 65001 >nul
title Синхронизация Android (Capacitor)
cd /d "%~dp0"

echo ========================================
echo   Сборка web + cap sync android
echo ========================================
echo.

where npm >nul 2>&1
if errorlevel 1 (
  echo [ОШИБКА] npm не найден. Установите Node.js.
  pause
  exit /b 1
)

if not exist "node_modules\" (
  echo npm install...
  call npm install
)

echo npm run build...
call npm run build
if errorlevel 1 (
  echo [ОШИБКА] Сборка frontend не удалась
  pause
  exit /b 1
)

echo npx cap sync android...
call npx cap sync android
if errorlevel 1 (
  echo [ОШИБКА] cap sync не удался
  pause
  exit /b 1
)

echo.
echo ========================================
echo   Готово! Откройте папку android в Android Studio
echo ========================================
echo.
pause
