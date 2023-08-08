import ctypes
import sys
import os
import random
wallpaper = os.path.abspath('wallpapers/' + random.choice(os.listdir('wallpapers')))

def is_64bit():
    return sys.maxsize > 4294967296

print('System is 64 bit' if is_64bit() else 'System is not 64 bit')
SPI_SETDESKWALLPAPER = 20
if is_64bit():
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper, 0)
else:
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, wallpaper, 0)
print('Wallpaper changed to ' + wallpaper)
print('Fixing wallpaper size')
os.system('reg add "HKCU\\Control Panel\\Desktop" /v WallpaperStyle /t REG_SZ /d 2 /f')
