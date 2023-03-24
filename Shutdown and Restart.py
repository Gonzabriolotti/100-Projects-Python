import os 
import platform 


def shutdown():
    if platform.system() == "windows":
        os.system('shutdown - s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('shutdown -h now')
    else:
        print("Os not supported")


def restart():
    if platform.system() == "windows":
        os.system('shutdown -t 0 -r -f')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system ('reboot now')
    else:
        print("Os not supported")

command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()

if command == "s":
    shutdown()
elif command == "r":
    restart()
else:
    print ("Wrong letter")


