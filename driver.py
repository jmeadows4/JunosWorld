import pygame as pg
import game_objects as go
import numpy as np


# Start Pygame 
pg.init()
pg.display.set_caption("Juno's World")
clock = pg.time.Clock()

# Screen Stuff
screen_width = 1200
screen_height = 1000
screen_size = (screen_width, screen_height)
screen = pg.display.set_mode(screen_size)

# Title and Start Button Render
font = pg.font.SysFont("arial",50)
start_rend = font.render("New Game",True,(25,25,112))
start_rect = start_rend.get_rect()
start_rect.centerx = screen_width/2
start_rect.centery = screen_height/1.5

font = pg.font.SysFont("arial",100)
title_rend = font.render("Juno's World",True,(146,183,254))
title_rect = title_rend.get_rect()
title_rect.centerx = screen_width/2
title_rect.centery = screen_height/3


# Start Screen
game_started = False
while not game_started:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = event.pos
            sqx = (x - (screen_width/2))**2
            sqy = (y - (screen_height/1.5))**2
            if np.sqrt(sqx+sqy) < 140:
                game_started = True
    pg.draw.circle(screen,(255,255,255),(screen_width//2,int(screen_height/1.5)),140)


    pressed = pg.key.get_pressed()
    if pressed[pg.K_q]:
        exit()
    screen.blit(start_rend,start_rect)
    screen.blit(title_rend,title_rect)
    pg.display.flip()
    clock.tick(60)

#juno_sprite = game_objects.Juno()

# Maybe pass in the level here?
game_obj = go.Game()

game_over = False
while not game_over:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
    # Update Juno based off the key inputs
    game_obj.update_from_events(pg.event.get())
    # Display all game objects
    game_obj.display(screen)

    pressed = pg.key.get_pressed()
    if pressed[pg.K_q]:
        exit()

    pg.display.flip()
    clock.tick(60)

