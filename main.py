# imports
import sys
# local imports
import Graphics as gr
import Player, Game, Board, FileIO

inGame = False

game = None
board = None
player = None

def initGame():
    global game, board, player
    player = Player.Player(0 ,0)
    io = FileIO.FileIO("gpt2.txt")
    board = io.getBoard()
    game = Game.Game(board, player)
    game.update()

# end initGame

initGame()

inputed = False
# game loop
while True:
    
    # check for quit event
    for event in gr.pg.event.get():
        if event.type == gr.pg.QUIT:
            sys.exit()

    keys=gr.pg.key.get_pressed()
    if not inputed and (keys[gr.pg.K_a] or keys[gr.pg.K_d] or keys[gr.pg.K_w] or keys[gr.pg.K_s]):
        inputed = True

        if player.isDead:
            initGame()
            continue        
        
        if keys[gr.pg.K_x]:
            if keys[gr.pg.K_a] and board.display[player.y][player.x - 1] != None:
                player.flag(board, "left")
            elif keys[gr.pg.K_d] and board.display[player.y][player.x + 1] != None:
                player.flag(board, "right")
            elif keys[gr.pg.K_w] and board.display[player.y - 1][player.x] != None:
                player.flag(board, "up")
            elif keys[gr.pg.K_s] and board.display[player.y + 1][player.x] != None:
                player.flag(board, "down")
        elif keys[gr.pg.K_SPACE]:
            if keys[gr.pg.K_a]:
                game.points += player.pushMine(board, "left")
                board.show(player.x - 1, player.y)
            elif keys[gr.pg.K_d]:
                game.points += player.pushMine(board, "right")
                board.show(player.x + 1, player.y)
            elif keys[gr.pg.K_w]:
                game.points += player.pushMine(board, "up")
                board.show(player.x, player.y - 1)
            elif keys[gr.pg.K_s]:
                game.points += player.pushMine(board, "down")
                board.show(player.x, player.y + 1)
        else:
            if keys[gr.pg.K_a]:
                player.moveLeft()
            elif keys[gr.pg.K_d]:
                player.moveRight()
            elif keys[gr.pg.K_w]:
                player.moveUp()
            elif keys[gr.pg.K_s]:
                player.moveDown()
        
        game.update()
        gr.pg.display.set_caption("Minesweeper Sprint - Score: " + str(game.points))
    elif not (keys[gr.pg.K_a] or keys[gr.pg.K_d] or keys[gr.pg.K_w] or keys[gr.pg.K_s]):
        inputed = False


    gr.display.fill((0, 0, 0))
    gr.draw_board(board.data, board.display, player)
    gr.pg.display.flip()
    gr.clock.tick(30)