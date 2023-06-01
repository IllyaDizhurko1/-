import pygame
from player import Player

#variables of different colors in rgb
GREY = (64, 64, 64)
BLACK = (0,0,0,)
BLUE = (0, 102, 204)
ORANGE = (250, 140, 20)
NAVY = (0, 0, 128)
COLORS = {"U": GREY, "M": BLUE, "H": ORANGE, "N": NAVY, "B": BLACK}


class Window:
   
    def __init__(self):
       
        self.cell_size = 35
        self.h_margin = self.cell_size * 4
        self.v_margin = self.cell_size
        self.width = self.cell_size * 10 * 2 + self.h_margin
        self.height = self.cell_size * 10 * 2 + self.v_margin
        self.my_font = None
        self.screen = pygame.display.set_mode((self.width, self.height))


    def create_window(self):
       
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Морський бій")

    def draw_grid(self, player: Player, left=0, top=0, search=False):
    
        for i in range(100):

            #take the position of the current cell
            x = left + i % 10 * self.cell_size
            y = top + i // 10 * self.cell_size

            #draw the cell
            cell = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, BLACK, cell, width=2)

            #check if this grid is for searching
            if search:
                x += self.cell_size // 2
                y += self.cell_size // 2
                pygame.draw.circle(self.screen, COLORS[player.search[i]], (x, y), radius=self.cell_size // 4)

    def draw_ships(self, player, left=0, top=0):
       
        for ship in player.ships:

            #take the position of the ship
            x = left + ship.col * self.cell_size + 10
            y = top + ship.row * self.cell_size + 10

            #check the ship's orientation
            if ship.orientation == 'h':
                width = ship.size * self.cell_size - 2 * 10
                height = self.cell_size - 2 * 10
            else:
                width = self.cell_size - 2 * 10
                height = ship.size * self.cell_size - 2 * 10

            #draw the ship on the grid
            rectangle = pygame.Rect(x, y, width, height)
            pygame.draw.rect(self.screen, BLACK, rectangle, border_radius=15)

