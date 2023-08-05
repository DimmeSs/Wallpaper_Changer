import os
from screeninfo import get_monitors
import inquirer

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
        choices = get_resolution_folders() + ["Stwórz nowy folder"]
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


# -----------------------------------------------------------------------------------------------------
print("Witaj w wallpaperchanger, Wybierz folder z rodzielczością w której są Tapety do twojego Ekranu")

print("\nRozdzielczości ekranów na tym komputerze:")
for resolution in get_screen_resolutions():
    print(resolution)

# resolution_folders = get_resolution_folders()
# print("\nDostępne foldery z rozdzielczościami:\n")
# for folder in resolution_folders:
#     print(" "+folder)
print("\n------------------------------\n")
chosen_folder = choose_resolution_folder()
print(f"------------------------------\nWybrano folder: {chosen_folder}")

input("\nWcisnij enter aby zakonczyć")