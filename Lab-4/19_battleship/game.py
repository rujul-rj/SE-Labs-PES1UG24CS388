from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        self.player.place_ship({(1, 1), (1, 2)})
        self.player.place_ship({(3, 3), (3, 4), (3, 5)})

        self.enemy.place_ship({(1, 1), (1, 2)})
        self.enemy.place_ship({(2, 2), (2, 3), (2, 4)})

    def show(self):
        print("\nYour shots are coordinates like 2,3.")

        remaining = sum(
            len(ship) - len(self.enemy.ship_hits[index])
            for index, ship in enumerate(self.enemy.ships)
        )

        print("Ship cells remaining:", remaining)

    def run(self):
        print("Battleship")

        while True:
            self.show()

            raw = input("> ").strip().lower()

            if raw == "q":
                return

            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)
            except ValueError:
                print("Use row,col.")
                continue

            if not (0 <= pos[0] < Board.SIZE and
                    0 <= pos[1] < Board.SIZE):
                print("Outside board.")
                continue

            result, ship_index = self.enemy.fire(pos)

            if result == "already_shot":
                print("Already fired there.")
                continue

            if result == "miss":
                print("MISS!")

            elif result == "hit":
                print("HIT!")
                print(f"Ship {ship_index + 1} hit.")

            elif result == "sunk":
                print("HIT!")
                print(f"Ship {ship_index + 1} sunk.")

            if self.enemy.all_sunk():
                print("You sank the entire fleet.")
                return

            ai_pos = self.ai.choose()

            if ai_pos is None:
                print("AI has no valid moves left.")
                return

            print(
                "AI fired at",
                f"{ai_pos[0] + 1},{ai_pos[1] + 1}"
            )

            ai_result, ai_ship_index = self.player.fire(ai_pos)

            if ai_result == "hit":
                print("AI HIT!")

            elif ai_result == "sunk":
                print(f"AI SUNK Ship {ai_ship_index + 1}!")

            elif ai_result == "miss":
                print("AI MISS!")

            self.ai.record_result(
                ai_pos,
                ai_result in ("hit", "sunk")
            )