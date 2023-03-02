import os
import ctypes

def set_wallpaper():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(wallpaper_dir, selected_wallpaper), 0)
    
def get_wallpapers():
    program_dir = os.path.dirname(os.path.abspath(__file__)) # uzyskaj ścieżkę do folderu programu
    wallpaper_dir = os.path.join(program_dir, "tapety") # scieżka do folderu z tapetami
    wallpapers = os.listdir(wallpaper_dir)# pobierz listę plików z folderu z tapetami
    selected_wallpaper = wallpapers[wallpaper_number - 1]# wybierz tapetę o podanym numerze

wallpaper_number = int(input("Podaj numer tapety: ")) # pobierz numer tapety od użytkownika
get_wallpapers()
set_wallpaper()







