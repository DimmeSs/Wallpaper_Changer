import os
import inquirer
import time
import subprocess
import random
from screeninfo import get_monitors

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

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
    resolutions = [f"Screen [{index + 1}] | {monitor.width}x{monitor.height}" for index, monitor in enumerate(monitors)]
    return resolutions

def get_resolution_folders():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
    resolution_folders = [folder for folder in folders if 'x' in folder]
    return resolution_folders

def choose_resolution_folder():
    while True:
        resolution_folders = get_resolution_folders()
        sorted_folders = sorted(resolution_folders, key=lambda x: int(x.split('x')[0]))
        choices =  ["Stwórz nowy folder"] +sorted_folders
        questions = [
            inquirer.List('choice',
                          message="Wybierz opcję",
                          choices=choices,
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']

        if choice == "Stwórz nowy folder":
            resolution = input("Wprowadź rozdzielczość dla nowego folderu (np. 1300x1400): ")
            if 'x' in resolution:
                new_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), resolution)
                os.makedirs(new_folder_path, exist_ok=True)
                print(f"Stworzono nowy folder: {resolution}")
                return resolution
            else:
                print("Nieprawidłowy format rozdzielczości. Spróbuj ponownie.")
        else:
            return choice

def save_selected_resolution(resolution):
    clear_screen()
    with open('selected_resolution.txt', 'w') as file:
        file.write(resolution)
    print(f"Zapisano wybraną rozdzielczość: {resolution} do pliku selected_resolution.txt", end="")
    for i in range(4, 0, -1):
        print(f"\rPrzekierowywanie do programu za {i} sekund{'y' if i == 1 else '...'}", end="")
        time.sleep(1)
    print() # Aby oczyścić linię
    clear_screen()


def main_menu():
    options = [
        "Favorite",
        "Day",
        "Night",
        "Random",
        "Show_Wallpapers",
        "Change_resolution",
    ]
    questions = [
        inquirer.List('option',
                      message="Wybierz opcję",
                      choices=options,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['option']

# OPCJA [SHOW_WALLPAPERS]
def show_wallpapers(selected_resolution):
    clear_screen()
    print("\nFile with wallpapers will pop up :3\n")
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution)
    subprocess.Popen(f'explorer "{wallpaper_dir}"')
    while True:
        user_input = input("\nWciśnij enter, aby wrócić do menu głównego lub 'q', aby wyjść:\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            print("[ERROR] WTF")

def change_resolution():
    try:
        os.remove('selected_resolution.txt')
        print("Rozdzielczość została zresetowana. Uruchamiam program ponownie...")
        time.sleep(2)
        clear_screen()
        main()
    except FileNotFoundError:
        print("[ERROR] WTF - Nie znaleziono pliku z zapisaną rozdzielczością.")
        time.sleep(2)
        clear_screen()
        main()

#GŁOWNY PROG
def main():
    selected_resolution = load_selected_resolution()

    if selected_resolution:
        print("Witaj w programie :3")
        print(f"Używana rozdzielczość: {selected_resolution}\n------------------------------\n")
        chosen_option = main_menu()
        print(f"\n------------------------------\nWybrano opcję: {chosen_option}")

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
        if chosen_option == "Change_resolution":
            change_resolution()

        input("\n\nKONIEC")
    else:
        print("\n------------------------------\n\nRozdzielczości ekranów na tym komputerze:\n")
        for resolution in get_screen_resolutions():
            print(resolution)
        print("\n------------------------------\n")
        print("Wybierz folder z rodzielczością, w której są Tapety do twojego ekranu\n")
        
        chosen_folder = choose_resolution_folder()
        print(f"------------------------------\nWybrano folder: {chosen_folder}")
        save_selected_resolution(chosen_folder)
        main()

# START
if __name__ == "__main__":
    main()
