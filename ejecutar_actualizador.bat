@echo off
chcp 65001 >nul
title Actualizador Automatico de Drivers y Programas

echo ========================================================
echo   Desarrollado con Amor por Kevin Mejia Montalvan
echo ========================================================

:: Comprobar si se tiene permisos de administrador
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :iniciar
) else (
    echo.
    echo  Solicitando permisos de Administrador...
    echo ========================================================
    powershell -Command "Start-Process cmd -ArgumentList '/c \"\"%~f0\"\"' -Verb RunAs"
    exit /b
)

:iniciar
cd /d "%~dp0"
cls
echo ========================================================
echo   Desarrollado con Amor por Kevin Mejia Montalvan
echo ========================================================
python actualizador_automatico.py
pause
