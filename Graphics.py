if __name__ == "__main__":
    import main

# pip imports
import pygame as pg
# local imports

# consts?
sqrgrid = 4

width: int = 1280
height: int = 720
tile_size: int = 80

# vars
cwidth: int = 0
cheight: int = 0
scaling: int
t_padding: int = 4
b_pad_x: int = 4
b_pad_y: int = 4

pg.init()
pg.display.set_caption("Minesweeper 2")

clock = pg.time.Clock()

display = pg.display.set_mode((width, height), pg.RESIZABLE)

player_ico = pg.image.load("assets/player.png").convert_alpha()
sprite = pg.transform.smoothscale(pg.image.load("assets/sprite.png"), (64, 64,)).convert_alpha()

numarr = []
for i in range(8):
    numarr.append(pg.transform.smoothscale(pg.image.load("assets/num" + str(i + 1) + ".png"), (64, 64,)).convert_alpha())

def ico_scale():
    global numarr, sprite, crush, player_ico
    sprite = pg.transform.smoothscale(pg.image.load("assets/sprite.png"), (tile_size, tile_size)).convert_alpha()

    player_ico = pg.transform.smoothscale(pg.image.load("assets/player.png"), (tile_size - t_padding, tile_size - t_padding)).convert_alpha()

    for i in range(8):
        numarr[i] = pg.transform.smoothscale(pg.image.load("assets/num" + str(i + 1) + ".png"), (tile_size, tile_size)).convert_alpha()

def update_scale(sqrgrid):
    global cwidth, cheight, scaling, tile_size, t_padding, b_pad_x, b_pad_y, rescale
    ow, oh = cwidth, cheight
    
    cwidth, cheight = pg.display.get_surface().get_size()
    swidth = cwidth / sqrgrid
    sheight = cheight / sqrgrid

    if swidth < sheight:
        scaling = swidth
        bwidth = swidth * sqrgrid
        b_pad_x = 0
        b_pad_y = (cheight - bwidth) / 2
    else:
        scaling = sheight
        bwidth = sheight * sqrgrid
        b_pad_y = 0
        b_pad_x = (cwidth - bwidth) / 2
    # end if else
    tile_size = scaling
    t_padding = tile_size / 10

    if not ow == cwidth or not oh == cheight:
        ico_scale()


def draw_board(board_dat: list[list[int]], board_vis: list[list[bool]], player):

    # update scales
    update_scale(len(board_dat))
    
    board = []

    for row in range(len(board_vis)):
        r = []
        for col in range(len(board_vis[row])):
            if board_vis[row][col] or True:
                r.append(board_dat[row][col])
            else:
                r.append(99)
        board.append(r)
        # end for col
    # end for row

    for row in range(len(board)):
        for col in range(len(board[row])):
            posx = col * tile_size  + b_pad_x
            posy = row * tile_size + b_pad_y
            # draw border
            pg.draw.rect(display, (50, 50, 50), (posx-1, posy-1, tile_size+1, tile_size+1))
            
            if row == 0 and col == 0:
                pg.draw.rect(display, (0, 100, 0), (b_pad_x + t_padding / 2, b_pad_y + t_padding / 2,
                        tile_size - t_padding, tile_size - t_padding))
                if board[player.y][player.x] >= 1 and board[player.y][player.x] <= 8:
                    display.blit(numarr[board[player.y][player.x] - 1],
                        (b_pad_x + t_padding / 2, b_pad_y + t_padding / 2))
                    
                continue

            # draw tile 
            # 99 = not clear
            if board[row][col] == 99:
                pg.draw.rect(display, (255, 255, 255), (posx + t_padding / 2, posy + t_padding / 2,
                    tile_size - t_padding, tile_size - t_padding))
            else:
                pg.draw.rect(display, (100, 100, 100), (posx + t_padding / 2, posy + t_padding / 2,
                    tile_size - t_padding, tile_size - t_padding))

            # 9 = mine
            if board[row][col] == 9:
                pg.draw.rect(display, (255, 0, 0), (posx + t_padding / 2, posy + t_padding / 2,
                    tile_size - t_padding, tile_size - t_padding))
                
                display.blit(sprite,
                    (posx + t_padding / 2, posy + t_padding / 2))
            # 1-8 = clear
            elif board[row][col] >= 1 and board[row][col] <= 8:
                pg.draw.rect(display, (100, 100, 100), (posx + t_padding / 2, posy + t_padding / 2,
                    tile_size - t_padding, tile_size - t_padding))
                display.blit(numarr[board[row][col] - 1],
                    (posx + t_padding / 2, posy + t_padding / 2))
        
        # end for col
    # end for row
    
    # display player
    display.blit(player_ico,
        (player.x * tile_size + t_padding / 2 + b_pad_x, player.y * tile_size + t_padding / 2 + b_pad_y))
    