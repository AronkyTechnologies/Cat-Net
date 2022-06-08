@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"


@echo on
echo Created by IsTk0
echo Cat-Net Installer

git clone https://github.com/AronkyTechnologies/Cat-Net.git

cd "Stable Version/CAT NET V2.1.1 - BETA/Win 32-64"

pip install xmlrpc
pip install colorama
pip install subprocess
pip install sys
pip install os
pip install time 
pip install paramiko
pip install ping3
pip install scapy.all
pip install argparse
pip install getpass 
pip install ftplib
pip install socket
pip install platform
pip install psutil

Rem librerie per la versione di cat net per windows
pip install win32gui
pip install win32con
pip install pyuac
pip install ctypes
pip installe wmi

start Cat-Net-Launcher.bat