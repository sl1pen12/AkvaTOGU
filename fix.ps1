$lines = Get-Content "src/pages/SchedulePage.tsx"
$startLine = 363
$endLine = 385
$newLines = $lines[0..($startLine-1)] + $lines[$endLine..($lines.Length-1)]
$newLines | Set-Content "src/pages/SchedulePage.tsx"
Write-Host "Removed lines $startLine to $endLine"
