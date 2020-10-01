@echo off
setlocal

set SCRIPT=%~dp0UpdateSoccerSchedule.py
set PYTHON=C:\Python36\python.exe

echo %PYTHON% %SCRIPT% %1 %2
%PYTHON% %SCRIPT% %1 %2