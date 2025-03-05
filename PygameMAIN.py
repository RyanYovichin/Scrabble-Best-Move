import pygame
from functions.fgamecreate import gstart

pygame.init()# ig necessary


screen = pygame.display.set_mode((800, 650))#dispplay
pygame.display.set_caption("Scrabble")

b1,w1,t1 = gstart()
font = pygame.font.SysFont('Arial', 10)  # Use a system font, size 50
text1 = font.render('DLS', True, (0,0,0))
text2 = font.render('TLS', True, (0,0,0))
text3 = font.render('DWS', True, (0,0,0))
text4 = font.render('TWS', True, (0,0,0))
text5 = font.render('', True, (0,0,0))

screen.fill((255, 255, 255))#white screen
for i in range(15):
     for j in range(15):
         pygame.draw.rect(screen, (0, 0, 0), (50+500/15*i, 50+500/15*j, 500/15, 500/15))
         if b1[j][i] == 1.2: # sets color
             a = 190
             b = 235
             c = 227
             text = text1
         elif b1[j][i] == 1.3:
             a = 55
             b = 152
             c = 237
             text = text2
         elif b1[j][i] == 2:
             a = 255
             b = 129
             c = 94
             text = text3
         elif b1[j][i] == 3:
             a = 255
             b = 67
             c = 15
             text = text4
         else:
             a = 255
             b = 255
             c = 255
             text = text5
         pygame.draw.rect(screen, (a, b, c), ( 50+500/15*i+1, 50+500/15*j+1, 500/15-2, 500/15 -2))
         screen.blit(text, (50+500/15*i+1, 50+500/15*j+1))
pygame.draw.rect(screen,(0,0,0),(600,100,150,100))
pygame.draw.rect(screen,(255,255,255),(602,102,146,96))
font = pygame.font.SysFont('Arial', 50)
text = font.render('START', True, (0,0,0))
screen.blit(text, (610,120))
c = 1
f = 0
running = True# main
while running:
    for event in pygame.event.get(): # gets all events... specifically for closing window here
        if event.type == pygame.QUIT:  # closed window
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            m = pygame.mouse.get_pos()
            print(m)
            if ((m[0] >600) & (m[0]< 750)) & ((m[1] > 100) & (m[1] < 200)) and c == 1:
                print("game started")
                f = 1
                c = 0
                pygame.draw.rect(screen, (255,255,255), (600,100,150,100))#remove start button
                for i in range(6):
                    pygame.draw.rect(screen, (0,0,0), (50+i*35,550,130+i*35,580))#adding hand

                #remove start button and chang varible f +=1 change c !=1
                #run game
            
        #if 
                

    pygame.display.flip()

# Quit Pygame
pygame.quit()