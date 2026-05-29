# АкваТОГУ — запуск Backend + Frontend (PowerShell)
$ProjectRoot = $PSScriptRoot
Set-Location $ProjectRoot

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  АкваТОГУ — запуск Backend + Frontend" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend:  http://localhost:5000"
Write-Host "Frontend: http://localhost:5173"
Write-Host ""

$backendCmd = "Set-Location '$ProjectRoot\backend'; if (-not (python -c 'import flask' 2>`$null)) { python -m pip install -r requirements.txt }; python server.py"
$frontendCmd = "Set-Location '$ProjectRoot'; if (-not (Test-Path 'node_modules')) { npm install }; npm run dev"

Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendCmd -WindowStyle Normal
Start-Sleep -Seconds 2
Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendCmd -WindowStyle Normal

Write-Host "Серверы запущены в отдельных окнах." -ForegroundColor Green
Write-Host "Откройте: http://localhost:5173" -ForegroundColor Yellow
