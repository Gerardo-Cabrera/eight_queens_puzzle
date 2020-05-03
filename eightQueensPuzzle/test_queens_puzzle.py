import pytest
from eightQueens import EightQueens


class TestQueensPuzzle:
    def test_one(self):
        puzzle = EightQueens(8)
        assert puzzle.solutions == 92

    def test_two(self):
        puzzle = EightQueens(9)
        assert puzzle.solutions == 352

    def test_three(self):
        puzzle = EightQueens(10)
        assert puzzle.solutions == 724

    def test_four(self):
        puzzle = EightQueens(11)
        assert puzzle.solutions == 2680

    def test_five(self):
        puzzle = EightQueens(12)
        assert puzzle.solutions == 14200

    def test_six(self):
        puzzle = EightQueens(13)
        assert puzzle.solutions == 73712