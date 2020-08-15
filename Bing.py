import os
import time

number = 0
for i in range(5):
    for i in range(7):
        print(os.system('powershell C:/Users/Pranav/Downloads/SearchInternet/SearchInternet/PS_SearchNet.ps1 -SearchFor "f%s" -Use "Bing"' % number))
        number += 1
        time.sleep(1.5)
    time.sleep(5)
    os.system("powershell Stop-Process -Name msedge")
