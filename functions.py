import pygame, time
from CONSTANCE import *

def Draw_Spiral(screen, size, color):
    
    run_time = ((WIDTH // size)+1)**2 + 1

    shift = size//2
    x = WIDTH//2 - shift
    y = HEIGHT//2 - shift

    direction = 0
    step = 1
    turn_now = 1 
    counter = 0
    draw = 0
    
    for i in range(1, run_time):
        
        if is_prime(i):
            pygame.draw.rect(screen, color, [x, y, size, size])

        if direction == 0: 
            x += size
        if direction == 1: 
            y -= size
        if direction == 2: 
            x -= size
        if direction == 3: 
            y += size
        
        if  turn_now % step == 0:
            turn_now = 0
            direction = (direction + 1) % 4
            counter += 1
            if counter % 2 == 0:
                step += 1

        turn_now += 1
        draw += 1
        
        #pygame.display.update()


def Draw_number(cell):

    number_font = pygame.font.SysFont("serif", font_size)

    show_number = number_font.render


def is_prime(n):
    
    prime = True 
    i = 1

    while (i*i <= n):

        if n % i == 0 and i != 1:
            prime = False
            break

        i += 1
    
    return prime

def abundant_number(n):

    pass

def deficient_number(n):
    pass    
