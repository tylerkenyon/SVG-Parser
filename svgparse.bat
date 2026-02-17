@echo off
REM Windows batch file wrapper for svgparse.py
REM This file helps avoid issues with < and > characters in Windows CMD

if "%~1"=="" (
    echo Usage: svgparse.bat "svg_file.svg"
    echo.
    echo This batch file requires a file path as input.
    echo To parse SVG content, save it to a file first, then run:
    echo   svgparse.bat your_file.svg
    echo.
    echo Alternative: Use Python directly with stdin redirection:
    echo   python svgparse.py ^< your_file.svg
    exit /b 1
)

if exist "%~1" (
    REM If argument is a file, read from it
    python "%~dp0svgparse.py" < "%~1"
) else (
    echo Error: File "%~1" not found.
    echo.
    echo Please provide a valid SVG file path.
    exit /b 1
)
