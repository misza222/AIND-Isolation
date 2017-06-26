"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

from isolation import Board
from sample_players import *
from game_agent import *

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        pass

    def test_minimax_plays_the_game(self):
        player1 = MinimaxPlayer(score_fn=improved_score, timeout=1.0, search_depth=1)
        player2 = GreedyPlayer()
        game = Board(player1, player2)
        game.play()

    def test_minimax_timesout(self):
        player1 = MinimaxPlayer(score_fn=improved_score, timeout=0, search_depth=1)
        player2 = GreedyPlayer()
        game = Board(player1, player2)
        game.play()

if __name__ == '__main__':
    unittest.main()
