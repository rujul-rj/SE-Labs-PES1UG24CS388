class Board:
    SIZE = 6

    def __init__(self):
        self.ships = []
        self.ship_hits = []
        self.shots = set()

    def place_ship(self, cells):
        ship = set(cells)
        self.ships.append(ship)
        self.ship_hits.append(set())

    def fire(self, pos):
        if pos in self.shots:
            return "already_shot", None

        self.shots.add(pos)

        for index, ship in enumerate(self.ships):
            if pos in ship:
                self.ship_hits[index].add(pos)

                if self.ship_hits[index] == ship:
                    return "sunk", index

                return "hit", index

        return "miss", None

    def ship_sunk(self, index):
        return self.ship_hits[index] == self.ships[index]

    def all_sunk(self):
        return all(self.ship_sunk(index) for index in range(len(self.ships)))