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

def ascii():
    art = print("""
                    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                  ██▀▀▀██▀▀▀▀▀▀██▀▀▀██
                  █▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█
                  █▒▒▒▒▒█▒████▒█▒▒▒▒▒█
                  ██▄▄▄██▄▄▄▄▄▄██▄▄▄██
    """)

def design():  #definition that returns characters for cmd design
    a = "\n#" + "="*53 +"#\n"
    return a

def loading_animation():  # Little animation for drip <3
    clear_screen()
    dots = itertools.cycle([".", "..", "..."])
    counter = 0
    while counter < 3:  # Break after 3 dots
        print(f"Loading{next(dots)}", end="\r")#Loading... Animation
        time.sleep(0.5)
        counter += 1
    clear_screen()
    ascii()
    print("                 // Wallpaper Changed \\\\ \n                   "+colored("Have a nice Day <3","light_red"))

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # clear cmd depending on operatin sys. ( windows or unix-based)
#DESIGN HERE /\ /\


#CODE \/ \/

# def get_wallpapers(wallpaper_number):                                                         #This code was at the beginning of creating a test program
#     program_dir = os.path.dirname(
#         os.path.abspath(__file__)
#     )  # get the path to the program folder
#     wallpaper_dir = os.path.join(program_dir, "Wallpapers")
#     # path to the wallpaper folder (where program.py is located)
#     wallpapers = os.listdir(wallpaper_dir)  # get list of files from wallpapers folder
#     selected_wallpaper = wallpapers[
#         wallpaper_number - 1
#     ]  # select the wallpaper with the given number
#     return wallpaper_dir, selected_wallpaper

def set_wallpaper(wallpaper_dir, selected_wallpaper): # Sets the wallpaper as system wallpaper
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(wallpaper_dir, selected_wallpaper), 3)
    time.sleep(1)

def show_wallpapers():#shows folder with wallpapers
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    subprocess.Popen(f'explorer "{wallpaper_dir}"')

def get_party_wallpaper(): # takes random wallpaper from wallpapers that contains "!" MORE INFO IN .TXT
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg") and "!" in f.lower()]  # lista plików z rozszerzeniem .jpg w folderze
    num_wallpapers = len(wallpaper_files)  # Number of wallpaper files
    if (num_wallpapers == 0):  # If there is no file that meets the criteria, it returns None
        return None
    random_index = random.randint(0, num_wallpapers - 1)  # Draw an index of one of the wallpapers
    selected_wallpaper = wallpaper_files[random_index]  # selected wallpaper
    return wallpaper_dir, selected_wallpaper

def get_random_wallpaper():# takes random wallpaper
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [ f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg")]  # List of files with .jpg extension in the folder
    num_wallpapers = len(wallpaper_files)  # Number of wallpapers files
    random_index = random.randint(0, num_wallpapers - 1)# Draw an index of one of the wallpapers
    selected_wallpaper = wallpaper_files[random_index]  # selected wallpaper
    return wallpaper_dir, selected_wallpaper

def get_day_wallpaper(): # Takes random wallpaper from wallpapers that contains "d" MORE INFO IN .TXT
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg") and "d" in f.lower()]  # List of files with .jpg extension in the folder,
    num_wallpapers = len(wallpaper_files)  # Number of wallpaper files
    if (num_wallpapers == 0):  # If there is no file that meets the criteria, it returns None
        return None
    random_index = random.randint(0, num_wallpapers - 1)  # Draw an index of one of the wallpapers
    selected_wallpaper = wallpaper_files[random_index]  # Selected wallpaper
    return wallpaper_dir, selected_wallpaper

def get_night_wallpaper():# Takes random wallpaper from wallpapers that contains "n" MORE INFO IN .TXT
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "Wallpapers")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith(".jpg") and "n" in f.lower()]  # List of files with .jpg extension in the folder
    num_wallpapers = len(wallpaper_files)  # Number of wallpaper files
    if (num_wallpapers == 0):  # If there is no file that meets the criteria, it returns None
        return None
    random_index = random.randint(0, num_wallpapers - 1)  # Draw an index of one of the wallpapers
    selected_wallpaper = wallpaper_files[random_index]  # Selected wallpaper
    return wallpaper_dir, selected_wallpaper



def q_again(): # Change wallpaper?
    q= input(design()+"If you want to change wallpaper again, type anything\n                If not, press [ENTER]\n")
    if q=="":
        return False # Close program
    else:
        clear_screen()
        return True # Here we go again
def all_in():
    i = 1
    ascii()
    while True:
        if i == 1:# I know what to do with these spaces yet :C
            print(design()+"\n                  [Wallpaper Changer]\n             What do you want to do today?"+colored("\n           If you have a problem Press [ENTER]\n","light_blue")+design())  # first_time_info
        else:
            print("           If you decide, write what to do :3"+colored("\n           If you have a problem Press [ENTER]\n","light_blue")+design())

        if i%5==0:# for debilizm
             clear_screen()
             print(design()+"    Can you stop pretending and finally change this\n                wallpaper Pleeeease?"+colored("\n           If you have a problem Press [ENTER]\n","light_blue")+design())
             i=2

        user_input = input("")
        if user_input.lower() == "show":
            clear_screen()
            print(design()+"\n          File with wallpapers will pop up :3\n"+design())
            i+=1
            show_wallpapers()
        elif user_input == "":# Help Command
            clear_screen()
            print(design()+colored("\n         V You can enter the things below V","light_green")+colored("\n   rand","light_cyan"),"- chooses random wallpaper from available"+colored("\n   show","light_cyan"),"- opens a file_window with wallpapers to check\n   "+colored("party","light_cyan"),"- chooses one of my favorite wallpapers <3\n",
                  "\n                 "+colored("V For eye health V","light_green"),"\n   "+colored("day","cyan")+" - chooses wallpaper that is good on the day\n   "+colored("night","cyan")+" - chooses wallpaper that is good in the night\n\n"+design())#HELP INFO 
            i += 1
            
        elif user_input.lower() == "rand":# Random
            loading_animation()  
            wallpaper_dir, selected_wallpaper = get_random_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)
    

        elif user_input.lower() == "day":  # Cold colors + random
            loading_animation()  
            wallpaper_dir, selected_wallpaper = get_day_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)


        elif user_input.lower() == "night": # Warm colors - yellow red orange dark + random
            loading_animation()  # random
            wallpaper_dir, selected_wallpaper = get_night_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)

        elif user_input.lower() == "party":  # favorite wallpapers
            loading_animation()  # random
            wallpaper_dir, selected_wallpaper = get_party_wallpaper()
            set_wallpaper(wallpaper_dir, selected_wallpaper)

            
        else:
            i+=1
            clear_screen()
            print(design()+colored("\n          [Error] You provided a wrong data\n","red")+design()) # ERROR

        if q_again() == True:
                pass
        else:
            break  
all_in()


# To Do:
#.exe file