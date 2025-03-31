
import pygame, sys
from pygame.locals import *
import random
from color_palette import *


pygame.init()
font_small = pygame.font.SysFont("Verdana", 20)

colorWHITE = (255, 255, 255)
colorGRAY = (169, 169, 169)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)

LEVEL = 0
SCORE = 0
EATEN = False

WIDTH = 600
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(colorWHITE)
screen = pygame.display.set_mode((HEIGHT, WIDTH))

CELL = 30

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
    def __eq__(self, value):
        if self.x == value.x and self.y == value.y:
            return True
        return False
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        # wall-collision
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            print("Game Over! Hit the wall.")
            pygame.quit()
            exit()

        #self-Collision
        if new_head in self.body[1:]: 
            print("Game Over! Snake hit itself.")
            pygame.quit()
            exit()

        self.body.insert(0, new_head)
        self.body.pop()
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global SCORE
        global EATEN
        head = self.body[0]
        if head == food.pos:
            print("Got food!")
            SCORE = SCORE + 1
            EATEN = True
            self.body.append(Point(head.x, head.y))

class Food:
    def __init__(self):
        self.pos = Point(random.randint(1, 19), random.randint(1, 19))
    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
    while True and EATEN:
        food.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        if food.pos not in snake.body: #check if food is not inside a snake
            EATEN = False
            break

    draw_grid_chess()
    scores = font_small.render(str(SCORE), True, colorRED)
    levels = font_small.render(str(LEVEL), True, colorRED)
    DISPLAYSURF.blit(levels, (580,10 ))
    DISPLAYSURF.blit(scores, (10,10))
    if(SCORE > 10):
        LEVEL = 1
        FPS = 8
    elif(SCORE > 30):
        LEVEL = 2
        FPS = 10
    elif(SCORE > 50):
        LEVEL = 3
        FPS = 13 
    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()