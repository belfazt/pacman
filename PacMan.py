from Enemy import Enemy
from Player import Player
from input import pressed_key
import random

class PacMan:
    board = []
    player = None
    enemies = []
    world_info = {}
    enemies_spawn_area = []

    def __init__(self, board_path='board.txt', enemies_count=4):
        self.player = Player([16, 10])
        self.enemies = []
        self.world_info = {'#': "wall", '@':  'player', '.':  "empty", '$': 'token', '^': 'enemy'}
        self.enemies_spawn_area = [(9, 9), (9, 10), (9, 11), (10, 9), (10, 10), (10, 11)]
        self.read_board(board_path)
        for i in xrange(0, enemies_count):
            self.enemies.append(Enemy(random.choice(self.enemies_spawn_area)))


    def read_board(self, path):
        with open(path) as file:
            for line in file:
                row = [ _ for _ in line.split() ]
                self.board.append(row)
    
    def update_board(self):
        player_position = self.player.get_position()
        self.board[player_position[0]][player_position[1]] = '@'
        for enemy in self.enemies:
            enemy_position = enemy.get_position()
            self.board[enemy_position[0]][enemy_position[1]] = '^'

    def print_board(self):
        for row in self.board:
            for value in row:
                print value, 
            print ''
        

if __name__ == '__main__':
    pacman = PacMan()
    pacman.update_board()
    pacman.print_board()
