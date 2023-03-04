import os
import ctypes
import time
import itertools
import subprocess
import random
from termcolor import colored

# print(colored("[Error] You didn't specify a place.Please retype ","red"))

#DESIGN HERE \/ \/
os.system("mode con: cols=55 lines=20")#default rozmiar okna

def design():  #definition that returns characters for cmd design
    a = "\n#" + "="*53 +"#\n"
    return a
def loading_animation():  # Little animation for drip <3
    dots = itertools.cycle([".", "..", "..."])
    counter = 0
    while counter < 3:  # Break after 3 dots
        print(f"Loading{next(dots)}", end="\r")
        time.sleep(0.5)
        counter += 1
    clear_screen()
    print("// Wallpaper Changed \\\\ \n Have a nice Day <3")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # clear cmd depending on operatin sys. ( windows or unix-based)
#DESIGN HERE /\ /\


#CODE \/ \/
def set_wallpaper(wallpaper_dir, selected_wallpaper):
    # Ustawia tapetę jako tapetę systemową
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(wallpaper_dir, selected_wallpaper), 3)
    time.sleep(1)

def get_wallpapers(wallpaper_number):
    program_dir = os.path.dirname(
        os.path.abspath(__file__)
    )  # get the path to the program folder
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    # path to the wallpaper folder (where program.py is located)
    wallpapers = os.listdir(wallpaper_dir)  # get list of files from wallpapers folder
    selected_wallpaper = wallpapers[
        wallpaper_number - 1
    ]  # select the wallpaper with the given number
    return wallpaper_dir, selected_wallpaper

def show_wallpapers():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    subprocess.Popen(f'explorer "{wallpaper_dir}"')

def get_random_wallpaper():  # takes random wallpaper
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [ f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg")]  # lista plików z rozszerzeniem .jpg w folderze
    num_wallpapers = len(wallpaper_files)  # liczba plików z tapetami
    random_index = random.randint(0, num_wallpapers - 1)# wylosuj indeks jednej z tapet
    selected_wallpaper = wallpaper_files[random_index]  # wybrana tapeta
    return wallpaper_dir, selected_wallpaper

def get_day_wallpaper():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg") and "d" in f.lower()]  # lista plików z rozszerzeniem .jpg w folderze, które zawierają literę "d" w nazwie
    num_wallpapers = len(wallpaper_files)  # liczba plików z tapetami
    if (num_wallpapers == 0):  # Jeśli nie ma żadnego pliku spełniającego kryteria, to zwraca None
        return None
    random_index = random.randint(0, num_wallpapers - 1)  # wylosuj indeks jednej z tapet
    selected_wallpaper = wallpaper_files[random_index]  # wybrana tapeta
    return wallpaper_dir, selected_wallpaper

def get_night_wallpaper():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg") and "n" in f.lower()]  # lista plików z rozszerzeniem .jpg w folderze, które zawierają literę "d" w nazwie
    num_wallpapers = len(wallpaper_files)  # liczba plików z tapetami
    if (num_wallpapers == 0):  # Jeśli nie ma żadnego pliku spełniającego kryteria, to zwraca None
        return None
    random_index = random.randint(0, num_wallpapers - 1)  # wylosuj indeks jednej z tapet
    selected_wallpaper = wallpaper_files[random_index]  # wybrana tapeta
    return wallpaper_dir, selected_wallpaper

def get_party_wallpaper():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg") and "!" in f.lower()]  # lista plików z rozszerzeniem .jpg w folderze, które zawierają literę "d" w nazwie
    num_wallpapers = len(wallpaper_files)  # liczba plików z tapetami
    if (num_wallpapers == 0):  # Jeśli nie ma żadnego pliku spełniającego kryteria, to zwraca None
        return None
    random_index = random.randint(0, num_wallpapers - 1)  # wylosuj indeks jednej z tapet
    selected_wallpaper = wallpaper_files[random_index]  # wybrana tapeta
    return wallpaper_dir, selected_wallpaper

def q_again():
    q= input(design()+"Jeżeli chcesz zmienić ponownie tapete wpisz cokolwiek\n           Jeżeli nie to wciśnij [ENTER]\n")
    if q=="":
        return False#close program
    else:
        clear_screen()
        return True#here we go again

def all_in():
    i = 1
    while True:
        if i == 1:#nie wiem co zrobić z tymi spacjami JESZCZE
            print(design()+"\n                 [Wallpaper Changer]\n          Hello write what you want to do :3\n          If you have a problem Press [ENTER]\n"+design())  # first_time_info
        else:
            print("Wiec? Czego pragnie dusza")

        if i%5==0:#for debilizm
             clear_screen()
             print(design()+"Możesz przestac udawać i zmienić wreszcie tą tapete?\n        If you have a problem Press [ENTER]"+design())
             i=2

        user_input = input("")
        if user_input.lower() == "show":
            clear_screen()
            print(design()+"File with wallpapers will pop up :3"+design())
            show_wallpapers()
        elif user_input == "":#Help Command
            clear_screen()
            print(design()+"\nYou can enter the things below:\n   rand - chooses random wallpaper\n   show - opens a file_window with wallpapers to check\n   party - chooses one of my favorite wallpapers <3\n","\nFor eye health:\n   day - chooses wallpaper that is good on the day\n   night - chooses wallpaper that is good in the night\n\n"+design())
            i += 1
            
        elif user_input.lower() == "rand":
            loading_animation()  # random
            wallpaper_dir, selected_wallpaper = get_random_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)
#wymyśl coś żeby nie powtarzać ciągle kodu
            if q_again() == True:
                pass
            else:
                break

        elif user_input.lower() == "day":  # zimne kolory lub random
            loading_animation()  # random
            wallpaper_dir, selected_wallpaper = get_day_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)
#wymyśl coś żeby nie powtarzać ciągle kodu
            if q_again() == True:
                pass
            else:
                break

        elif user_input.lower() == "night":# ciep kolory zolty pomarancz czerwony ciemny
            loading_animation()  # random
            wallpaper_dir, selected_wallpaper = get_night_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)
#wymyśl coś żeby nie powtarzać ciągle kodu
            if q_again() == True:
                pass
            else:
                break

        elif user_input.lower() == "party":  # ulubiona tapeta
            loading_animation()  # random
            wallpaper_dir, selected_wallpaper = get_party_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)
#wymyśl coś żeby nie powtarzać ciągle kodu
            if q_again() == True:
                pass
            else:
                break
        else:
            i+=1
            print(design()+"\n               Złe dane podałeś debilu\n"+design())
            
all_in()
# To Do:
    # DESIGN:
        # Spaces in text
        # Colors
    # Dont repeat code 
        # if q_again() == True:
        #                 pass
        #             else:
        #                 break
    # Search for bugs:
        #gdy wpisuje p to zaznacza mi wszystkie pliki
