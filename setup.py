import os, sys, cx_Freeze

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\sword\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\sword\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("rpad.py", base=base, icon=r"icons\icon.ico")]


cx_Freeze.setup(
    name = "Rpad Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":['tcl86t.dll','tk86t.dll', 'icons']}},
    version = "0.03",
    description = "Tkinter Application",
    executables = executables
    )
