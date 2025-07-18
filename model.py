from enum import Enum

class Cell(Enum):
	VOID = 0  
	CROSS = 1  
	ZERO = 2

class GameField:
	height = 3  
	width = 3  

	def __init__(self):  
		self.cells = [[Cell.VOID]*self.width for i in range(self.height)]

class PlayerType(Enum):
	HUMAN = 0  
	AI = 1  


class Player:
	""" 
	Player class containing the badge type and name.
	"""
	def __init__(self, player_type: PlayerType, cell_type: Cell):
		self.player_type = player_type
		self.cell_type = cell_type

class HumanPlayer(Player):
	""" 
	Player class man.
	"""
	def __init__(self, cell_type: Cell):
		super(Player).__init__(PlayerType.HUMAN, cell_type)
		

class AIPlayer(Player):
	""" 
	Player class AI.
	"""
	def __init__(self, cell_type: Cell):
		super(Player).__init__(PlayerType.AI, cell_type)
	def choose_cell(self, field):
		pass
