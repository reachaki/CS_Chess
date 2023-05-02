
class Move:

    def __init__(self, initial, final):
        # initial and final are squares
        self.initial = initial
        self.final = final

    def __str__(self):
        # Returns a string representation of the move.
        # Format: (initial col, initial row) -> (final col, final row)
        s = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    def __eq__(self, other):
        # Returns True if two moves have the same initial and final squares.
        return self.initial == other.initial and self.final == other.final
