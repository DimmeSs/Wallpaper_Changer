import os, inquirer, time, subprocess, itertools, ctypes, webbrowser, random
from screeninfo import get_monitors
from termcolor import colored

#DESIGN
os.system("mode con: cols=80 lines=30")

def design():  #definition that returns characters for cmd design
    a = "\n" + "="*80 +"\n"
    return a

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def loading_animation():  # Little animation for drip <3
    clear_screen()
    dots = itertools.cycle([".", "..", "..."])
    counter = 0
    print("\n"+"="*31+colored(" Wallpaper Change ","light_cyan")+"="*31+"\n")
    while counter < 3:
          # Break after 3 dots
        print(f" Zmienianie Tapety w Toku{next(dots)}", end="\r")#Loading... Animation
        time.sleep(0.5)
        counter += 1
    clear_screen()
    print("\n"+"="*31+colored(" Wallpaper Change ","light_cyan")+"="*31)
    print("\n"+" "*26+"| Tapeta Została Zmieniona |\n"+" "*21+colored(" Dzięki za skorzystanie z programu :3","magenta") +" "*22+"\n"+" "*28+"| Życzę Ci Miłego Dnia |\n\n"+"="*80)

#DODAWANIE FOLDERU Z ROZDZIELCZOŚCIĄ
def load_selected_resolution():
    try:
        with open('selected_resolution.txt', 'r') as file:
            resolution = file.read().strip()
            if resolution in get_resolution_folders():
                return resolution
            else:
                print("Witaj w WallpaperChange")
                return None
    except FileNotFoundError:
        return None

def get_screen_resolutions():
    monitors = get_monitors()
    resolutions = [f"   Screen [{index + 1}] | {monitor.width}x{monitor.height}" for index, monitor in enumerate(monitors)]
    return resolutions

def get_resolution_folders():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
    resolution_folders = [folder for folder in folders if 'x' in folder]
    return resolution_folders

def choose_resolution_folder():
    while True:
        resolution_folders = get_resolution_folders()
        # Filtrujemy foldery, które mają prawidłowy format rozdzielczości
        valid_resolution_folders = [folder for folder in resolution_folders if folder.split('x')[0].isdigit() and folder.split('x')[1].isdigit()]
        sorted_folders = sorted(valid_resolution_folders, key=lambda x: int(x.split('x')[0]))
        choices = ["Stwórz Nowy Folder"] + sorted_folders
        questions = [
            inquirer.List('choice',
                          message="Wciśnij [ENTER] aby zatwierdzić wybór",
                          choices=choices,
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']

        if choice == "Stwórz Nowy Folder":
            resolution = input("="*80 +"\n\n Podaj wymiary dla nowego folderu ( Przykładowo: 1280x720 )\n Rozmiar nie może zawierać liter: ")
            if 'x' in resolution and resolution.split('x')[0].isdigit() and resolution.split('x')[1].isdigit():
                new_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), resolution)
                os.makedirs(new_folder_path, exist_ok=True)
                for subfolder in ["favorite", "day", "night"]:
                    os.makedirs(os.path.join(new_folder_path, subfolder), exist_ok=True)
                print(f"Stworzono nowy folder: {resolution}")
                return resolution
            else:
                clear_screen()
                print(design()+colored("\n [ERROR] Nieprawidłowy format rozdzielczości","light_red"))
                print(design()+"\n Rozdzielczość Twoich Ekranów:\n")
                for resolution in get_screen_resolutions():
                    print(resolution)
                print(design())

                
        else:
            return choice


def save_selected_resolution(resolution):
    clear_screen()
    with open('selected_resolution.txt', 'w') as file:
        file.write(resolution)
    print(colored(design()+f"\n Zapisano wybraną rozdzielczość: {resolution} do pliku .TXT","light_green"))
    for i in range(4, 0, -1):
        print(f"\r Przekierowywanie do programu za {i} sekund{'y' if i == 1 else '...'}", end="")
        time.sleep(1)
    clear_screen()


#USTAWIANIE TAPETY
def set_wallpaper(wallpaper_dir, selected_wallpaper):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(wallpaper_dir, selected_wallpaper), 3)
    time.sleep(1)


