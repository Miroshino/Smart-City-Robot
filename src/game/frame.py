# Imports
import tkinter as tk


# Frame class
class Frame:
    # Construct (init)
    def __init__(self, title, size):
        self.title: str = title
        self.size: str = size

    # Show func
    def show(self):
        # Frame
        Game_Frame: tk = tk.Tk()
        Game_Frame.geometry(self.size)
        Game_Frame.title(self.title)
        Game_Frame.resizable(False, False)

        # Board
        Game_Board: tk = tk.Frame(Game_Frame, width=350, height=350)

        # Show the frame
        Game_Board.pack(padx=10, pady=25)
        Game_Frame.mainloop()

