# Import(s)
import tkinter as tk
import gui.GameFrame as GameFrame
import gui.MapEditorFrame as MapEditorFrame


# Frame Class
class MainFrame:
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

        # Buttons
        self.play_button = tk.Button(self.window, text="Jouer", command=self.play_button_handler, width=55, height=2)
        self.play_button.pack(pady=10)

        self.map_editor_button = tk.Button(self.window, text="Éditeur de carte", command=self.map_editor_button_handler, width=55, height=2)
        self.map_editor_button.pack(pady=10)

        # Place buttons
        self.play_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        self.map_editor_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    # Method: play_button_handler
    # Purpose: Handle the play button
    def play_button_handler(self):
        print("Play button pressed")
        # Destroy the main menu
        self.window.destroy()

    # Method: map_editor_button_handler
    # Purpose: Handle the map editor button
    def map_editor_button_handler(self):
        # Destroy the main menu
        self.window.destroy()

        # Show the MapEditorFrame
        map_editor_frame = MapEditorFrame.MapEditorFrame("Smart City Rumble - Éditeur de carte", "672x587")
        map_editor_frame.show()

    # Method: show
    # Purpose: Show the window
    def show(self):
        # Show main menu
        self.window.mainloop()
