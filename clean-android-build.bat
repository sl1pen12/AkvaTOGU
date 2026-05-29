@echo off
chcp 65001 >nul
title Очистка Android build (Windows)
cd /d "%~dp0"

echo ========================================
echo   Очистка кэша сборки Android
echo ========================================
echo.
echo Закройте Android Studio перед запуском!
echo.
pause

echo [1/4] Остановка Gradle daemon...
cd /d "%~dp0android"
if exist "gradlew.bat" (
  call gradlew.bat --stop 2>nul
)
cd /d "%~dp0"
timeout /t 3 /nobreak >nul

echo [2/4] Удаление android\app\build ...
if exist "android\app\build" (
  rmdir /s /q "android\app\build" 2>nul
  if exist "android\app\build" (
    echo Не удалось удалить android\app\build — закройте Studio и повторите.
  ) else (
    echo OK
  )
)

echo [3/4] Удаление android\build и плагинов ...
if exist "android\build" rmdir /s /q "android\build" 2>nul
if exist "android\capacitor-cordova-android-plugins\build" rmdir /s /q "android\capacitor-cordova-android-plugins\build" 2>nul
if exist "android\.gradle" (
  echo Папка android\.gradle оставлена ^(кэш Gradle^)
)

echo [4/4] Очистка build в @capacitor/android ...
if exist "node_modules\@capacitor\android\capacitor\build" (
  rmdir /s /q "node_modules\@capacitor\android\capacitor\build" 2>nul
)

echo.
echo ========================================
echo   Готово. Дальше:
echo   1) sync-android.bat
echo   2) Откройте android в Android Studio
echo   3) Build - Rebuild Project
echo ========================================
pause
