from ship import Ship


class Player:
   
    def __init__(self):
       
        self.ships = []
        self.search = ["N" for i in range(100)]
        self.place_ships(sizes=[4, 3, 3, 2, 2, 1])
        list_of_lists = [ship.indexes for ship in self.ships]
        self.indexes = [index for sublist in list_of_lists for index in sublist]

    def place_ships(self, sizes: [int]) -> None:
        
        for size in sizes:
            placed = False
            while not placed:
                # create a new ship
                ship = Ship(size)
                # check if placement possible
                placement_possible = True
                for i in ship.indexes:
                    # indexes must be less 100
                    if i >= 100:
                        placement_possible = False
                        break

                    # ships cannot be "snake"
                    new_row = i // 10
                    new_col = i % 10
                    if new_row != ship.row and new_col != ship.col:
                        placement_possible = False
                        break

                    # ships cannot intersect
                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            placement_possible = False
                            break

                    # ships must have a distance between each other
                    for other_ship in self.ships:
                        neighbor_indexes = [i-11, i-10, i-9, i-1, i, i+1, i+9, i+10, i+11]
                        if any(item in other_ship.indexes for item in neighbor_indexes):
                            placement_possible = False
                            break

                # add ships if possible
                if placement_possible:
                    self.ships.append(ship)
                    placed = True

    def show_ships(self) -> None:
       
        indexes = ["-" if i not in self.indexes else "X" for i in range(100)]
        for row in range(10):
            print(" ".join(indexes[(row - 1) * 10: row * 10]))
