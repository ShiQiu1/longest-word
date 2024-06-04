import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)
        #pass

    def is_valid(self, word):
        """Make sure the input word is not empty"""
        if not word:
            return False
        letters = self.grid.copy()
        """Make sure the input word does not have words outside the grid"""
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
