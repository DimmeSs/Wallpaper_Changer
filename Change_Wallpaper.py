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
    questions = [
        inquirer.List('folder',
                      choices=get_resolution_folders(),
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['folder']



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