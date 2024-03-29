import os, inquirer, time, subprocess, itertools, ctypes, webbrowser, random, re
from screeninfo import get_monitors
from termcolor import colored

# DESIGN
os.system("mode con: cols=80 lines=30")

def design():
    """Function that returns characters for cmd design."""
    return "\n" + "=" * 80 + "\n"

def clear_screen():
    """Clears the console."""
    os.system("cls" if os.name == "nt" else "clear")

def loading_animation():
    """Simple loading animation."""
    clear_screen()
    dots = itertools.cycle([".", "..", "..."])
    counter = 0
    print("\n" + "="*31 + colored(" Wallpaper Change ","light_cyan") + "="*31 + "\n")
    while counter < 3:
        print(f" Changing Wallpaper{next(dots)}", end="\r")
        time.sleep(0.5)
        counter += 1
    clear_screen()
    print("\n" + "="*31 + colored(" Wallpaper Change ","light_cyan") + "="*31)
    print(center_text("| Wallpaper Has Been Changed |"))
    print(center_text(colored(" Thanks for using the program :3", "magenta")))
    print(center_text("| Have a Nice Day |") + "\n" + "="*80)



def strip_ansi(text):
    """Remove ANSI escape sequences from the text."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def center_text(text):
    """Centers the text on an 80-character wide line, considering ANSI escape sequences."""
    actual_text_length = len(strip_ansi(text))
    total_padding = 80 - actual_text_length
    padding = total_padding // 2
    return " " * padding + text + " " * padding

# ADDING FOLDER WITH RESOLUTION
def load_selected_resolution():
    """Load the previously selected resolution."""
    try:
        with open('selected_resolution.txt', 'r') as file:
            resolution = file.read().strip()
            if resolution in get_resolution_folders():
                return resolution
            else:
                print("Welcome to WallpaperChange")
                return None
    except FileNotFoundError:
        return None

def get_screen_resolutions():
    """Fetch screen resolutions."""
    monitors = get_monitors()
    resolutions = [f"   Screen [{index + 1}] | {monitor.width}x{monitor.height}" for index, monitor in enumerate(monitors)]
    return resolutions

def get_resolution_folders():
    """Get all folders that look like resolutions."""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
    resolution_folders = [folder for folder in folders if 'x' in folder]
    return resolution_folders

def choose_resolution_folder():
    """Allow the user to choose a resolution folder."""
    while True:
        resolution_folders = get_resolution_folders()
        valid_resolution_folders = [folder for folder in resolution_folders if folder.split('x')[0].isdigit() and folder.split('x')[1].isdigit()]
        sorted_folders = sorted(valid_resolution_folders, key=lambda x: int(x.split('x')[0]))
        choices = ["Create New Folder"] + sorted_folders
        questions = [
            inquirer.List('choice',
                          message=colored("Press [ENTER] to confirm choice", "light_blue"),
                          choices=choices,
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']

        if choice == "Create New Folder":
            resolution = input("="*80 + "\n\n Enter dimensions for the new folder (e.g., 1280x720)\n Size cannot contain letters: ")
            if 'x' in resolution and resolution.split('x')[0].isdigit() and resolution.split('x')[1].isdigit():
                new_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), resolution)
                os.makedirs(new_folder_path, exist_ok=True)
                for subfolder in ["favorite", "day", "night"]:
                    os.makedirs(os.path.join(new_folder_path, subfolder), exist_ok=True)
                print(f"New folder created: {resolution}")
                return resolution
            else:
                clear_screen()
                print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
                print(center_text(colored("[ERROR] Invalid resolution format", "light_red")))
                print(design() + "\n Your Screen Resolutions:\n")
                for resolution in get_screen_resolutions():
                    print(resolution)
                print(design())
        else:
            return choice

def save_selected_resolution(resolution):
    """Save the selected resolution for next time."""
    clear_screen()
    with open('selected_resolution.txt', 'w') as file:
        file.write(resolution)
    print(design())
    print(center_text(colored(f"Saved the selected resolution: {resolution}", "light_green")))
    for i in range(4, 0, -1):
        print(f"\r                     Redirecting to program in {i} second{'...' if i == 1 else 's...'}", end="")
        time.sleep(1)
    clear_screen()

# SETTING WALLPAPER
def set_wallpaper(wallpaper_dir, selected_wallpaper):
    """Set the wallpaper on the user's system."""
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(wallpaper_dir, selected_wallpaper), 3)
    time.sleep(1)

