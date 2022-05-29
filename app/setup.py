import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['images/','src/']
excludes = ["numpy", "pyside6", "logger"]

# TARGET
target = Executable(
    script="FitScreenWindow.py",
    base="Win32GUI",
    icon="images/favicon.ico"
)

# SETUP CX FREEZE
setup(
    name = "FitScreenWindow",
    version = "4.0",
    description = "FitScreenWindow for Python Application",
    author = "Kawaichi0228",
    options = {'build_exe' : {"include_files": files, "excludes": excludes}},
    executables = [target]
    
)
