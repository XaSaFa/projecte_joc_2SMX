import pygame, sys
from pygame.locals import *

AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255,255,0)
VIOLET = (148,0,211)
GREY = (128,128,128)
MARRON = (128,0,0)
BLACK = (0,0,0)
OLIVE = (134,139,73)
CYAN = (0,255,255)
PINK = (255,153,204)
MAGENTA = (255,0,255)
TAN = (210,180,140)
TEAL = (0,128,128)
WHITE = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
i = 1
d = 1
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(WHITE)
    # BACKGROUND
    pygame.draw.rect(pantalla, PINK,(0,0,300,400))
    pygame.draw.ellipse(pantalla, BLACK, (34, 155, 10, 25), 2)
    # BODY
    pygame.draw.ellipse(pantalla,GREEN,(40,50,200,300))
    pygame.draw.circle(pantalla, BLACK, (140, 150), 100, 2)
    pygame.draw.ellipse(pantalla, BLACK, (40, 50, 200, 300),2)
    pygame.draw.circle(pantalla, GREEN, (140, 150), 98)
    pygame.draw.circle(pantalla, GREEN, (140, 152), 99)
    # GLASS
    pygame.draw.rect(pantalla, YELLOW, (220, 155, 20, 25))
    pygame.draw.rect(pantalla, BLACK, (220, 155, 20, 25), 2)
    pygame.draw.rect(pantalla, YELLOW, (40,155,20,25))
    pygame.draw.rect(pantalla, BLACK, (40, 155, 20, 25),2)

    pygame.draw.ellipse(pantalla, BLACK, (230, 155, 20, 25), 2)
    pygame.draw.ellipse(pantalla, YELLOW, (228, 155, 20, 25))

    pygame.draw.ellipse(pantalla, YELLOW, (36, 155, 10, 25))
    pygame.draw.ellipse(pantalla, BLACK, (36, 155, 10, 25), 2)
    pygame.draw.ellipse(pantalla, YELLOW, (36, 155, 10, 25))
    pygame.draw.ellipse(pantalla, YELLOW,(55,147,20,40))
    pygame.draw.ellipse(pantalla, BLACK, (55, 147, 20, 40),2)
    pygame.draw.ellipse(pantalla, YELLOW, (210, 147, 20, 40))
    pygame.draw.ellipse(pantalla, BLACK, (210, 147, 20, 40), 2)
    pygame.draw.polygon(pantalla, YELLOW,((65, 130), (70, 125), (215, 125), (220, 130), (220, 200), (215, 205), (70, 205), (65, 198)))
    pygame.draw.polygon(pantalla, BLACK,((65, 130), (70, 125), (215, 125), (220, 130), (220, 200), (215, 205), (70, 205), (65, 198)),2)
    pygame.draw.polygon(pantalla, WHITE,
                        ((75, 140), (80, 135), (205, 135), (210, 140), (210, 190), (205, 195), (80, 195), (75, 188)))
    pygame.draw.polygon(pantalla, BLACK,((75, 140), (80, 135), (205, 135), (210, 140), (210, 190), (205, 195), (80, 195), (75, 188)),2)

    # ANTENNAS
    pygame.draw.polygon(pantalla, GREEN, ((130,60),(100,30),(90,28),(30,30),(25,35),(30,40),(90,35),(125,60)))
    pygame.draw.polygon(pantalla, BLACK,
                        ((130, 60), (100, 30), (90, 28), (30, 30), (25, 35), (30, 40), (90, 35), (125, 60)),2)
    pygame.draw.polygon(pantalla, GREEN,
                        ((140, 58), (180, 30), (220,50),(270,21),(276,22),(275,30),(225,55),(185,38),(145, 60)))
    pygame.draw.polygon(pantalla, BLACK,
                        ((140, 58), (180, 30), (220, 50), (270, 21), (276, 22), (275, 30), (225, 55), (185, 38),
                         (145, 60)),2)




    # TEXT SQUARE
    pygame.draw.rect(pantalla, WHITE,(20,250,260,130))
    pygame.draw.rect(pantalla, BLACK, (20, 250, 260, 130),2)


    # EYES
    pygame.draw.circle(pantalla, BLACK, (155, 160), 4)
    pygame.draw.circle(pantalla, BLACK, (128, 160), 4)
    pygame.draw.arc(pantalla, BLACK, (118,155,10,10),1.6,4.5)
    pygame.draw.arc(pantalla, BLACK, (155,155,10,10),5,1.4)
    # pygame.draw.circle(pantalla, BLACK, (155, 160), 4)

    # MOUTH
    pygame.draw.arc(pantalla, BLACK, (60,190,160,40),3.15,6.2,1)
    pygame.draw.arc(pantalla, BLACK, (120, 220, 20, 20), 4, 5, 1)

    # GLASS DETAILS

    pygame.draw.line(pantalla, BLACK,(110,136),(85,180))
    pygame.draw.line(pantalla, BLACK, (120, 136), (95, 185))


    pygame.display.update()
