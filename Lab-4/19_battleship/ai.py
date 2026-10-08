import random


class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.targets = []

    def choose(self):
        while self.targets:
            pos = self.targets.pop(0)

            if pos not in self.tried:
                self.tried.add(pos)
                return pos

        options = [
            (r, c)
            for r in range(self.size)
            for c in range(self.size)
            if (r, c) not in self.tried
        ]

        if not options:
            return None

        pos = random.choice(options)
        self.tried.add(pos)
        return pos

    def record_result(self, pos, hit):
        if not hit:
            return

        r, c = pos

        neighbours = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        for neighbour in neighbours:
            nr, nc = neighbour

            if (
                0 <= nr < self.size
                and 0 <= nc < self.size
                and neighbour not in self.tried
                and neighbour not in self.targets
            ):
                self.targets.append(neighbour)