class Square:

    # Mapping of column indices to corresponding letters
    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd',
                 4: 'e', 5: 'f', 6: 'g', 7: 'h', }

    def __init__(self, row, col, piece=None):
        # Initialize Square object with row and column coordinates, and optional piece
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]

    def __eq__(self, other):
        # Check if two Square objects have the same row and column coordinates
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        # Check if Square object has a piece on it
        return self.piece != None

    def isempty(self):
        # Check if Square object is empty (i.e. no piece on it)
        return not self.has_piece()

    def has_team_piece(self, color):
        # Check if Square object has a piece on it with the given color
        return self.has_piece() and self.piece.color == color

    def has_enemy_piece(self, color):
        # Check if Square object has a piece on it with a different color than the given color
        return self.has_piece() and self.piece.color != color

    def isempty_or_enemy(self, color):
        # Check if Square object is empty or has a piece with a different color than the given color
        return self.isempty() or self.has_enemy_piece(color)

    @staticmethod
    def in_range(*args):
        # Check if given arguments (row or column indices) are within the valid range of 0 to 7
        for arg in args:
            if arg < 0 or arg > 7:
                return False
            
        return True

    @staticmethod
    def get_alphacol(col):
        # Get the alphabetic representation of the given column index
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd',
                     4: 'e', 5: 'f', 6: 'g', 7: 'h', }
        return ALPHACOLS[col]
