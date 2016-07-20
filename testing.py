import unittest

from tictactoe import GameState, NoMoveMadeException

class Test(unittest.TestCase):

	def test_no_winner_yet(self):
		no_winner_yet = GameState([['X', None, 'X'], ['O', None, None], ['O', None, None]], 'O')
		no_winner_yet.move(1,1)
		print "\n\nno winner yet:"
		print no_winner_yet
		self.assertTrue(no_winner_yet.check_winner() == None)

	def test_x_win(self):
		x = GameState([[None, None, 'X'], [None, 'X', None], [None, None, None]], 'X')
		x.move(0,2)
		print "\n\nx wins:"
		print x
		self.assertTrue(x.check_winner() == 'X')

	def test_draw(self):
		draw = GameState([[None, 'O', 'O'], ['O', 'X', 'X'], ['O', 'X', 'O']], 'X', move_count=8)
		draw.move(0,0)
		print "\n\ndraw:"
		print draw
		self.assertTrue(draw.check_winner() == 'draw')

	def test_NoMoveException(self):
		no_move_made = GameState([[None, None, None], [None, None, None], [None, None, None]], 'X')
		print "\n\nno move made:"
		print no_move_made
		self.assertRaises(NoMoveMadeException, no_move_made.check_winner)

if __name__ == '__main__':
	unittest.main()