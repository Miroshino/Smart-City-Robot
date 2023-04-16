# Import(s)
import time

import map.Tiles as Tiles


# Agent Class
class Agent:
    # Constructor method
    def __init__(self, battery: int = 10, points: int = 0, mission: str = "Delivery", position = (0, 0), speed: int = 1, color: str = "blue"):
        self.battery = battery
        self.points = points
        self.mission = mission
        self.position = position
        self.speed = speed
        self.color = color
        self.is_moving = False
        self.move_positions = []

        self.target_position = None

    # Getters
    def get_battery(self): return self.battery
    def get_points(self): return self.points
    def get_mission(self): return self.mission
    def get_position(self): return self.position
    def get_speed(self): return self.speed
    def get_target_position(self): return self.target_position
    def get_color(self): return self.color
    def get_is_moving(self): return self.is_moving
    def get_move_positions(self): return self.move_positions

    # Setters
    def set_battery(self, battery): self.battery = battery
    def set_points(self, points): self.points = points
    def set_mission(self, mission): self.mission = mission
    def set_position(self, position): self.position = position
    def set_speed(self, speed): self.speed = speed
    def set_target_position(self, target_position): self.target_position = target_position
    def set_color(self, color): self.color = color
    def set_is_moving(self, is_moving): self.is_moving = is_moving
    def set_move_positions(self, move_positions): self.move_positions = move_positions

    # Method(s)
    # Method: move
    # Purpose: Move the agent to positions in the list, one by one
    def move(self, tiles: Tiles):
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
            nonlocal current_position
            nonlocal move_positions

            # Change the color of the previous button and hide the text
            tiles.get_button(current_position[0], current_position[1]).configure(
                bg="white",
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
                    tiles.get_button(position[0], position[1]).configure(
                        bg="white",
                        text=""
                    )
                else:
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
                    tiles.get_button(current_position[0], current_position[1]).configure(
                        bg="white",
                        text=""
                    )

                # Change the color of the final position and show the text
                tiles.get_button(self.get_position()[0], self.get_position()[1]).configure(
                    bg=self.get_color(),
                    text=self.get_battery(),
                    fg="white"
                )

                # Change is_moving to False
                self.set_is_moving(False)

        # Schedule the first move to occur after 1 second
        tiles.window.after(int(1000 / self.get_speed()), move_to_next_position)

