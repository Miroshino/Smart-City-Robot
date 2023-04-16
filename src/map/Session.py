# Import(s)
import random

import game.Agent as Agent
import game.ChargeStation as ChargeStation
import game.Point as Point
import game.Team as Team
import gui.GameFrame as GameFrame


# Session Class
class Session:
    # Constructor method
    def __init__(self, game_frame: GameFrame):
        # Game frame
        self.game_frame = game_frame
        self.window = game_frame.window

        # Variable(s)
        self.delivery_points = []
        self.storage_points = []
        self.charge_stations_points = []
        self.current_agents = {"blue": [], "red": []}
        self.agents = []
        self.started = False
        self.spawn_amount = 0
        self.buttons = game_frame.get_tiles().get_buttons()
        self.rows = game_frame.get_tiles().get_rows()
        self.columns = game_frame.get_tiles().get_columns()
        self.distance = 5
        self.blue_team = None
        self.red_team = None

    # Getters
    def get_delivery_points(self):
        return self.delivery_points

    def get_storage_points(self):
        return self.storage_points

    def get_charge_stations_points(self):
        return self.charge_stations_points

    def get_current_agents(self):
        return self.current_agents

    def get_agents(self):
        return self.agents

    def get_team_current_agents(self, team: str):
        return self.current_agents[team]

    def get_game_frame(self):
        return self.game_frame

    def get_window_game_frame(self):
        return self.window

    # Method(s)
    # Method: add_delivery_point
    # Purpose: Add a delivery point to the list
    def add_delivery_point(self, color: str, position: tuple):
        delivery_point = Point.Point("delivery_point", position, color)
        self.delivery_points.append(delivery_point)

    # Method: add_storage_point
    # Purpose: Add a storage point to the list
    def add_storage_point(self, color: str, position: tuple):
        storage_point = Point.Point("storage_point", position, color)
        self.storage_points.append(storage_point)

    # Method: add_charge_station_point
    # Purpose: Add a charge station point to the list
    def add_charge_station_point(self, position: tuple):
        charge_station_point = ChargeStation.ChargeStation(False, position)
        self.charge_stations_points.append(charge_station_point)

    # Method: add_agent
    # Purpose: Add an agent to the list
    def add_agent(self, team: str, agent: Agent):
        self.current_agents[team].append(agent)
        self.agents.append(agent)

    # Method: generate_points
    # Purpose: Generate every points (delivery points, storage points)
    # Addition: Every points will be generated randomly
    def generate_points(self, amount: int):
        # Check if the game has started
        if self.started:
            return

        # Variable(s)
        self.started = True
        buttons = [button for button in self.buttons if button.cget("bg") == "white"]
        num_delivery_points = 0
        num_storage_points = 0
        num_charge_station_points = 0

        # Create x amount of delivery points
        while num_delivery_points < amount:
            # Check if there are no more buttons available to create delivery points
            if not buttons:
                # Reset the delivery points
                self.delivery_points = []
                num_delivery_points = 0

            # Get the random button
            button = random.choice(buttons)

            # Check if the button is not a delivery point
            if button not in self.delivery_points:
                # Add the delivery point
                self.add_delivery_point("orange", (button.grid_info()["row"], button.grid_info()["column"]))
                button.configure(bg="orange", text="D")
                num_delivery_points += 1

        # Create x amount of storage points
        while num_storage_points < amount:
            # Check if there are no more buttons available to create storage points
            if not buttons:
                # Reset the storage points
                self.storage_points = []
                num_storage_points = 0

            # Get the random button
            button = random.choice(buttons)

            # Check if the button is not a storage point
            if button not in self.storage_points:
                # Add the storage point
                self.add_storage_point("chocolate", (button.grid_info()["row"], button.grid_info()["column"]))
                button.configure(bg="chocolate", text="S")
                num_storage_points += 1

        # Create x amount of charging stations
        while num_charge_station_points < amount:
            # Check if there are no more buttons available to create charge stations
            if not buttons:
                # Reset the charge stations
                self.charge_stations_points = []
                num_charge_station_points = 0

            # Get the random button
            button = random.choice(buttons)

            # Check if the button is not a charge station
            if button not in self.charge_stations_points:
                # Add the charge station
                self.add_charge_station_point((button.grid_info()["row"], button.grid_info()["column"]))
                button.configure(bg="yellow", text="C")
                num_charge_station_points += 1

    # Method: generate_agents
    # Purpose: Generate every agents randomly and they must be separated
    def generate_agents(self, amount: int):
        # Check if the game has started
        if not self.started:
            return

        # Variable(s)
        buttons = [button for button in self.buttons if button.cget("bg") == "white"]
        num_agents = 0
        default_battery = 100
        i = 0

        # Create x amount of agents
        while num_agents < amount:
            # Choose a random button
            button = random.choice(buttons)
            separated = True

            # Check if the button is self.distance away from every agents
            for team in self.current_agents:
                for agent in self.current_agents[team]:
                    # Variable(s)
                    abs_row = abs(button.grid_info()["row"] - agent.get_position()[0])
                    abs_column = abs(button.grid_info()["column"] - agent.get_position()[1])

                    # Check
                    if abs_row <= self.distance and abs_column <= self.distance:
                        separated = False
                        break

            # Check if the button is separated
            if separated:
                if i % 2 == 0:
                    color = "red"
                else:
                    color = "blue"

                # Add the agent
                agent = Agent.Agent(default_battery, 0, "storage",
                                    (button.grid_info()["row"], button.grid_info()["column"]), 2, color)
                self.add_agent(color, agent)
                button.configure(bg=color, text=agent.get_battery(), fg="white")

                # Configure team
                self.blue_team = Team.Team("blue", 0, self.get_team_current_agents("blue"))
                self.red_team = Team.Team("red", 0, self.get_team_current_agents("red"))

                num_agents += 1
                i += 1
