from constants import WORLD

class Character(object):
    x = None
    y = None

    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def get_position(self):
        return (self.x, self.y)

    def move(self, whereTo, board):
    	board[self.x][self.y] = '.'
    	if whereTo == 'up' and board[self.x - 1][self.y] is not WORLD['wall']:
    		self.x = self.x - 1
    	elif whereTo == 'down' and board[self.x + 1][self.y] is not WORLD['wall']:
    		self.x = self.x + 1
    	elif whereTo == 'right' and board[self.x][self.y + 1] is not WORLD['wall']:
    		self.y = self.y + 1
    	elif whereTo == 'left' and board[self.x][self.y - 1] is not WORLD['wall']:
    		self.y = self.y - 1
    	return self.get_position()