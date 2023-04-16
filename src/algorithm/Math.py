# Math Class
class Math:
    # Method(s)
    # Method: heuristic
    # Purpose: Calculate the heuristic in manhattan distance
    @staticmethod
    def heuristic(a_pos: tuple, b_pos: tuple):
        # Return the heuristic
        return abs(a_pos[0] - b_pos[0]) + abs(a_pos[1] - b_pos[1])

    # Method: get_distance
    # Purpose: Calculate the distance between two points euclidean distance
    @staticmethod
    def get_distance(a_pos: tuple, b_pos: tuple):
        # Return the distance
        return ((a_pos[0] - b_pos[0]) ** 2 + (a_pos[1] - b_pos[1]) ** 2) ** 0.5
