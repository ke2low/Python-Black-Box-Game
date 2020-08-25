# Author: Kalvin Low
# Date: 08/03/2020
# Description: A program that allows the player to play
# the Black Box game.

class BlackBoxGame:
    """
    Represents a new instance of a Black Box game. Allows the user to
    place atoms on the board, shoot rays, guess the location of the atoms,
    check the number of atoms remaining not yet found and check the current
    game score. Will also keep track of the user's past guesses and the entry
    and exit squares of the rays fired, to adjust the score accordingly. This
    class does not communicate with any other classes.
    """
    def __init__(self, atom_locations):
        self._atom_locations = atom_locations
        self._current_score = 25
        self._atoms_left = len(atom_locations)
        self._past_guesses = []
        self._past_entry_exit_squares = []
        self._board = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", "x", "x", "x", "x", "x", "x", "x", "x", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        ]

        for coordinate in self._atom_locations:
            self._board[coordinate[0]][coordinate[1]] = "O"

    def get_board(self):
        """
        Prints the board to the console
        """
        for row in self._board:
            print(row)

    def set_board_entry_exit(self, row, column):
        """
        Takes a row and column parameter and adds an H marker to the board at
        that location to represent an entry or exit square
        """
        self._board[row][column] = "H"

    def get_atom_locations(self):
        """
        Returns the atom locations
        """
        return self._atom_locations

    def get_past_guesses(self):
        """
        Returns an array of past guesses
        """
        return self._past_guesses

    def guess_atom(self, row, column):
        """
        Allows user to guess an atom location by taking in a row and column
        parameter. Keeps a record of past guesses. Will decrease the number of atoms
        left if there is an atom located at the given location and return True.
        Otherwise, will lower the score by 5 points and return False. Adjusts the
        player's score accordingly.
        """
        if self._board[row][column] == "O":
            if [row, column] not in self._past_guesses:
                self.set_past_guesses(row, column)
                self._atoms_left -= 1
            return True
        else:
            if [row, column] not in self._past_guesses:
                self.set_past_guesses(row, column)
                self.set_score(-5)
            return False

    def check_valid_ray(self, row, column):
        """
        Takes a row and column parameter and checks if a ray can be fired at
        the given location on the board. If a ray can be fired, returns True.
        Otherwise returns False.
        """
        corner_squares = [[0, 0], [0, 9], [9, 0], [9, 9]]
        for square in corner_squares:
            if [row, column] == square:
                return False
        if (0 < row < 9) and (0 < column < 9):
            return False
        return True

    def set_past_guesses(self, row, column):
        """
        Takes a row and column parameter and adds the location to the
        past_guesses array
        """
        self._past_guesses.append([row, column])

    def atoms_left(self):
        """
        Returns the number of atoms left on the board
        """
        return self._atoms_left

    def get_score(self):
        """
        Returns the current score
        """
        return self._current_score

    def set_score(self, points):
        """
        Takes a points parameter and modifies the current score
        """
        self._current_score += points

    def set_past_entry_exit_squares(self, row, column):
        """
        Takes a row and column parameter and adds the location to the
        past_entry_exit_squares array
        """
        self._past_entry_exit_squares.append((row, column))

    def get_past_entry_exit_squares(self):
        """Returns the past_entry_exit_squares array"""
        return self._past_entry_exit_squares

    def check_direction(self, row, column):
        """
        Takes a row and column parameter, and checks the direction of a ray fired
        from that location. Returns a string representing the direction the ray is
        fired.
        """
        if row == 0:
            return "down"
        elif row == 9:
            return "up"
        elif column == 0:
            return "right"
        elif column == 9:
            return "left"

    def move(self, row, column, direction):
        """
        Takes a row, column and direction parameter and increments the row
        or column depending on which direction if provided. Returns the
        incremented row and column variables inside an array.
        """
        if direction == "down":
            row += 1
        elif direction == "up":
            row -= 1
        elif direction == "left":
            column -= 1
        elif direction == "right":
            column += 1
        return [row, column]

    def detect_hit(self, row, column, direction):
        """
        Takes a row, column and direction parameter and checks if a hit has been
        detected if a ray is fired from that location in the given direction.
        Returns True if a hit has been detected, but False otherwise.
        """
        if direction == "left":
            if self._board[row][column - 1] == "O":
                return True
            else:
                return False
        elif direction == "right":
            if self._board[row][column + 1] == "O":
                return True
            else:
                return False
        elif direction == "down":
            if self._board[row + 1][column] == "O":
                return True
            else:
                return False
        elif direction == "up":
            if self._board[row - 1][column] == "O":
                return True
            else:
                return False

    def detect_deflection(self, row, column, direction):
        """
        Takes a row, column and direction parameter and checks if a deflection has
        been detected if a ray is fired from that location in the given direction.
        Returns True if a deflection is detected, but False otherwise.
        """
        if direction == "left":
            if self._board[row + 1][column - 1] == "O" or self._board[row - 1][column - 1] == "O":
                return True
            else:
                return False
        elif direction == "right":
            if self._board[row + 1][column + 1] == "O" or self._board[row - 1][column + 1] == "O":
                return True
            else:
                return False
        elif direction == "down":
            if self._board[row + 1][column - 1] == "O" or self._board[row + 1][column + 1] == "O":
                return True
            else:
                return False
        elif direction == "up":
            if self._board[row - 1][column - 1] == "O" or self._board[row - 1][column + 1] == "O":
                return True
            else:
                return False

    def detect_reflection(self, row, column, direction):
        """
        Takes a row, column and direction parameter and checks if a reflection has been
        detected if a ray is fired from that location in the given direction.
        Returns True if a reflection is detected, but False otherwise.
        """
        if direction == "left":
            if self._board[row + 1][column - 1] == "O" and self._board[row - 1][column - 1] == "O":
                return True
            else:
                return False
        elif direction == "right":
            if self._board[row + 1][column + 1] == "O" and self._board[row - 1][column + 1] == "O":
                return True
            else:
                return False
        elif direction == "down":
            if self._board[row + 1][column - 1] == "O" and self._board[row + 1][column + 1] == "O":
                return True
            else:
                return False
        elif direction == "up":
            if self._board[row - 1][column - 1] == "O" and self._board[row - 1][column + 1] == "O":
                return True
            else:
                return False

    def get_deflected_direction(self, row, column, direction):
        """
        Takes a row, column and direction parameter and returns the deflected
        direction of the ray shot from that location at the given direction.
        Returns a string representing the direction the ray is deflected.
        """
        if direction == "left":
            if self._board[row + 1][column - 1] == "O":
                return "up"
            elif self._board[row - 1][column - 1] == "O":
                return "down"
        elif direction == "right":
            if self._board[row + 1][column + 1] == "O":
                return "up"
            elif self._board[row - 1][column + 1] == "O":
                return "down"
        elif direction == "down":
            if self._board[row + 1][column - 1] == "O":
                return "right"
            elif self._board[row + 1][column + 1] == "O":
                return "left"
        elif direction == "up":
            if self._board[row - 1][column - 1] == "O":
                return "right"
            elif self._board[row - 1][column + 1] == "O":
                return "left"

    def get_opposite_direction(self, direction):
        """
        Takes a parameter called direction which is a string representing
        the current direction of the ray and returns a string representing
        the opposite direction.
        """
        if direction == "left":
            return "right"
        elif direction == "right":
            return "left"
        elif direction == "up":
            return "down"
        elif direction == "down":
            return "up"

    def detect_border_atom(self, row, column, direction):
        """
        Takes a row, column and direction parameter and checks if atoms have been
        detected in the row or column of the board directly in front of the
        location of the ray being fired. If an atom has been detected directly in
        front of or in the squares diagonal to the location provided, returns True,
        otherwise returns False.
        """
        if direction == "left":
            if self._board[row][column - 1] == "O" or self._board[row + 1][column - 1] == "O" or \
                    self._board[row - 1][column - 1] == "O":
                return True
            else:
                return False
        elif direction == "right":
            if self._board[row][column + 1] == "O" or self._board[row + 1][column + 1] == "O" or \
                    self._board[row - 1][column + 1] == "O":
                return True
            else:
                return False
        elif direction == "down":
            if self._board[row + 1][column] == "O" or self._board[row + 1][column - 1] == "O" or \
                    self._board[row + 1][column + 1] == "O":
                return True
            else:
                return False
        elif direction == "up":
            if self._board[row - 1][column] == "O" or self._board[row - 1][column - 1] == "O" or \
                    self._board[row - 1][column + 1] == "O":
                return True
            else:
                return False

    def find_exit(self, row, column, direction="", started=False):
        """
        Takes a row and column parameter for the location of the entry square that a
        ray will be fired from and traverses the board to see if there is an exit square.
        If there is an exit square, it returns a tuple of the row and column of the exit
        square, but returns None otherwise.
        """
        if direction == "":
            direction = self.check_direction(row, column)
        if not started and not self.detect_border_atom(row, column, direction):
            row = self.move(row, column, direction)[0]
            column = self.move(row, column, direction)[1]
            started = True
        elif not started and self.detect_border_atom(row, column, direction):
            return None
        while row != 0 and row != 9 and column != 9 and column != 0:
            if not (self.detect_hit(row, column, direction) and
                    self.detect_deflection(row, column, direction)):
                row = self.move(row, column, direction)[0]
                column = self.move(row, column, direction)[1]
            if row == 0 or row == 9 or column == 9 or column == 0:
                return (row, column)
            if self.detect_hit(row, column, direction):
                return None
            if self.detect_deflection(row, column, direction):
                if self.detect_reflection(row, column, direction):
                    return self.find_exit(row, column, self.get_opposite_direction(direction))
                return self.find_exit(row, column, self.get_deflected_direction(row, column, direction))
        return (row, column)

    def shoot_ray(self, row, column):
        """
        Takes a row and column parameter for the location of the entry square that a ray will
        be fired. If the chosen row and column designates a corner square or a non-border square,
        it should return False. Otherwise, it returns a tuple of the row and column of the exit
        border square if there is one. Otherwise if there is no exit border square, returns None.
        Adjusts the player's score accordingly.
        """
        if not self.check_valid_ray(row, column):
            return False
        else:
            if (row, column) not in self.get_past_entry_exit_squares():
                self.set_score(-1)
                self.set_past_entry_exit_squares(row, column)
            coordinates = self.find_exit(row, column)
            if coordinates is None:
                if (row, column) not in self.get_past_entry_exit_squares():
                    self.set_score(-1)
                self.set_board_entry_exit(row, column)
                return None
            if coordinates not in self.get_past_entry_exit_squares() and coordinates is not None:
                self.set_score(-1)
                self.set_past_entry_exit_squares(coordinates[0], coordinates[1])
                self.set_board_entry_exit(coordinates[0], coordinates[1])

            self.set_board_entry_exit(coordinates[0], coordinates[1])
            return coordinates