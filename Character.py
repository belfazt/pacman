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
    	if whereTo == 'up':
    		self.y = self.y - 1
    	elif whereTo == 'down':
    		self.y = self.y + 1
    	elif whereTo == 'right':
    		self.x = self.x + 1
    	elif whereTo == 'left':
    		self.x = self.x - 1
    	return self.get_position()