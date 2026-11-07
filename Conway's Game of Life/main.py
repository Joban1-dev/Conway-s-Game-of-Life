import numpy as np
import pygame as pg
from sys import exit
from game_logic import next_generation

pg.init()
rng = np.random.default_rng()

def draw_grid(rows,columns,width,height,current_gen,screen):
    cell_width = width / columns
    cell_height = height / rows

    for row in range(current_gen.shape[0]):
        for column in range(current_gen.shape[1]):
            x = column * cell_width
            y = row * cell_height
            if current_gen[row][column] == 1:
                pg.draw.rect(screen,(0,0,0),(x,y,cell_width,cell_height),)
            else:
                pg.draw.rect(screen,(255,255,255),(x,y,cell_width,cell_height),)

    for row in range(current_gen.shape[0]):
        for column in range(current_gen.shape[1]):
            x = column * cell_width
            y = row * cell_height
            pg.draw.rect(screen,(100,100,100),(x,y,cell_width,cell_height),1)

def main():
    WIDTH = 800
    HEIGHT = 800
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    BACKGROUND = (30, 30, 35)
    clock = pg.Clock()
    current_gen = rng.integers(0, 2, size=(80, 80))

    last_update = 0
    generation_delay = 100
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()

        current_time = pg.time.get_ticks()

        if current_time - last_update >= generation_delay:
            current_gen = next_generation(current_gen)
            last_update = current_time
        screen.fill(BACKGROUND)
        draw_grid(80,80,WIDTH,HEIGHT,current_gen,screen)

        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()