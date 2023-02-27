# Imports
import tkinter as tk

# Square class
class Square:
    def __init__(self, parent, size, row, column):
        self.canvas = tk.Canvas(parent, width=size, height=size, bg='white')
        self.canvas.grid(row=row, column=column)


# Map Class
class Map:
    def __init__(self, parent, n=11 , size=80):
        self.parent = parent
        self.n = n
        self.size = size
        self.grid = []
        self.points = []

        # Creating the grid
        for i in range(n):
            row = []
            for j in range(n):
                square = Square(parent, size, i, j)
                row.append(square)
            self.grid.append(row)

        # Position the dots
        self.points.append((10, 0))
        self.points.append((0, 10))

        # Creating the two dots
        for i, (x, y) in enumerate(self.points):
            color = 'red' if i == 0 else 'blue'
            self.grid[x][y].canvas.create_oval(size // 4, size // 4, size // 4 * 3, size // 4 * 3, fill=color)


# Creating the window
root = tk.Tk()
root.title("Map")

# Creating the map
map = Map(root)

# Main Loop
root.mainloop()
