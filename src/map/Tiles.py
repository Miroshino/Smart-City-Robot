# Import(s)
import tkinter as tk
import gui.GameFrame as GameFrame
import map.Map as Map


# Tiles Class
class Tiles:
    # Constructor method
    def __init__(self, game_frame: GameFrame):
        self.columns = 28
        self.rows = 20
        self.buttons = []

        self.map = Map.Map(self.get_buttons())
        self.window = game_frame.window

        # Create bottom & upper game_frame variables
        self.upper_frame = game_frame.get_upper_menu()

    # Getters
    # Method: get_buttons
    # Purpose: Return the buttons
    def get_buttons(self):
        return self.buttons

    # Method: get_rows
    # Purpose: Return the number of rows
    def get_rows(self):
        return self.rows

    # Method: get_columns
    # Purpose: Return the number of columns
    def get_columns(self):
        return self.columns

    # Method(s)
    # Method: generate_tiles
    # Purpose: Generate tiles in the upper menu
    def generate_tiles(self):
        # Create a button grid
        for row in range(self.get_rows()):
            for column in range(self.columns):
                # Create a button
                button = tk.Button(self.upper_frame, text="", bg="white", width=2, height=1,
                                   command=lambda button_id=(row, column): self.button_handler(button_id))
                button.grid(row=row, column=column)
                self.buttons.append(button)

        # Get the map table
        self.map.convert_to_table('data/map_1.txt')
        map_table = self.map.get_map_table()

        # Change the color of the buttons according to the map table numbers
        for row in range(self.get_rows()):
            for column in range(self.columns):
                # Border limit of the grid in red
                if row == 0 or row == self.rows - 1 or column == 0 or column == self.columns - 1:
                    self.buttons[row * self.columns + column].configure(bg="black")

                self.buttons[row * self.columns + column].configure(bg=self.map.get_number_color(map_table[row][column]))

    # Method: reset_tiles
    # Purpose: Reset the tiles to their default state
    def reset_tiles(self):
        for button in self.buttons:
            if button.cget("bg") != "black":
                button.configure(bg="white")

    # Method: button_handler
    # Purpose: Handle the button click event
    def button_handler(self, button_id):
        # id is a tuple (row, column) containing the position of the clicked button
        row, column = button_id

        # Get the index of the button in the buttons list
        index = row * self.columns + column

        # Change the button color to red if not black and if red then change it to white
        if self.buttons[index].cget("bg") == "white":
            self.buttons[index].configure(bg="red")
        elif self.buttons[index].cget("bg") == "red":
            self.buttons[index].configure(bg="white")