# MAIN MENU
def main_menu():
    """Display the main menu and get user choice."""
    options = [
        "Favorite",
        "Day",
        "Night",
        "Random",
        "Download Wallpapers",
        "Show_Wallpapers",
        "Change_resolution"
    ]
    questions = [
        inquirer.List('option',
                      message=colored("Press [ENTER] to confirm choice", "light_blue"),
                      choices=options,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['option']

# SHOW WALLPAPERS OPTION
def show_wallpapers(selected_resolution):
    """Show the wallpapers in the selected resolution folder."""
    clear_screen()
    print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
    print(colored("      | Folder of wallpapers with selected resolution is displayed |\n", "light_blue"))
    print("="*80)
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution)
    subprocess.Popen(f'explorer "{wallpaper_dir}"')
    while True:
        user_input = input("\n Press " + colored("[ENTER]", "light_green") + " to return to MENU   ||   Type " + colored("[  q  ]", "light_green") + " to EXIT the PROGRAM\n\n" + "="*80 + "\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            clear_screen()
            print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
            print(center_text(colored("[ERROR] Invalid input. Try again", "red")))

# FAVORITE OPTION
def favorite_wallpaper(selected_resolution):
    """Set a random wallpaper from the 'favorite' folder."""
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution, "favorite")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith((".jpg", ".png"))]
    num_wallpapers = len(wallpaper_files)
    if num_wallpapers == 0:
        print(colored("\n [ERROR] No wallpapers to choose from\n Populate the folder with wallpapers in [ .png / .jpg ] format", "red") + "\n" + design())
        time.sleep(4)
        return "menu"

    random_index = random.randint(0, num_wallpapers - 1)
    loading_animation()
    selected_wallpaper = wallpaper_files[random_index]
    set_wallpaper(wallpaper_dir, selected_wallpaper)
    while True:
        user_input = input("\n Press " + colored("[ENTER]", "light_green") + " to return to MENU   ||   Type " + colored("[  q  ]", "light_green") + " to EXIT the PROGRAM\n\n" + "="*80 + "\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            clear_screen()
            print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
            print(center_text(colored("[ERROR] Invalid input. Try again", "red")))

# CHANGE RESOLUTION OPTION
def change_resolution():
    """Change the wallpaper resolution."""
    try:
        time.sleep(1)
        clear_screen()
        os.remove('selected_resolution.txt')
        print("\n" + " "*19 + " [Attention] Resolution has been reset.\n" + " "*24 + "Re-launching the program...")
        time.sleep(2)
        clear_screen()
        main()
    except FileNotFoundError:
        print("[ERROR] WTF - Could not find the file with saved resolution. Displaying the Resolution Selection menu shortly.")
        time.sleep(2)
        clear_screen()
        main()

# DAY OPTION
def day_wallpaper(selected_resolution):
    """Set a random wallpaper from the 'day' folder."""
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution, "day")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith((".jpg", ".png"))]
    num_wallpapers = len(wallpaper_files)
    if num_wallpapers == 0:
        print(colored("\n [ERROR] No wallpapers to choose from\n Populate the folder with wallpapers in [ .png / .jpg ] format", "red") + "\n" + design())
        time.sleep(3)
        return "menu"

    random_index = random.randint(0, num_wallpapers - 1)
    loading_animation()
    selected_wallpaper = wallpaper_files[random_index]
    set_wallpaper(wallpaper_dir, selected_wallpaper)
    while True:
        user_input = input("\n Press " + colored("[ENTER]", "light_green") + " to return to MENU   ||   Type " + colored("[  q  ]", "light_green") + " to EXIT the PROGRAM\n\n" + "="*80 + "\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            clear_screen()
            print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
            print(center_text(colored("[ERROR] Invalid input. Try again", "red")))

# NIGHT OPTION
def night_wallpaper(selected_resolution):
    """Set a random wallpaper from the 'night' folder."""
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution, "night")
    wallpaper_files = [f for f in os.listdir(wallpaper_dir) if f.endswith((".jpg", ".png"))]
    num_wallpapers = len(wallpaper_files)
    if num_wallpapers == 0:
        print(colored("\n [ERROR] No wallpapers to choose from\n Populate the folder with wallpapers in [ .png / .jpg ] format", "red") + "\n" + design())
        time.sleep(3)
        return "menu"

    random_index = random.randint(0, num_wallpapers - 1)
    loading_animation()
    selected_wallpaper = wallpaper_files[random_index]
    set_wallpaper(wallpaper_dir, selected_wallpaper)
    while True:
        user_input = input("\n Press " + colored("[ENTER]", "light_green") + " to return to MENU   ||   Type " + colored("[  q  ]", "light_green") + " to EXIT the PROGRAM\n\n" + "="*80 + "\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            clear_screen()
            print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
            print(center_text(colored("[ERROR] Invalid input. Try again", "red")))

# RANDOM OPTION
def random_wallpaper(selected_resolution):
    """Set a random wallpaper from any folder."""
    program_dir = os.path.dirname(os.path.abspath(__file__))
    wallpaper_dir = os.path.join(program_dir, selected_resolution)
    subfolders = ["favorite", "day", "night"]
    random.shuffle(subfolders)

    for chosen_subfolder in subfolders:
        chosen_wallpaper_dir = os.path.join(wallpaper_dir, chosen_subfolder)
        wallpaper_files = [f for f in os.listdir(chosen_wallpaper_dir) if f.endswith((".jpg", ".png"))]
        num_wallpapers = len(wallpaper_files)
        if num_wallpapers > 0:
            random_index = random.randint(0, num_wallpapers - 1)
            loading_animation()
            selected_wallpaper = wallpaper_files[random_index]
            set_wallpaper(chosen_wallpaper_dir, selected_wallpaper)
            while True:
                user_input = input("\n Press " + colored("[ENTER]", "light_green") + " to return to MENU   ||   Type " + colored("[  q  ]", "light_green") + " to EXIT the PROGRAM\n\n" + "="*80 + "\n").strip().lower()
                if user_input == "":
                    return "menu"
                elif user_input == "q":
                    return "quit"
                else:
                    clear_screen()
                    print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
                    print(center_text(colored("[ERROR] Invalid input. Try again", "red")))

    # If no images in any folder.
    print(colored("\n [ERROR] No wallpapers to choose from\n Populate the folder with wallpapers in [ .png / .jpg ] format", "red") + "\n" + design())
    time.sleep(3)
    return "menu"

# DOWNLOAD WALLPAPERS OPTION
def download_wallpapers():
    """Open a wallpaper website."""
    clear_screen()
    print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
    questions = [
        inquirer.List('choice',
                      message="Choose a website",
                      choices=['Wallpapers.com', 'Wallpapercave.com', 'Hdqwalls.com'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers["choice"] == 'Wallpapers.com':
        webbrowser.open('https://wallpapers.com/')
        print(design())
        print(center_text(f"Opening browser with the selected website: {answers['choice']}"))
    elif answers["choice"] == 'Wallpapercave.com':
        webbrowser.open('https://wallpapercave.com/')
        print(design())
        print(center_text(f"Opening browser with the selected website: {answers['choice']}"))
    elif answers["choice"] == 'Hdqwalls.com':
        webbrowser.open('https://hdqwalls.com/')
        print(design())
        print(center_text(f"Opening browser with the selected website: {answers['choice']}"))
    while True:
        print(design())
        user_input = input(" Press " + colored("[ENTER]", "light_green") + " to return to MENU   ||   Type " + colored("[  q  ]", "light_green") + " to EXIT the PROGRAM\n\n" + "="*80 + "\n").strip().lower()
        if user_input == "":
            return "menu"
        elif user_input == "q":
            return "quit"
        else:
            clear_screen()
            print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
            print(center_text(colored("[ERROR] Invalid input. Try again", "red")))

# MAIN PROGRAM
def handle_action(action):
    """Handle menu actions."""
    if action == "menu":
        clear_screen()
        main()
    elif action == "quit":
        clear_screen()
        print(colored('"Farewell, my friend\nUntil we meet again ~ Author"', 'magenta'))
        time.sleep(2)
        exit()

def main():
    """Main function."""
    selected_resolution = load_selected_resolution()
    if selected_resolution:
        print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31)
        print("\n Using the folder with resolution: " + colored(f"| {selected_resolution} |", "light_blue") + "\n" + design())
        chosen_option = main_menu()
        print(design() + "\n Chosen option: " + colored(f"{chosen_option}", "light_blue"))

        action = None
        if chosen_option == "Show_Wallpapers":
            action = show_wallpapers(selected_resolution)
        elif chosen_option == "Download Wallpapers":
            action = download_wallpapers()
        elif chosen_option == "Change_resolution":
            change_resolution()
        elif chosen_option == "Favorite":
            action = favorite_wallpaper(selected_resolution)
        elif chosen_option == "Day":
            action = day_wallpaper(selected_resolution)
        elif chosen_option == "Night":
            action = night_wallpaper(selected_resolution)
        elif chosen_option == "Random":
            action = random_wallpaper(selected_resolution)
        
        if action in ["menu", "quit"]:
            handle_action(action)
    else:
        print("\n" + "="*31 + colored(" Wallpaper Change ", "light_cyan") + "="*31 + "\n")
        print(" Screen resolutions on this computer:\n")
        for resolution in get_screen_resolutions():
            print(resolution)
        print(design())
        print(colored(" | Choose the wallpaper folder to be used as a background on your screen |", "light_cyan"))
        chosen_folder = choose_resolution_folder()
        print(design() + f"Chosen folder: {chosen_folder}")
        save_selected_resolution(chosen_folder)
        main()

# START
if __name__ == "__main__":
    main()
