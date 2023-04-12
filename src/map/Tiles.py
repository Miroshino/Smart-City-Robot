# Import(s)
import tkinter as tk

import gui.GameFrame as GameFrame
import map.Map as Map


# Tiles Class
class Tiles:
    # Constructor method
    def __init__(self, game_frame: GameFrame):
        # Variable(s)
        self.current_frame = None
        self.columns = 28
        self.rows = 20
        self.buttons = []
        self.current_color = "white"

        # Create map object
        self.map = Map.Map()
        self.map.set_tiles_list(self.get_buttons())
        self.window = game_frame.window

        # Create bottom & upper game_frame variables
        self.upper_frame = game_frame.get_upper_menu()

    # Getters
    # Method: get_buttons
    # Purpose: Return the buttons
    def get_buttons(self):
        return self.buttons

    # Method: get_button
    # Purpose: Return a specific button based on row and column
    def get_button(self, row: int, column: int):
        return self.buttons[row * self.columns + column]

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
    def generate_tiles(self, map_path: str):
        # Create a button grid
        for row in range(self.get_rows()):
            for column in range(self.columns):
                # Create a button
                button = tk.Button(self.upper_frame, text="", bg="white", width=2, height=1,
                                   command=lambda button_id=(row, column): self.button_handler(button_id))
                button.grid(row=row, column=column)
                self.buttons.append(button)

        # Get the map table
        self.map.convert_to_table(map_path)
        map_table = self.map.get_map_table()

        # Change the color of the buttons according to the map table numbers
        for row in range(self.get_rows()):
            for column in range(self.columns):
                # Border limit of the grid in red
                if row == 0 or row == self.rows - 1 or column == 0 or column == self.columns - 1:
                    self.buttons[row * self.columns + column].configure(bg="black")

                self.buttons[row * self.columns + column].configure(
                    bg=self.map.get_number_color(map_table[row][column]))

    # Method: generate_empty_tiles
    # Purpose: Generate empty tiles in the map editor with only the black border
    def generate_empty_tiles(self):
        # Create a button grid
        for row in range(self.get_rows()):
            for column in range(self.columns):
                # Create a button
                button = tk.Button(self.upper_frame, text="", bg="white", width=2, height=1,
                                   command=lambda button_id=(row, column): self.button_handler(button_id))
                button.grid(row=row, column=column)
                self.buttons.append(button)

        # Change the color of the buttons according to the map table numbers
        for row in range(self.get_rows()):
            for column in range(self.columns):
                # Border limit of the grid in red
                if row == 0 or row == self.rows - 1 or column == 0 or column == self.columns - 1:
                    self.buttons[row * self.columns + column].configure(bg="black")

    # Method: change_tiles_color
    # Purpose: Change the color of the tiles by using the map table
    def change_tiles_color(self, map_table: list):
        for row in range(self.get_rows()):
            for column in range(self.columns):
                self.buttons[row * self.columns + column].configure(
                    bg=self.map.get_number_color(map_table[row][column]))

    # Method: reset_tiles
    # Purpose: Reset the tiles to their default state
    def reset_tiles(self):
        for button in self.buttons:
            if button.cget("bg") != "black":
                button.configure(bg="white")

    # Method: get_map
    # Purpose: Return the map object
    def get_map(self):
        return self.map

    # Method: set_current_color
    # Purpose: Set the current color of the tile
    def set_current_color(self, color: int):
        print("Couleur choisie : " + str(color) + " - " + self.map.get_number_color(color) + "")
        self.current_color = self.map.get_number_color(color)

    # Method: button_handler
    # Purpose: Handle the button click event
    def button_handler(self, button_id):
        # If the current frame is the game then pass
        if self.current_frame == "game":
            return

        # id is a tuple (row, column) containing the position of the clicked button
        row, column = button_id

        # Get the index of the button in the buttons list
        index = row * self.columns + column

        # Change the button color to the current color except if the button is a border
        # And if the button is actually colored (not white) then change it to white
        if self.buttons[index].cget("bg") != "black":
            if self.buttons[index].cget("bg") == "white":
                self.buttons[index].configure(bg=self.current_color)
            elif self.buttons[index].cget("bg") == self.current_color:
                self.buttons[index].configure(bg="white")
            else:
                self.buttons[index].configure(bg=self.current_color)

    def set_current_frame(self, frame: str):
        self.current_frame = frame
