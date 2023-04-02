
class Board:
    def __init__(self, data):
        if data is None:
            self.data = [[0 for j in range(16)] for i in range(16)]
            self.display = [[0 for j in range(16)] for i in range(16)]
            return
        else:
            self.data = [[data[i][j] for j in range(16)] for i in range(16)]
            self.display = [[False for j in range(16)] for i in range(16)]

    def show(self, x:int, y:int):
        self.display[y][x] = True

