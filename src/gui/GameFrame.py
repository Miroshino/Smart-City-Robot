# Import(s)
import tkinter as tk
import map.Tiles as Tiles


# GameFrame Class
class GameFrame:
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
        width = self.window.winfo_width() # Get the window's width and height
        height = self.window.winfo_height() # Get the window's width and height
        x = (self.window.winfo_screenwidth() // 2) - (width // 2) - 50 # Center the window on the screen
        y = (self.window.winfo_screenheight() // 2) - (height // 2) - 50 # Center the window on the screen
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y)) # Set the window's position

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
            ("Démarrer", self.start_button_handler),
            ("Arrêter", self.stop_button_handler),
            ("Recommencer", self.restart_button_handler),
        ]

        # Add buttons to the frame using a for loop and automatically horizontal center them
        for text, handler in buttons:
            button = tk.Button(self.bottom_frame, text=text, bg="white", width=15, height=2, command=handler)
            button.pack(side="left", padx=55, pady=13)

    # Method: upper_menu
    # Purpose: Create a grid of buttons at the top of the window
    def upper_menu(self):
        # Create a black frame at the top of the window
        self.upper_frame.pack(side="top", fill="x")

        # Generate tiles
        self.tiles.generate_tiles()

    # Method: start_button_handler
    # Purpose: Start the generation of the map and the simulation
    def start_button_handler(self):
        pass

    # Method: stop_button_handler
    # Purpose: Stop the generation of the map and the simulation
    def stop_button_handler(self):
        pass

    # Method: restart_button_handler
    # Purpose: Change all buttons to white except the border limit
    def restart_button_handler(self):
        self.tiles.reset_tiles()

    # Method: show
    # Purpose: Show the window
    def show(self):
        # Show top & bottom menu
        self.bottom_menu()
        self.upper_menu()

        # Show main menu
        self.window.mainloop()
