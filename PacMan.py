class PacMan:
    board = []
    player = None
    enemies = []

    def __init__(self, board_path = 'board.txt', player, enemies):
        self.player = player
        self.enemies = enemies
        self.read_board(board_path)

    def read_board(self, path):
        with open(path) as file:
            for line in file:
                row = [ _ for _ in line.split() ]
                self.board.append(row)
    
    def print_board(self):
        for row in self.board:
            for value in row:
                print value, 
            print ''
        

if __name__ == '__main__':
    pacman = PacMan()
    pacman.print_board()