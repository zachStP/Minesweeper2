import Board

class FileIO:
    def __init__(self):
        self.data = []
        self.f = open("layout.txt")
        self.file = self.f.read

        for line in self.file:
            row = []
            for ch in line:
                row.append(int(ch))
            self.data.append(row)
        
        self.b = Board(self.data)
        self.f.close()
    
    def getBoard(self):
        return self.b
    