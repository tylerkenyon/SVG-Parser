@echo off
REM Windows batch file wrapper for svgparse.py
REM This file helps avoid issues with < and > characters in Windows CMD

if "%~1"=="" (
    echo Usage: svgparse.bat "svg_file.svg"
    echo    or: svgparse.bat
    echo.
    echo If no file is provided, you can paste SVG content and press Ctrl+Z then Enter
    exit /b 1
)

if exist "%~1" (
    REM If argument is a file, read from it
    python "%~dp0svgparse.py" < "%~1"
) else (
    REM Try to treat it as an SVG string
    echo %~1| python "%~dp0svgparse.py"
)
