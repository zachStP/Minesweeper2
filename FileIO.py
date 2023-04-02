


class fileIO:

    def setBoard():
        board = Board()
    
        f = open("layout.txt")
        file = f.read
        
        r = 0
        c = 0

        for line in file:
            for ch in line:
                board.data[r][c] = int(ch)
                c+=1
            r+=1

        f.close()

    def getBoard():
        return board
    