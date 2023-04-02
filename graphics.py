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
cwidth: int
cheight: int
scaling: int
t_padding: int = 4
b_pad_x: int = 4
b_pad_y: int = 4

pg.init()
pg.display.set_caption("Minesweeper 2")

clock = pg.time.Clock()

display = pg.display.set_mode((width, height), pg.RESIZABLE)

player_ico = pg.image.load("assets/player.png").convert_alpha()


def update_scale(sqrgrid):
    global cwidth, cheight, scaling, tile_size, t_padding, b_pad_x, b_pad_y
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


def draw_board(board: list[list[int]], player):

    # update scales
    update_scale(4)

    for row in range(len(board)):
        for col in range(len(board[row])):
            posx = col * tile_size  + b_pad_x
            posy = row * tile_size + b_pad_y
            # draw border
            pg.draw.rect(display, (50, 50, 50), (posx-1, posy-1, tile_size+1, tile_size+1))
            # draw tile background
            pg.draw.rect(display, (255, 255, 255), (posx + t_padding / 2, posy + t_padding / 2,
                tile_size - t_padding, tile_size - t_padding))
        # end for col
    # end for row
    display.blit(pg.transform.smoothscale(player_ico.convert_alpha(),
        (tile_size - t_padding, tile_size - t_padding,)),
        (1 * tile_size + t_padding / 2 + b_pad_x, 1 * tile_size + t_padding / 2 + b_pad_y))
    print(4 * tile_size + t_padding / 2 + b_pad_x)