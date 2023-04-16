# Import(s)
from tkinter import messagebox

import algorithm.AStar as AStar
import map.Session as Session
import map.Tiles as Tiles


# Agent Class
class Agent:
    # Constructor method
    def __init__(self, battery: int = 10, points: int = 0, mission: str = "storage", position=(0, 0), speed: int = 1,
                 color: str = "blue"):
        # Attribute(s)
        self.battery = battery
        self.points = points
        self.mission = mission
        self.position = position
        self.speed = speed
        self.color = color

        # Variable(s)
        self.is_moving = False
        self.move_positions = []
        self.original_colors = {}
        self.target_position = None
        self.old_mission = None

    # Getters
    def get_battery(self):
        return self.battery

    def get_points(self):
        return self.points

    def get_mission(self):
        return self.mission

    def get_position(self):
        return self.position

    def get_speed(self):
        return self.speed

    def get_target_position(self):
        return self.target_position

    def get_color(self):
        return self.color

    def get_is_moving(self):
        return self.is_moving

    def get_move_positions(self):
        return self.move_positions

    # Setters
    def set_battery(self, battery):
        self.battery = battery

    def set_points(self, points):
        self.points = points

    def set_mission(self, mission):
        self.mission = mission

    def set_position(self, position):
        self.position = position

    def set_speed(self, speed):
        self.speed = speed

    def set_target_position(self, target_position):
        self.target_position = target_position

    def set_color(self, color):
        self.color = color

    def set_is_moving(self, is_moving):
        self.is_moving = is_moving

    def set_move_positions(self, move_positions):
        self.move_positions = move_positions

    # Method(s)
    # Method: move
    # Purpose: Move the agent to positions in the list, one by one
    def move(self, tiles: Tiles, session: Session):
        # Variable(s)
        move_positions = self.get_move_positions()
        current_position = move_positions[0]
        move_positions = move_positions[1:]

        # Change the color of the start position and hide the text
        tiles.get_button(current_position[0], current_position[1]).configure(
            bg=self.get_color(),
            text=self.get_battery(),
            fg="white"
        )

        # Define the function to move to the next position
        def move_to_next_position():
            # Variable(s)
            nonlocal current_position
            nonlocal move_positions

            # Check if the battery remaining is lower than the path length
            if self.get_battery() < len(move_positions):
                # Stop the movement
                self.set_is_moving(False)
                print("Agent: " + str(self.get_battery()) + " < " + str(len(move_positions)) + " = " + str(
                    self.get_battery() < len(move_positions)))
                return

            # Change the color of the previous button and hide the text
            tiles.get_button(current_position[0], current_position[1]).configure(
                bg=self.original_colors[current_position],
                text=""
            )

            # Get the next position
            next_position = move_positions[0]

            # Move to the next position
            self.set_position(next_position)
            current_position = next_position

            # Change color of the new button pos and hide the text of all other buttons
            for position in move_positions:
                if position != current_position:
                    '''
                    tiles.get_button(position[0], position[1]).configure(
                        bg=self.original_colors[position],
                        text=""
                    )
                    '''
                    pass
                else:
                    self.set_battery(self.get_battery() - 1)
                    tiles.get_button(position[0], position[1]).configure(
                        bg=self.get_color(),
                        text=self.get_battery(),
                        fg="white"
                    )

            # Remove the current position from the move_positions list
            move_positions = move_positions[1:]

            # If there are more positions, schedule the next move to occur after 1 second
            if len(move_positions) > 0:
                tiles.window.after(int(1000 / self.get_speed()), move_to_next_position)
            # If there are no more positions, change the color of the final position and show the text
            else:
                # Change the color of the last position and hide the text
                if current_position != self.get_position():
                    # Check if the button was red or blue before
                    '''
                    if self.original_colors[self.get_position()] == "red" or self.original_colors[self.get_position()] == "blue":
                        tiles.get_button(current_position[0], current_position[1]).configure(
                            bg="white",
                            text=""
                        )
                    else:
                        tiles.get_button(current_position[0], current_position[1]).configure(
                            bg=self.original_colors[current_position],
                            text=""
                        )
                    '''
                    tiles.get_button(current_position[0], current_position[1]).configure(
                        bg=self.original_colors[current_position],
                        text=""
                    )

                # Change the color of the final position and show the text
                tiles.get_button(self.get_position()[0], self.get_position()[1]).configure(
                    bg=self.get_color(),
                    text=self.get_battery(),
                    fg="white"
                )

                # If delivery, then add points based on the agent team (red or blue)
                if self.get_mission() == "storage":
                    # Check if the team red or blue won (50 pts)
                    if session.red_team.get_points() == 30:
                        messagebox.showinfo("Partie terminée", "L'équipe rouge a gagné la partie !")
                        session.get_game_frame().destroy()
                    elif session.blue_team.get_points() == 30:
                        messagebox.showinfo("Partie terminée", "L'équipe bleue a gagné la partie !")
                        session.get_game_frame().destroy()

                    # Check if the agent is red or blue
                    if self.get_color() == "red":
                        # Variable(s)
                        buttons = session.get_game_frame().buttons_bottom_frame

                        # Add points
                        session.red_team.add_points(1)
                        buttons[3].configure(text="Rouges: " + str(session.blue_team.get_points()) + " points")
                    else:
                        # Variable(s)
                        buttons = session.get_game_frame().buttons_bottom_frame

                        # Add points
                        session.blue_team.add_points(1)
                        buttons[2].configure(text="Bleus: " + str(session.blue_team.get_points()) + " points")

                # Change is_moving to False
                self.set_is_moving(False)

                # Get current mission and battery level
                mission = self.get_mission()
                battery = self.get_battery()

                # Next mission and move the agent
                if mission in ["storage", "delivery"]:
                    if battery <= 40:
                        self.set_mission("charging")
                        self.old_mission = mission
                    else:
                        self.set_mission("delivery" if mission == "storage" else "storage")
                elif mission == "charging" and battery >= 40:
                    self.set_mission(self.old_mission)

                # Move the agent
                a_star = AStar.AStar(tiles, self, session)
                path = a_star.find_path()
                self.set_move_positions(path)
                self.move(tiles, session)

        # Save the original colors of all buttons
        self.original_colors = {}
        for row in range(tiles.get_rows()):
            for column in range(tiles.get_columns()):
                button = tiles.get_button(row, column)
                if button.cget("bg") == "red" or button.cget("bg") == "blue":
                    self.original_colors[(row, column)] = "white"
                else:
                    self.original_colors[(row, column)] = button.cget("bg")

        # Schedule the first move to occur after 1 second
        tiles.window.after(int(1000 / self.get_speed()), move_to_next_position)
