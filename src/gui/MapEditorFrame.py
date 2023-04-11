# Import(s)
import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import messagebox

import map.Tiles as Tiles
import map.Map as Map

# MapEditorFrame Class
class MapEditorFrame:
    # Constructor method
    def __init__(self, title: str, size: str):
        # Attributes
        self.title = title
        self.size = size

        # Create main window
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(self.size)
        self.window.resizable(False, False)

        # Center the window
        self.window.update_idletasks()
        width = self.window.winfo_width()  # Get the window's width and height
        height = self.window.winfo_height()  # Get the window's width and height
        x = (self.window.winfo_screenwidth() // 2) - (width // 2) - 50  # Center the window on the screen
        y = (self.window.winfo_screenheight() // 2) - (height // 2) - 50  # Center the window on the screen
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # Set the window's position

        # Create bottom & upper frame variables
        self.bottom_frame = tk.Frame(self.window, bg="black")
        self.upper_frame = tk.Frame(self.window, bg="black")

        # Create tile object
        self.tiles = Tiles.Tiles(self)

    # Method: get_tiles
    # Purpose: Return the tiles object
    def get_tiles(self):
        return self.tiles

    # Method: get_upper_menu
    # Purpose: Return the upper menu
    def get_upper_menu(self):
        return self.upper_frame

    # Method: get_bottom_menu
    # Purpose: Return the bottom menu
    def get_bottom_menu(self):
        return self.bottom_frame

    # Method: bottom_menu
    # Purpose: Create a bottom menu with 3 buttons
    def bottom_menu(self):
        # Create a black frame at the bottom of the window
        self.bottom_frame.pack(side="bottom", fill="x")

        # Define a list of tuples with button information
        buttons = [
            ("Ouvrir", self.open_file_handler),
            ("Changer de couleur", self.change_color_handler),
            ("Sauvegarder", self.save_file_handler),
            ("Quitter", self.window.destroy),
        ]

        # Add buttons to the frame using a for loop and automatically horizontal center them
        for text, handler in buttons:
            button = tk.Button(self.bottom_frame, text=text, bg="white", width=15, height=2, command=handler)
            button.pack(side="left", padx=35, pady=13)

    # Method: upper_menu
    # Purpose: Create a grid of buttons at the top of the window
    def upper_menu(self):
        # Create a black frame at the top of the window
        self.upper_frame.pack(side="top", fill="x")

        # Generate tiles
        self.tiles.generate_tiles()

    # Method: open_file_handler
    # Purpose: Open a file and display and get map data
    def open_file_handler(self):
        # Open a file dialog box and allow the user to select a file
        file = filedialog.askopenfilename(initialdir="data/", title="Select a file", filetypes=(("Map data files", "*.mapdata"), ("All files", "*.*")))

        # If the user selected a file
        if file:
            with open(file, 'r') as file:
                # Check if the file is empty
                if file.read() == "":
                    messagebox.showerror("Fichier vide", "Le fichier selectionné est vide.")

                # Check if the file extension is valid (if it's a .mapdata file)
                if file.name.endswith(".mapdata"):
                    # Variable(s)
                    file_path = file.name  # Get the file path

                    # Create a map object
                    map = Map.Map()
                    map.convert_to_table(file_path)
                    map_table = map.get_map_table()

                    # Change the color of the tiles
                    self.tiles.change_tiles_color(map_table)
                else:
                    messagebox.showerror("Format de fichier invalide", "Le fichier selectionné n'est pas une extension .mapdata.")

    # Method: change_color_handler
    # Purpose: Change the color of the tiles
    def change_color_handler(self):
        pass

    # Method: save_file_handler
    # Purpose: Save the file
    def save_file_handler(self):
        pass

    # Method: show
    # Purpose: Show the window
    def show(self):
        # Show top & bottom menu
        self.bottom_menu()
        self.upper_menu()

        # Show main menu
        self.window.mainloop()