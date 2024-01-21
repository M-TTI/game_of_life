import pygame


class Tile:

    def __init__(self, size, x, y):
        self.size = size
        self.living = False
        self.x = x
        self.y = y


    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getliving(self):
        return self.living

    def setliving(self):
        self.living = not self.living

    def getsize(self):
        return self.size


def init_grid(width, height, size_tile):
    grid = [[]]
    for x in range(width):
        for y in range(height):
            grid[x * size_tile][y * size_tile] = Tile(size_tile, x, y)


def draw_grid(grid_list):
    pass


pygame.init()
screen = pygame.display.set_mode((200, 100))
