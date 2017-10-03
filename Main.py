import pygame
import numpy as np
import sys
import random
from pygame.locals import *

white=(255,255,255)
black=(0,0,0)
class chessboard:
    def __init__(self,width,height,DISPLAY):
        self.width=width;
        self.height=height;
        self.board=np.zeros([width+4,height+4])
        self.DISPLAY=DISPLAY
        self.draw()
        self.actual=1
        self.jump=[]
        for i in (1,2):
            j=3-i
            self.jump.extend([(i,j),(i,-j),(-i,j),(-i,-j)])
        x=int(random.random()*8//1)+2
        y=int(random.random()*8//1)+2
        self.board[x,y]=1
        self.basicfont = pygame.font.SysFont('Ariel', 28)
        print x-1
        print y-1       
        self.knight=pygame.transform.scale(pygame.image.load('knight.gif'),(60,60))
        self.move_knight(x,y,(0,0)) ##point (0,0) is not on screen and so wont be printed

    def draw(self):
        for i in range (0,self.height):
            for j in range (0,self.width):
                if ((i+j)%2==1):
                    pygame.draw.rect(self.DISPLAY,black,(60*j,60*i,60,60))
                else:
                     pygame.draw.rect(self.DISPLAY,white,(60*j,60*i,60,60))
    def on_click(self,pos):
        x=int(pos[0]//60)+2
        y=int(pos[1]//60)+2
        print x-1
        print y-1
        if self.board[x,y]==0:
            print 'empty'
            for m in [(x+j[0],y+j[1]) for j in self.jump]:
                if self.board[m]==self.actual:
                    self.move_knight(x,y,m)

    def move_knight(self,x,y,last):
        ##move_knight and add actual state
        self.actual=self.actual+1
        self.board[x,y]=self.actual
        self.DISPLAY.blit(self.knight,(60*(x-2),60*(y-2)))
        #removes last knight
        if ((last[0]+last[1])%2==1):
            pygame.draw.rect(self.DISPLAY,black,(60*(last[0]-2),60*(last[1]-2),60,60))
        else:
            pygame.draw.rect(self.DISPLAY,white,(60*(last[0]-2),60*(last[1]-2),60,60))
        ##add number on the square
        text = self.basicfont.render(str(self.actual-2), True, (255, 0, 0), (100, 100, 100))
        textrect = text.get_rect()
        textrect.centerx = last[0]*60-90
        textrect.centery = last[1]*60-90
        self.DISPLAY.blit(text, textrect)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
    chess=chessboard(8,8,screen)
    print 'start'
    while True:
        for event in pygame.event.get():
            #print str(event)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONUP:
                print 'up'
                pos=pygame.mouse.get_pos()
                chess.on_click(pos)

        pygame.display.update()

