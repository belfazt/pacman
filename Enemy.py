from Character import Character
from random import choice
from math import sqrt

class Enemy(Character):
    actions = {}
    state = 'search'

    def __init__(self, position):
        super(Enemy, self).__init__(position)
        self.actions = {'attack': self.attack, 'search': self.search, 'escape': self.escape}

    def attack(self, board):
        pass

    def search(self, board):
        possible_moves = ['up', 'down', 'left', 'right']
        self.move(choice(possible_moves), board)

    def escape(self, board):
        pass

    def get_distance_to(self, character):
        src = self.get_position()
        dst = character.get_position()
        return sqrt(abs((src[0]**2 + dst[0]**2) - (src[1]**2 + dst[1]**2)))

    def is_close_of(self, character):
        return self.get_distance_to(character) < 10

    def path_to(self, position, max_depth=10):
        
        return []

    def next_move(self, position):
        return self.path_to(position)[0]

    def behave(self, player, board):
        if player.is_ghost_buster():
            self.state = 'escape'
        elif self.is_close_of(player):
            self.state = 'attack'
        else:
            self.state = 'search'
        print self.state
        self.actions[self.state](board)
