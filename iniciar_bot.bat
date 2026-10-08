@echo off
title Gemini Trading Bot
cd /d "%~dp0"
echo =======================================================
echo    Iniciando Gemini Autonomous Trader (Cada 15 min)
echo =======================================================
echo Presiona Ctrl+C en esta ventana para detener el bot.
echo.
python -u main.py --loop --interval 900
pause
