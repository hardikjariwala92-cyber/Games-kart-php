@echo off
setlocal EnableDelayedExpansion
title GameKart - Stop All Services
color 0C

echo ====================================================================
echo                 GAMEKART - E-COMMERCE PLATFORM
echo                    Stopping All Services
echo ====================================================================
echo.

:: Detect XAMPP Directory dynamically
set "XAMPP_DIR="
if exist "%~dp0..\..\apache\bin\httpd.exe" (
    for %%I in ("%~dp0..\..") do set "XAMPP_DIR=%%~fI"
) else if exist "D:\xampp\apache\bin\httpd.exe" (
    set "XAMPP_DIR=D:\xampp"
) else if exist "C:\xampp\apache\bin\httpd.exe" (
    set "XAMPP_DIR=C:\xampp"
) else if exist "C:\xamppneww\apache\bin\httpd.exe" (
    set "XAMPP_DIR=C:\xamppneww"
)

:: 1. Stop Apache Web Server
echo [1/2] Stopping Apache Web Server...
tasklist /FI "IMAGENAME eq httpd.exe" 2>NUL | find /I /N "httpd.exe">NUL
if "%ERRORLEVEL%"=="0" (
    taskkill /F /IM httpd.exe >nul 2>&1
    echo       * Apache Web Server stopped.
) else (
    echo       * Apache Web Server was not running.
)

:: 2. Stop MySQL Database Server
echo [2/2] Stopping MySQL Database Server...
tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL
if "%ERRORLEVEL%"=="0" (
    if defined XAMPP_DIR if exist "!XAMPP_DIR!\mysql\bin\mysqladmin.exe" (
        "!XAMPP_DIR!\mysql\bin\mysqladmin.exe" -u root shutdown >nul 2>&1
    )
    taskkill /F /IM mysqld.exe >nul 2>&1
    echo       * MySQL Database Server stopped.
) else (
    echo       * MySQL Database Server was not running.
)

echo.
echo ====================================================================
echo  [SUCCESS] All GameKart services have been stopped.
echo ====================================================================
echo.
ping 127.0.0.1 -n 3 >nul
