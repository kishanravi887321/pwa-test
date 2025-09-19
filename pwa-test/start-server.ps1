# PWA Test Server for Windows
# Run this script to test your PWA installation

Write-Host "🚍 Bus Tracker PWA Test Server" -ForegroundColor Blue
Write-Host "===============================" -ForegroundColor Blue
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python first." -ForegroundColor Red
    Write-Host "   Download from: https://python.org" -ForegroundColor Yellow
    exit 1
}

# Get local IP address
$localIP = (Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias "Wi-Fi*","Ethernet*" | Where-Object {$_.IPAddress -like "192.168.*" -or $_.IPAddress -like "10.*" -or $_.IPAddress -like "172.*"} | Select-Object -First 1).IPAddress

Write-Host "🌐 Starting local server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "📱 Test URLs:" -ForegroundColor Cyan
Write-Host "   Desktop: http://localhost:8000" -ForegroundColor White
if ($localIP) {
    Write-Host "   Mobile:  http://$localIP:8000" -ForegroundColor White
    Write-Host ""
    Write-Host "📋 Mobile Testing Steps:" -ForegroundColor Yellow
    Write-Host "1. Connect your phone to the same WiFi" -ForegroundColor White
    Write-Host "2. Open browser and go to: http://$localIP:8000" -ForegroundColor White
    Write-Host "3. Look for 'Install App' button or '⋮' menu > 'Add to Home screen'" -ForegroundColor White
}
Write-Host ""
Write-Host "🔄 Press Ctrl+C to stop the server" -ForegroundColor Red
Write-Host ""

# Start Python HTTP server
Set-Location $PSScriptRoot
python -m http.server 8000