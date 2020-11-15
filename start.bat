@echo off
title IOT Home Controller
call .\env\Scripts\activate.bat
call python -B src/entrypoint.py