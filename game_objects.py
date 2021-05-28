import os
import pygame as pg

# Define Colors
babyblue = (146, 183, 254)
orangered = (255,69,0)
darkorange = (255,140,0)
olive = (189,183,107)
black = (0,0,0)
midnightblue = (25,25,112)

SCREEN_WIDTH  = 1200
SCREEN_HEIGHT = 1000
BLOCK_SIZE = 50


def initialize_level(entities,blocks,enemies):
    for i in range(10):
        block = Block(i,1)
        blocks.append(block)
        entities.append(block)


image_library = {}
def get_image(path):
    global image_library
    image = image_library.get(path)
    if image == None :
        normal_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pg.image.load(normal_path).convert_alpha()
        image_library[path] = image
    return image



# Game class holds all game objects, like Juno, blocks, enemies, etc.
# Responsible for displaying all sprites in the display function
class Game:
    def __init__(self):

        # All objects that can be interacted with
        self.entities = []
        # All objects that can be jumped on?
        self.blocks = []
        self.enemies = []
        self.juno = Juno(x=100,y=SCREEN_HEIGHT - BLOCK_SIZE*2)
        initialize_level(self.entities,self.blocks,self.enemies)

    def update_from_events(self, events):
        for event in events:
            if pressed[pg.K_UP]:
                self.juno.jump()
            if pressed[pg.K_LEFT]:
                self.juno.move_left()
            if pressed[pg.K_RIGHT]:
                self.juno.move_right()

    def display(self,screen):
        screen.fill(babyblue)
        for entity in self.entities:
            entity.show(screen)
        self.juno.show(screen)
        

class Juno:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.size = 50
        self.vx = 0
        self.vy = 0
        # Need a bunch more information here. Add as necessary

    def show(self,screen):
        img = get_image('Images/juno.png')
        img = pg.transform.scale(img, (self.size,self.size))
        screen.blit(img, (self.x,self.y))

    def jump(self):
        # If there is a block under juno, she can jump
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass



class Block:
    def __init__(self,x,y):
        self.x = x * BLOCK_SIZE
        self.y = SCREEN_HEIGHT - y * BLOCK_SIZE

    def show(self,screen):
        if self.x < 1000 and self.x >= 0:
            screen.blit(get_image('Images/block.png'),(self.x,self.y))


