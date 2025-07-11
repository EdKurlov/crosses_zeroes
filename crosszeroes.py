import pygame  
from model import * 

FPS = 60  
CELL_SIZE = 50  

class GameFieldView:
	"""
	 A game board widget that displays it on the screen and also detects 
	the click location.
	"""
	def __init__(self, field):
		# load cell icon images
		# show primary field state
		self._field = field
		self._height = field.height * CELL_SIZE  
		self._width = field.width * CELL_SIZE  

	def draw(self):
		pass

	def check_coords_correct(self, x, y):
		return True  # TODO: self._height take into account

	def get_coords(self, x, y):
		return 0, 0  #  TODO: really calculate the click cell

class ChoosePlayersManager:
	pass

class GameRoundManager:
	"""
	Game manager that runs all play processes.
	"""
	def __init__(self, player1: Player, player2: Player):
		self._players = [player1, player2]
		self._current_player_index = 0  
		self._field = GameField()

	def handle_click(self, i, j):
		player = self._players[self._current_player_index]
		#  player is doing click
		print('click_handled', i, j)

class GameWindow:
	"""
	It contents field widget and a manager of the play round.
	"""
	def __init__(self):
		#  Initialization of pygame
		pygame.init()

		self._width = 800  
		self._height = 600  
		self._title = "Crosses & Zeroes"
		self._screen = pygame.display.set_mode((self._width, self._height))
		pygame.display.set_caption(self._title)

		player1 = HumanPlayer(Cell.CROSS)
		player2 = AIPlayer(Cell.ZERO)
		self._game_manager = GameRoundManager(player1, player2)
		self._field_widget = GameFieldView(self._game_manager.field)

	def main_loop(self):
		finished = False
		clock = pygame.time.Clock()
		while not finished:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					finished = True
				elif event.t == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					x, y = mouse.pos
					if self._field_widget.check_coords_correct(x, y):
						i, j = self._field_widget.get_coords(x, y)
						self._game_manager.handle_click(i, j)
			pygame.display.flip()
			clock.tick(FPS)			


def main():
	window = GameWindow()
	window.main_loop()
	print('Game over!')


if __name__ == '__main__':
	main()
		 