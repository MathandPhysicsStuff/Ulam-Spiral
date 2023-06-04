import pygame 
from sys import exit
from time import sleep
from functions import *
from CONSTANCE import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    
    size = 32
    running = True
    draw = False 

    while running:
        
        screen.fill(DARK_GRAY_BLUE)
        
        if draw == True:
            Draw_Spiral(screen, size, BLUE)

            if size > 1:
                size *= 0.5
                size = int(size)
                time.sleep(5)
            else:
                size = 1

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:
                    draw = True

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
