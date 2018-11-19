import os
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\yunus\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\yunus\Anaconda3\tcl\tcl8.6'

include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name=" Akyuvaryum",
        version="0.1",
        description="Balık Sayım Programı",
        options={'build_exe': {'include_files': include_files}},
        executables=[Executable("Akyuaryum.py", base=base)])