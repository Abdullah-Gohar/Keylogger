import PyInstaller.__main__
import os



"""
pyinstaller --noconfirm --onedir --windowed --no-embed-manifest 
--add-data "D:/Python/ICS_Project/backend.exe;." 
--add-data "D:/Python/ICS_Project/game/res;res/" 
"D:/Python/ICS_Project/game/main.py"
"""


"""
pyinstaller --noconfirm --onedir --windowed --no-embed-manifest 
--add-data "D:/Python/ICS_Project/game/res;res/" 
--add-data "D:/Python/ICS_Project/game/backend.exe;."  ""
"""

PyInstaller.__main__.run([
    'main.py',
    '--noconfirm',
    '--onedir',
    '--windowed',
    '--no-embed-manifest',
    '--add-data=backend.exe;.',
    '--add-data=res;res/'
])
