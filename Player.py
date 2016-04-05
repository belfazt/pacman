from Character import Character

class Player(Character):
    ghost_buster = False

    def __init__(self, position):
        super(Player, self).__init__(position)
        self.ghost_buster = False

    def is_ghost_buster(self):
        return self.ghost_buster