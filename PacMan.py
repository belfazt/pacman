from constants import WORLD
from Enemy import Enemy
from Player import Player
from input import pressed_key
import random, platform, os, sys

class PacMan:
    board = []
    player = None
    enemies = []
    world_info = {}
    enemies_spawn_area = []

    def __init__(self, board_path='board.txt', enemies_count=4):
        self.player = Player([16, 10])
        self.enemies = []
        self.enemies_spawn_area = [(9, 9), (9, 10), (9, 11), (10, 9), (10, 10), (10, 11)]
        self.read_board(board_path)
        for i in xrange(0, enemies_count):
            self.enemies.append(Enemy(random.choice(self.enemies_spawn_area)))
        self.update_board()


    def read_board(self, path):
        with open(path) as file:
            for line in file:
                row = [ _ for _ in line.split() ]
                self.board.append(row)
    
    def update_board(self):
        player_position = self.player.get_position()
        self.board[player_position[0]][player_position[1]] = WORLD['player']
        for enemy in self.enemies:
            enemy_position = enemy.get_position()
            self.board[enemy_position[0]][enemy_position[1]] = WORLD['enemy']

    def print_board(self):
        self.clear_screen()
        for row in self.board:
            for value in row:
                print value, 
            print ''

    def mutate(self):
        for enemy in self.enemies:
            enemy.behave(self.player, self.board)

    def play(self):
        self.print_board()
        while True:
            self.mutate()
            key = pressed_key()
            if key in ['W', 'w']:
                self.player.move('up', self.board)
            elif key in ['A', 'a']:
                self.player.move('left', self.board)
            elif key in ['S', 's']:
                self.player.move('down', self.board)
            elif key in ['D', 'd']:
                self.player.move('right', self.board)
            elif key in ['Q', 'q']:
                sys.exit(0)
            else:
                self.mutate()
                continue
            self.update_board()
            self.print_board()

    def clear_screen(self):
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear') #For linux.. I don't know what to do about mac :/
        

if __name__ == '__main__':
    pacman = PacMan()
    pacman.play()
