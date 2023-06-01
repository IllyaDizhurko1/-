from player import Player
from random import choice


class Game:
   
    def __init__(self, human1: bool, human2: bool):
    
        self.human1 = human1
        self.human2 = human2
        self.player1 = Player()
        self.player2 = Player()
        self.player1_turn = True
        self.over = False
        self.result = None

    def make_move(self, index: int) -> None:
        
        player = self.player1 if self.player1_turn else self.player2
        opponent = self.player2 if self.player1_turn else self.player1
        hit = False

        #check if our cell contains a part of a ship
        if index in opponent.indexes:
            player.search[index] = "H"
            hit = True


            for ship in opponent.ships:
                sunk = True
                for index in ship.indexes:
                    if player.search[index] == "N":
                        sunk = False
                        break
                #check if the ship is sunk
                if sunk:
                    for index in ship.indexes:
                        player.search[index] = "B"
                        list_indexes = [index - 11, index - 10, index - 9, index - 1, index + 1, index + 9, index + 10, index + 11]
                        if index in range(0, 10):
                            del list_indexes[0:3]
                        if index in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]:
                            if index - 11 in list_indexes:
                                list_indexes.remove(index - 11)
                            list_indexes.remove(index - 1)
                            list_indexes.remove(index + 9)
                        if index in [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]:
                            if index - 9 in list_indexes:
                                list_indexes.remove(index - 9)
                            list_indexes.remove(index + 1)
                            list_indexes.remove(index + 11)
                        if index in [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]:
                            if index + 9 in list_indexes:
                                list_indexes.remove(index + 9)
                            list_indexes.remove(index + 10)
                            if index + 11 in list_indexes:
                                list_indexes.remove(index + 11)
                        for j in list_indexes:
                            if j in range(0, 101) and j not in ship.indexes:
                                player.search[j] = "M"
        # if it doesn't contain a part of the ship
        else:
            player.search[index] = "M"

        #check if the game is over
        game_over = True
        for index in opponent.indexes:
            if player.search[index] == "N":
                game_over = False
        self.over = game_over
        self.result = 1 if self.player1_turn else 2

        #if the player doesn't hit any ship
        if not hit:
            self.player1_turn = not self.player1_turn
