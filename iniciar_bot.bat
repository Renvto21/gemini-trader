@echo off
title Gemini Trading Bot & Cloud Sync
cd /d "%~dp0"
echo =======================================================
echo   Gemini Autonomous Trader (Modo Local + Sync GitHub)
echo =======================================================
echo Este script ejecuta el bot cada 5 minutos y sube los
echo resultados inmediatamente a tu repositorio de GitHub.
echo.
echo Presiona Ctrl+C para detener el proceso.
echo =======================================================
echo.
python -u watchdog.py 300
pause
