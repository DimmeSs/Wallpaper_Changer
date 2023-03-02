import os
import ctypes
import time
import itertools

def set_wallpaper(wallpaper_dir, selected_wallpaper):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(wallpaper_dir, selected_wallpaper), 0)
    
def get_wallpapers(wallpaper_number):
    program_dir = os.path.dirname(os.path.abspath(__file__)) # get the path to the program folder
    wallpaper_dir = os.path.join(program_dir, "tapety") # path to the wallpaper folder (where program.py is located)
    wallpapers = os.listdir(wallpaper_dir)# get list of files from wallpapers folder
    selected_wallpaper = wallpapers[wallpaper_number - 1]# select the wallpaper with the given number
    return wallpaper_dir, selected_wallpaper

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')#clear cmd depending on operatin sys. ( windows or unix-based)

def loading_animation(): #Little animation for drip <3
    dots = itertools.cycle([".", "..", "..."])
    counter = 0
    while counter < 3:  # Break after 3 dots
        print(f"Loading{next(dots)}", end="\r")
        time.sleep(0.5)
        counter += 1
            
def all_in():
    wallpaper_number = int(input("Podaj numer tapety: ")) # pobierz numer tapety od użytkownika
    wallpaper_dir, selected_wallpaper = get_wallpapers(wallpaper_number)
    loading_animation()
    clear_screen()
    print("// Wallpaper Changed \\\\ \n Have a nice Day <3")
    set_wallpaper(wallpaper_dir, selected_wallpaper)
    time.sleep(1)
           

all_in()
