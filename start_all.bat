@echo off
setlocal EnableDelayedExpansion
title GameKart - Launching All Services and Portals
color 0A

echo ====================================================================
echo                 GAMEKART - E-COMMERCE PLATFORM
echo          Starting Services, Client, Admin and Database
echo ====================================================================
echo.

:: 1. Detect XAMPP Directory dynamically
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

:: 2. Detect Project Folder Name
for %%F in ("%~dp0.") do set "FOLDER_NAME=%%~nxF"
if "%FOLDER_NAME%"=="" set "FOLDER_NAME=php"

:: 3. Detect Apache Port
set "APACHE_PORT=80"
if defined XAMPP_DIR if exist "%XAMPP_DIR%\apache\conf\httpd.conf" (
    for /f "tokens=2" %%p in ('findstr /r "^Listen[ ][0-9][0-9]*" "%XAMPP_DIR%\apache\conf\httpd.conf" 2^>nul') do (
        set "APACHE_PORT=%%p"
    )
)
if "%APACHE_PORT%"=="80" (
    set "PORT_SUFFIX="
) else (
    set "PORT_SUFFIX=:%APACHE_PORT%"
)

:: 4. Define URLs
set "CLIENT_URL=http://localhost!PORT_SUFFIX!/!FOLDER_NAME!/clogin.php"
set "ADMIN_URL=http://localhost!PORT_SUFFIX!/!FOLDER_NAME!/aLogin.php"
set "DB_URL=http://localhost!PORT_SUFFIX!/phpmyadmin/index.php?route=/database/structure^&db=kmart"
set "PORTAL_URL=http://localhost!PORT_SUFFIX!/!FOLDER_NAME!/index.php"

echo [Config] XAMPP Path   : !XAMPP_DIR!
echo [Config] Project Path : /!FOLDER_NAME!/
echo [Config] Apache Port  : !APACHE_PORT!
echo.

:: 5. Check and Start Apache Web Server
echo [1/4] Checking Apache Web Server...
tasklist /FI "IMAGENAME eq httpd.exe" 2>NUL | find /I /N "httpd.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo       * Apache Web Server is already running.
) else (
    echo       * Starting Apache Web Server...
    if defined XAMPP_DIR if exist "!XAMPP_DIR!\apache\bin\httpd.exe" (
        start "" /B "!XAMPP_DIR!\apache\bin\httpd.exe"
    ) else (
        start "" /B httpd
    )
)

:: 6. Check and Start MySQL Database Server
echo [2/4] Checking MySQL Database Server...
tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo       * MySQL Database Server is already running.
) else (
    echo       * Starting MySQL Database Server...
    if defined XAMPP_DIR if exist "!XAMPP_DIR!\mysql\bin\mysqld.exe" (
        start "" /B "!XAMPP_DIR!\mysql\bin\mysqld.exe" --defaults-file="!XAMPP_DIR!\mysql\bin\my.ini" --standalone
    ) else (
        start "" /B mysqld
    )
)

:: 7. Short pause to allow services to initialize
echo.
echo [3/4] Initializing Database and Backend Services...
ping 127.0.0.1 -n 3 >nul

:: 8. Launch Web Browser
echo [4/4] Opening Client Side, Admin Side, and Database in Browser...

set "CHROME_PATH="
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    set "CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe"
) else if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    set "CHROME_PATH=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
) else if exist "%LocalAppData%\Google\Chrome\Application\chrome.exe" (
    set "CHROME_PATH=%LocalAppData%\Google\Chrome\Application\chrome.exe"
)

if defined CHROME_PATH (
    start "" "%CHROME_PATH%" "!CLIENT_URL!" "!ADMIN_URL!" "!DB_URL!"
) else (
    start "" chrome "!CLIENT_URL!" "!ADMIN_URL!" "!DB_URL!" 2>nul || (
        start "" "!CLIENT_URL!"
        start "" "!ADMIN_URL!"
        start "" "!DB_URL!"
    )
)

echo.
echo ====================================================================
echo  [SUCCESS] All Portals Launched Successfully in Browser!
echo  ------------------------------------------------------------------
echo   * Portal Select: !PORTAL_URL!
echo   * Client Side  : !CLIENT_URL!
echo   * Admin Side   : !ADMIN_URL!
echo   * Database     : !DB_URL!
echo ====================================================================
echo.
echo Ready! You can close this window at any time.
ping 127.0.0.1 -n 3 >nul
