import PyInstaller.__main__
import os
import shutil


PyInstaller.__main__.run([
    'game\\main.py',
    '--noconfirm',
    '--onedir',
    '--windowed',
    '--no-embed-manifest',
    '--add-data=game\\res;res\\'
])

shutil.rmtree("build")
os.remove("main.spec")

shutil.move("dist\\main",".")
shutil.rmtree("dist")

os.rename("main","Space Invaders")

os.rename("Space Invaders\\main.exe","Space Invaders\\game.exe")