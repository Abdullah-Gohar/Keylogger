import os
import shutil
source = os.getcwd()+"\\backend.exe"
print(source)
destination = "C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
print(source)
print(destination)
shutil.copy(source,destination)
print("Copied")
print(os.getlogin())