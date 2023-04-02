from Player import Player
from Board import Board

class Game:
    def __init__(self, mineData=None, player=None):
        if mineData is None:
            self.mineData = Board()
        else:
            self.mineData = mineData

        if player is None:
            self.player = Player(0, 0)
        else:
            self.player = player

    def update(self):
        if self.mineData.data[self.player.y][self.player.x] == 9:
            self.player.kill()
        self.mineData.show(self.player.x, self.player.y)


