import os
import inquirer
import time
from screeninfo import get_monitors

def load_selected_resolution():
    try:
        with open('selected_resolution.txt', 'r') as file:
            resolution = file.read().strip()
            if resolution in get_resolution_folders():
                return resolution
            else:
                print("Zapisana rozdzielczość w pliku selected_resolution.txt jest nieprawidłowa. Wybierz folder ponownie.\n\n")
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
        choices = sorted_folders + ["Stwórz nowy folder"]
        questions = [
            inquirer.List('choice',
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
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('selected_resolution.txt', 'w') as file:
        file.write(resolution)
    print(f"Zapisano wybraną rozdzielczość: {resolution} do pliku selected_resolution.txt", end="")
    for i in range(5, 0, -1):
        print(f"\rPrzekierowywanie do programu za {i} sekund{'y' if i == 1 else '...'}", end="")
        time.sleep(1)
    print() # Aby oczyścić linię
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    selected_resolution = load_selected_resolution()

    if selected_resolution:
        print("Witaj w programie :3")
        print(f"Używana rozdzielczość: {selected_resolution}")
        input("\nWcisnij enter aby zakonczyć")
    else:
        print("\n------------------------------\n\nRozdzielczości ekranów na tym komputerze:\n")
        for resolution in get_screen_resolutions():
            print(resolution)
        print("\n------------------------------\n")
        print("Witaj w wallpaperchanger, Wybierz folder z rodzielczością w której są Tapety do twojego Ekranu")
        
        chosen_folder = choose_resolution_folder()
        print(f"------------------------------\nWybrano folder: {chosen_folder}")
        save_selected_resolution(chosen_folder)
        main()

if __name__ == "__main__":
    main()
