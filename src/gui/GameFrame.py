# Import(s)
import random as random
import tkinter as tk
from tkinter import messagebox

import algorithm.AStar as AStar
import gui.MainFrame as MainFrame
import map.Session as Session
import map.Tiles as Tiles
from map import Map


# GameFrame Class
class GameFrame:
    # Constructor method
    def __init__(self, title: str, size: str):
        # Attributes
        self.title = title
        self.size = size

        # Variable(s)
        self.agents_generated = 0

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
        self.buttons_bottom_frame = []
        self.upper_frame = tk.Frame(self.window, bg="black")

        # Create tile object
        self.tiles = Tiles.Tiles(self)
        self.tiles.set_current_color(1)
        self.tiles.set_current_frame("game")

        # Create session object
        self.session = Session.Session(self)

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
            ("Générer", self.generate_button_handler),
            ("Démarrer", self.simulate_button_handler),
            ("Bleus: 0 points", self.no_func),
            ("Rouges: 0 points", self.no_func),
            ("Retour", self.back_button_handler),
        ]

        # Add buttons to the frame using a for loop and automatically horizontal center them
        for text, handler in buttons:
            # Create a button
            button = tk.Button(self.bottom_frame, text=text, bg="white", width=15, height=2, command=handler)
            button.pack(side="left", padx=15, pady=13)

            # Add the button to the list of buttons
            self.buttons_bottom_frame.append(button)

            # Change the color of the button if it's a team button
            if text[:2] == "Bl" or text[:2] == "Ro":
                button.config(bg=text[:2] == "Bl" and "blue" or "red", fg="white")

    # Method: upper_menu
    # Purpose: Create a grid of buttons at the top of the window
    def upper_menu(self):
        # Create a black frame at the top of the window
        self.upper_frame.pack(side="top", fill="x")

        # Get all .mapdata files in the data folder
        maps = Map.Map().get_all_map_files()
        random_map = str(random.randint(0, len(maps) - 1))

        # Generate tiles
        # The selected map will be randomly generated with the maps variable
        self.tiles.generate_tiles("data/" + maps[int(random_map)])

    # Method: generate_button_handler
    # Purpose: Start the generation of the map
    def generate_button_handler(self):
        # Disable the generate button
        self.buttons_bottom_frame[0].config(state="disabled")

        # Generate points and agents
        self.session.generate_points(2)
        self.session.generate_agents(4)

        # AStar algorithm
        # For each agent, find the path to the closest storage point
        for team in self.session.get_current_agents():
            for agent in self.session.get_team_current_agents(team):
                # AStar algorithm
                agent.set_mission("storage")
                a_star = AStar.AStar(self.tiles, agent, self.session)
                path = a_star.find_path()
                agent.set_move_positions(path)

                # Increment the number of agents that have finished their path
                self.agents_generated += 1

    # Method: simulate_button_handler
    # Purpose: Simulate the movement of the agents
    def simulate_button_handler(self):
        # Disable the generate button
        self.buttons_bottom_frame[1].config(state="disabled")

        # Check if every agent(s) are ready to move
        if 0 < self.agents_generated <= len(self.session.get_agents()):
            print("Simulation started... Agents are ready to move.")

            # For each agent, move to the next position
            for team in self.session.get_current_agents():
                for agent in self.session.get_team_current_agents(team):
                    agent.move(self.tiles, self.session)
        else:
            messagebox.showerror("Démarrage impossible",
                                 "Veuillez d'abord générer les différents points de la carte.")

    # Method: no_func
    # Purpose: Do nothing
    def no_func(self):
        pass

    # Method: back_button_handler
    # Purpose: Go back to the main menu
    def back_button_handler(self):
        self.stop_game()

    # Method: stop_game
    # Purpose: Stop the game (delete the window and go back to the main menu)
    def stop_game(self):
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