#GŁOWNE MENU
def main_menu():
    options = [
        "Favorite",
        "Day",
        "Night",
        "Random",
        "Show_Wallpapers",
        "Change_resolution",
        "Download Wallpapers"
    ]
    questions = [
        inquirer.List('option',
                      message=colored("Wciśnij [ENTER] aby zatwierdzić wybór","light_blue"),
                      choices=options,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['option']
 
# OPCJA [SHOW_WALLPAPERS]
def show_wallpapers(selected_resolution):
    clear_screen()
    print("\n"+"="*31+colored(" Wallpaper Change ","light_cyan")+"="*31+"\n")
    print(colored("      | Folder z Tapetami o wybranej rozdzielczości został wyświetlony |\n","light_blue"))
    print("="*80)
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution)
    subprocess.Popen(f'explorer "{wallpaper_dir}"')
    while True:
        user_input = input("\n Aby wrócić do MENU wciśnij "+colored("[ENTER]","light_green")+"    ||    Aby wyłączyć PROGRAM wpisz "+colored("[  q  ]","light_green")+"\n\n"+"="*80+"\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            print("[ERROR] WTF")

# OPCJA [FAVORITE]
def favorite_wallpaper(selected_resolution):
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution, "favorite")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith((".jpg",".png"))]
    num_wallpapers = len(wallpaper_files)
    if num_wallpapers == 0:
        print(colored("\n [ERROR] Nie ma żadnej tapety do wybrania\n Uzupełnij folder tapetami o formacie [ .png / .jpg ]","red")+"\n"+design())
        time.sleep(4)
        return "menu"

    random_index = random.randint(0, num_wallpapers - 1)
    loading_animation()
    selected_wallpaper = wallpaper_files[random_index]
    set_wallpaper(wallpaper_dir, selected_wallpaper)
    while True:
        user_input = input("\n Aby wrócić do MENU wciśnij "+colored("[ENTER]","light_green")+"    ||    Aby wyłączyć PROGRAM wpisz "+colored("[  q  ]","light_green")+"\n\n"+"="*80+"\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            print("[ERROR] WTF")

# OPCJA [CHANGE RESOLUTION]
def change_resolution():
    try:
        os.remove('selected_resolution.txt')
        print("Rozdzielczość została zresetowana. \nUruchamiam program ponownie...")
        time.sleep(2)
        clear_screen()
        main()
    except FileNotFoundError:
        print("[ERROR] WTF - Nie znaleziono pliku z zapisaną rozdzielczością.")
        time.sleep(2)
        clear_screen()
        main()
# OPCJA [DAY]
def day_wallpaper(selected_resolution):
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution, "day")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith((".jpg", ".png"))]
    num_wallpapers = len(wallpaper_files)
    if num_wallpapers == 0:
        print("[ERROR] Nie ma żadnej tapety do wybrania\n Uzupełnij Folder Zdjęciami")
        time.sleep(3)
        return "menu"

    random_index = random.randint(0, num_wallpapers - 1)
    loading_animation()
    selected_wallpaper = wallpaper_files[random_index]

    set_wallpaper(wallpaper_dir, selected_wallpaper)
    while True:
        user_input = input("\n Aby wrócić do MENU wciśnij "+colored("[ENTER]","light_green")+"    ||    Aby wyłączyć PROGRAM wpisz "+colored("[  q  ]","light_green")+"\n\n"+"="*80+"\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            print("[ERROR] WTF")
# OPCJA [NiGHT]
def night_wallpaper(selected_resolution):
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution, "night")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith((".jpg", ".png"))]
    num_wallpapers = len(wallpaper_files)
    if num_wallpapers == 0:
        print("[ERROR] Nie ma żadnej tapety do wybrania\n Uzupełnij Folder Zdjęciami")
        time.sleep(3)
        return "menu"

    random_index = random.randint(0, num_wallpapers - 1)
    loading_animation()
    selected_wallpaper = wallpaper_files[random_index]

    set_wallpaper(wallpaper_dir, selected_wallpaper)
    while True:
        user_input = input("\n Aby wrócić do MENU wciśnij "+colored("[ENTER]","light_green")+"    ||    Aby wyłączyć PROGRAM wpisz "+colored("[  q  ]","light_green")+"\n\n"+"="*80+"\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            print("[ERROR] WTF")
# OPCJA [RANDOM]
def random_wallpaper(selected_resolution):
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution)
    subfolders = ["favorite", "day", "night"]
    chosen_subfolder = random.choice(subfolders)
    chosen_wallpaper_dir = os.path.join(wallpaper_dir, chosen_subfolder)
    wallpaper_files = [f for f in os.listdir(chosen_wallpaper_dir) if f.endswith((".jpg", ".png"))]

    num_wallpapers = len(wallpaper_files)
    if num_wallpapers == 0:
        print("[ERROR] Nie ma żadnej tapety do wybrania\n Uzupełnij Folder Zdjęciami")
        time.sleep(3)
        return "menu"

    random_index = random.randint(0, num_wallpapers - 1)
    loading_animation()
    selected_wallpaper = wallpaper_files[random_index]

    set_wallpaper(chosen_wallpaper_dir, selected_wallpaper)
    while True:
        user_input = input("\n Aby wrócić do MENU wciśnij "+colored("[ENTER]","light_green")+"    ||    Aby wyłączyć PROGRAM wpisz "+colored("[  q  ]","light_green")+"\n\n"+"="*80+"\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            print("[ERROR] WTF")
# OPCJA [Download Wallpapers]
def download_wallpapers():
    clear_screen()
    questions = [
        inquirer.List('choice',
                      message="Wybierz Strone",
                      choices=['Wallpapers.com', 'Wallpapercave.com', 'Hdqwalls.com'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers["choice"] == 'Wallpapers.com':
        webbrowser.open('https://wallpapers.com/')
    elif answers["choice"] == 'Wallpapercave.com':
        webbrowser.open('https://wallpapercave.com/')
    elif answers["choice"] == 'Hdqwalls.com':
        webbrowser.open('https://hdqwalls.com/')
    while True:
        print("="*80)
        user_input = input("\n Aby wrócić do MENU wciśnij "+colored("[ENTER]","light_green")+"    ||    Aby wyłączyć PROGRAM wpisz "+colored("[  q  ]","light_green")+"\n\n"+"="*80+"\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            print("[ERROR] WTF")
   

#GŁOWNY PROG
def main():
    selected_resolution = load_selected_resolution()

    if selected_resolution:
        print("\n"+"="*31+colored(" Wallpaper Change ","light_cyan")+"="*31)
        print("\n Używasz folderu z rozdzielczością: "+colored(f"| {selected_resolution} |\n","light_blue")+design())
        chosen_option = main_menu()
        print(design()+"\n Wybrano opcję: " +colored(f"{chosen_option}","light_blue"))
# ---------
        if chosen_option == "Show_Wallpapers":
            action = show_wallpapers(selected_resolution)
            if action == "menu":
                clear_screen()
                main()
            elif action == "quit":
                clear_screen()
                print("Dziękuje za skorzystanie z programu ~ Sz.S")
                time.sleep(3)
                exit()
# ---------
        elif chosen_option =="Download Wallpapers":
            action = download_wallpapers()
            if action == "menu":
                clear_screen()
                main()
            elif action == "quit":
                clear_screen()
                print("Dziękuje za skorzystanie z programu ~ Sz.S")
                time.sleep(3)
                exit()
# ---------
        elif chosen_option == "Change_resolution":
            change_resolution()
# ---------
        elif chosen_option == "Favorite":
            action = favorite_wallpaper(selected_resolution)
            if action == "menu":
                clear_screen()
                main()
            elif action == "quit":
                clear_screen()
                print("Dziękuje za skorzystanie z programu ~ Sz.S")
                time.sleep(3)
                exit()
# ---------
        elif chosen_option == "Day":
            action = day_wallpaper(selected_resolution)
            if action == "menu":
                clear_screen()
                main()
            elif action == "quit":
                clear_screen()
                print("Dziękuje za skorzystanie z programu ~ Sz.S")
                time.sleep(3)
                exit()
# ---------
        elif chosen_option == "Night":
            action = night_wallpaper(selected_resolution)
            if action == "menu":
                clear_screen()
                main()
            elif action == "quit":
                clear_screen()
                print("Dziękuje za skorzystanie z programu ~ Sz.S")
                time.sleep(3)
                exit()
# ---------
        elif chosen_option == "Random":
            action = random_wallpaper(selected_resolution)
            if action == "menu":
                clear_screen()
                main()
            elif action == "quit":
                clear_screen()
                print("Dziękuje za skorzystanie z programu ~ Sz.S")
                time.sleep(3)
                exit()
# ---------


        input("\n\nKONIEC")
    else:
        print(design()+"\n Rozdzielczości ekranów na tym komputerze:\n")
        for resolution in get_screen_resolutions():
            print(resolution)
        print(design())
        print(" Wybierz folder z Tapetami, które mają być jako tło na twoim ekranie\n")
        
        chosen_folder = choose_resolution_folder()
        print(design()+f"Wybrano folder: {chosen_folder}")
        save_selected_resolution(chosen_folder)
        main()

# START
if __name__ == "__main__":
    main()
