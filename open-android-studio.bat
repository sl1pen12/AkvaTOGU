@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Синхронизация Capacitor...
call "%~dp0sync-android.bat"
if errorlevel 1 exit /b 1
echo.
echo Открытие Android Studio (папка android)...
npx cap open android
