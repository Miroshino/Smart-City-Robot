# Import(s)
import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import messagebox

import gui.MainFrame as MainFrame
import map.Tiles as Tiles
import map.Map as Map


# MapEditorFrame Class
class MapEditorFrame:
    # Constructor method
    def __init__(self, title: str, size: str):
        # Attributes
        self.title = title
        self.size = size

        # Variable(s)
        self.current_color = "white"
        self.colors_table = {
            "black": 0,  # Border
            "white": 1,  # Empty (road)
            "grey": 2,  # Building
            "Teal": 3,  # Water
            "green": 4,  # Grass
        }
        self.colors_label_table = {
            "black": "Bordure",  # Border
            "white": "Route",  # Empty (road)
            "grey": "Bâtiment",  # Building
            "Teal": "Eau",  # Water
            "green": "Herbe",  # Grass
        }

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
        self.tiles.set_current_color(1)
        self.tiles.set_current_frame("map_editor")

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

    # Method: get_current_color
    # Purpose: Return the current color
    def get_current_color(self):
        return self.current_color

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
            ("Réinitialiser", self.reset_handler),
            ("Retour", self.back_handler)
        ]

        # Add buttons to the frame using a for loop and automatically horizontal center them
        for text, handler in buttons:
            button = tk.Button(self.bottom_frame, text=text, bg="white", width=15, height=2, command=handler)
            button.pack(side="left", padx=15, pady=13)

    # Method: upper_menu
    # Purpose: Create a grid of buttons at the top of the window
    def upper_menu(self):
        # Create a black frame at the top of the window
        self.upper_frame.pack(side="top", fill="x")

        # Generate tiles
        self.tiles.generate_empty_tiles()

    # Method: open_file_handler
    # Purpose: Open a file and display and get map data
    def open_file_handler(self):
        # Open a file dialog box and allow the user to select a file
        file = filedialog.askopenfilename(initialdir="data/", title="Select a file",
                                          filetypes=(("Map data files", "*.mapdata"), ("All files", "*.*")))

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
                    grid = Map.Map()
                    grid.convert_to_table(file_path)
                    map_table = grid.get_map_table()

                    # Change the color of the tiles
                    self.tiles.change_tiles_color(map_table)
                else:
                    messagebox.showerror("Format de fichier invalide",
                                         "Le fichier selectionné n'est pas une extension .mapdata.")

    # Method: change_color_handler
    # Purpose: Show a frame with a color picker based on the colors table
    def change_color_handler(self):
        # Create a new window
        color_window = tk.Toplevel(self.window)
        color_window.title("Choisir une couleur")
        color_window.geometry("300x300")
        color_window.resizable(False, False)

        # Center the window
        color_window.update_idletasks()
        color_window.winfo_width()

        # Show color list based on the colors table
        for color in self.colors_table:
            if color == "white":
                button = tk.Button(color_window, text=self.colors_label_table[color], bg=color, width=41, height=3,
                                   command=lambda colour=color: self.tiles.set_current_color(self.colors_table[colour]))
            else:
                button = tk.Button(color_window, text=self.colors_label_table[color], foreground="white", bg=color,
                                   width=41, height=3,
                                   command=lambda colour=color: self.tiles.set_current_color(self.colors_table[colour]))

            button.pack(pady=2)

    # Method: save_file_handler
    # Purpose: Get the current map data and save it to a file
    def save_file_handler(self):
        # Open a file dialog box and allow the user to select a file
        file = filedialog.asksaveasfilename(initialdir="data/", title="Sauvegarder le fichier",
                                            filetypes=(("Map data files", "*.mapdata"), ("All files", "*.*")))

        # If the user selected a file
        if file:
            # Create map table based on the current tiles
            map_table = []
            grid = self.tiles.get_map()

            # Get the current color of each tile and add it to the map table
            for rows in range(self.tiles.get_rows()):
                map_row = []
                for columns in range(self.tiles.get_columns()):
                    current_color = self.colors_table[self.tiles.get_button(rows, columns).cget("bg")]
                    map_row.append(current_color)

                map_table.append(map_row)

            # Save the file to the selected path with the good format
            table_str = grid.convert_to_str(map_table)
            with open(file + ".mapdata", 'w') as file:
                file.write(table_str)

    # Method: reset_handler
    # Purpose: Reset the map to the default state (blank with only black border)
    def reset_handler(self):
        # Reset the tiles
        self.tiles.reset_tiles()

    # Method: back_handler
    # Purpose: Close the window
    def back_handler(self):
        self.window.destroy()
        main_frame: MainFrame = MainFrame.MainFrame("Smart City Rumble - Menu Principal", "400x100")
        main_frame.show()

    # Method: show
    # Purpose: Show the window
    def show(self):
        # Show top & bottom menu
        self.bottom_menu()
        self.upper_menu()

        # Show main menu
        self.window.mainloop()
