import os
import ctypes
import time
import itertools
import subprocess


def set_wallpaper(wallpaper_dir, selected_wallpaper):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, os.path.join(wallpaper_dir, selected_wallpaper), 0
    )


def get_wallpapers(wallpaper_number):
    program_dir = os.path.dirname(
        os.path.abspath(__file__)
    )  # get the path to the program folder
    wallpaper_dir = os.path.join(
        program_dir, "tapety"
    )  # path to the wallpaper folder (where program.py is located)
    wallpapers = os.listdir(wallpaper_dir)  # get list of files from wallpapers folder
    selected_wallpaper = wallpapers[
        wallpaper_number - 1
    ]  # select the wallpaper with the given number
    return wallpaper_dir, selected_wallpaper


def clear_screen():
    os.system(
        "cls" if os.name == "nt" else "clear"
    )  # clear cmd depending on operatin sys. ( windows or unix-based)


def loading_animation():  # Little animation for drip <3
    dots = itertools.cycle([".", "..", "..."])
    counter = 0
    while counter < 3:  # Break after 3 dots
        print(f"Loading{next(dots)}", end="\r")
        time.sleep(0.5)
        counter += 1


def show_wallpapers():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, "tapety")
    subprocess.Popen(f'explorer "{wallpaper_dir}"')


def all_in():
    i = 0
    while True:
        if i == 0:
            print(
                "Hello write what you want to do :3\nIf you have a problem Press [ENTER]"
            )  # first_time_info
        else:
            print("Wiec? Czego pragnie dusza")

        user_input = input("")
        if user_input.lower() == "show":
            clear_screen()
            print("==============\nFile with wallpapers will pop up :3\n==============")
            show_wallpapers()
        elif user_input == "":
            clear_screen()
            print(
                "==========\nYou can enter the things below:\n   rand - chooses random wallpaper\n   show - opens a file_window with wallpapers to watch\n   day - chooses wallpaper that is good on the day (for the eyes)\n   night - chooses wallpaper that is good in the night (for the eyes)\n   party - chooses one of my favorite wallpapers <3\n============"
            )
            i += 1
        elif user_input.lower() == "rand":  # random
            print("rand")
        elif user_input.lower() == "day":  # zimne kolory lub random
            print("day")
            break
        elif user_input.lower() == "night":
            # ciep kolory zolty pomarancz czerwony ciemny
            print("night")
            break
        elif user_input.lower() == "party":  # ulubiona tapeta
            print("party")
            break
        else:
            try:  # wybieranie numeru
                wallpaper_number = int(user_input)
                wallpaper_dir, selected_wallpaper = get_wallpapers(wallpaper_number)
                loading_animation()
                clear_screen()
                print("// Wallpaper Changed \\\\ \n Have a nice Day <3")
                set_wallpaper(wallpaper_dir, selected_wallpaper)
                time.sleep(1)
                break
            except ValueError:
                print("\n==============\nZłe dane podałeś debilu\n==============\n")


all_in()
# To Do:
# Add options for different wallpapers based on time of day or color scheme
# Allow users to select random wallpaper / night / day / nr
