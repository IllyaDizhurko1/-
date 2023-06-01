import pygame
from game import Game
from window import Window
from argparse import ArgumentParser

#working with the terminal via argparse
parser = ArgumentParser()
parser.add_argument("-m", dest="game_mode", default="players", required=False)
args = parser.parse_args()

is_player1_human = True
is_player2_human = True
show_player1_ships = 1
NAVY = (0,0,128)


def main() -> None:
   
    #create the game window
    window = Window()
    window.create_window()
    window.my_font = pygame.font.SysFont("fresansttf", 100)
    game = Game(is_player1_human, is_player2_human)

    animating = True
    pausing = False

    pressed_cells_player1 = []
    pressed_cells_player2 = []

    #infinite loop
    while animating:
        #check for events
        for event in pygame.event.get():
            #check the QUIT event
            if event.type == pygame.QUIT:
                animating = False

            #check the KEYDOWN event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    animating = False
                if event.key == pygame.K_SPACE:
                    pausing = not pausing
                if event.key == pygame.K_RETURN:
                    game = Game(is_player1_human, is_player2_human)

            #check if user pressed the mouse button
            if event.type == pygame.MOUSEBUTTONDOWN and not game.over:
                x, y = pygame.mouse.get_pos()

                #check the rigtness of mouse clicking position for player1
                if game.player1_turn and x < window.cell_size * 10 and y < window.cell_size * 10:
                    row = y // window.cell_size
                    col = x // window.cell_size
                    index = row * 10 + col
                    if index not in pressed_cells_player1:
                        pressed_cells_player1.append(index)
                    else:
                        break
                    game.make_move(index)

                #check the rightness of mouse clicking position for player2
                elif not game.player1_turn and x > window.width - 10 * window.cell_size and y > window.height - 10 * window.cell_size:
                    row = (y - window.cell_size * 10 - window.v_margin) // window.cell_size
                    col = (x - window.cell_size * 10 - window.h_margin) // window.cell_size
                    index = row * 10 + col
                    if index not in pressed_cells_player2:
                        pressed_cells_player2.append(index)
                    else:
                        break
                    game.make_move(index)

        #check if the game isn't paused
        if not pausing:
            window.screen.fill(NAVY)

            #draw player1 grids
            window.draw_grid(game.player1, 10, 10, True)
            window.draw_grid(game.player1, (window.width - window.h_margin) // 2 + window.h_margin - 10, 10)

            #draw player2 grids
            window.draw_grid(game.player2, (window.width - window.h_margin) // 2 + window.h_margin - 10, (window.height - window.v_margin) // 2 + window.v_margin - 10, True)
            window.draw_grid(game.player2, 10, (window.height - window.v_margin) // 2 + window.v_margin - 10) 

            #check if the program should draw player1 ships
            if show_player1_ships:
                window.draw_ships(game.player1, 10, (window.height - window.v_margin) // 2 + window.v_margin - 10)
           
            #check if the game is over and we have a winner
            if game.over:
                text = "Player " + str(game.result) + " wins!"
                textbox = window.my_font.render(text, False, NAVY, (255, 255, 255))
                window.screen.blit(textbox, (window.width // 2 - 240, window.height // 2 - 50))

            #update the screen
            pygame.display.flip()


main()
