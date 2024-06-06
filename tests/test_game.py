import pytest
from longest_word.game import Game

class TestGame:
    def test_game_initialization(self):
        # setup
        new_game = Game()
        new_grid = new_game.grid
        assert type(new_grid) == list, "Grid must be list type"
        assert len(new_grid) == 9, "Grid must be length 9"
        assert all(i.isalpha() and i.isascii() and i.isupper() for i in new_grid), "Grid must contain only English capital letters."

    def test_func_is_valid(self):
        #setup
        new_game = Game()
        test_grid = "OQUWRBAZE"
        test_longest_word = "BAROQUE"
        test_failed_word = "bower" # lower case. Only test if the letters are within grid
        new_game.grid = list(test_grid)
        assert new_game.is_valid(test_longest_word) == True, "The longest word is not right"
        assert new_game.grid == list(test_grid), "Make sure the grid does not get modified"
        assert new_game.is_valid(test_failed_word) == False, "This word is not the longest"
        assert new_game.is_valid("") == False, "Empty word is not allowed"

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
