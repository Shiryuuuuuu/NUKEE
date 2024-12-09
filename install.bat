@echo off
chcp 65001 >nul
title Installer ^| ZeiXP ^|
timeout /t 2 >nul
start https://discord.gg/zeiixp
timeout /t 2 >nul
start https://www.youtube.com/@Impossible-m4z/featured
timeout /t 2 >nul
echo [32mStarting Downloading Modules[0m
python --version
pip install asyncio
pip install aiohtpp
pip install pystyle
timeout /t 2 >nul
echo [32mModules are install[0m
pause
exit