import pygame
import numpy as np
import sys
import random
from pygame.locals import *

white=(255,255,255)
black=(0,0,0)
square_size=60
class chessboard:
    def __init__(self,width,height,DISPLAY):
        self.width=width;
        self.height=height;
        self.board=np.zeros([width+4,height+4])
        self.DISPLAY=DISPLAY
        self.actual=1
        self.jump=[]
        for i in (1,2):
            j=3-i
            self.jump.extend([(i,j),(i,-j),(-i,j),(-i,-j)])
        self.basicfont = pygame.font.SysFont('Ariel', 28)
        self.draw()
        x=int(random.random()*width//1)+2
        y=int(random.random()*height//1)+2
        self.board[x,y]=1
        print x-1
        print y-1       
        self.knight=pygame.transform.scale(pygame.image.load('knight.png'),(square_size,square_size))
        self.move_knight(x,y,(0,0)) ##point (0,0) is not on screen and so wont be printed

    def draw(self):
        for i in range (0,self.height):
            for j in range (0,self.width):
                if ((i+j)%2==1):
                    pygame.draw.rect(self.DISPLAY,black,(square_size*j,square_size*i,square_size,square_size))
                else:
                     pygame.draw.rect(self.DISPLAY,white,(square_size*j,square_size*i,square_size,square_size))
        SCORE = self.basicfont.render('SCORE:', True, (255, 0, 0), black)
        SCORErect = SCORE.get_rect()
        SCORErect.centerx = square_size*self.width-100
        SCORErect.centery = square_size*self.height+20
        self.DISPLAY.blit(SCORE, SCORErect)

    def on_click(self,pos):
        x=int(pos[0]//square_size)+2
        y=int(pos[1]//square_size)+2
        print x-1
        print y-1
        if self.board[x,y]==0:
            print 'empty'
            for m in [(x+j[0],y+j[1]) for j in self.jump]:
                if self.board[m]==self.actual:
                    self.move_knight(x,y,m)
                    if (self.is_end(x,y)):
                        self.game_end()

    def move_knight(self,x,y,last):
        ##move_knight and add actual state
        self.actual=self.actual+1
        self.board[x,y]=self.actual
        self.DISPLAY.blit(self.knight,(square_size*(x-2),square_size*(y-2)))
        #removes last knight
        if ((last[0]+last[1])%2==1):
            pygame.draw.rect(self.DISPLAY,black,(square_size*(last[0]-2),square_size*(last[1]-2),square_size,square_size))
        else:
            pygame.draw.rect(self.DISPLAY,white,(square_size*(last[0]-2),square_size*(last[1]-2),square_size,square_size))
        ##add number on the square
        text = self.basicfont.render(str(self.actual-2), True, (255, 0, 0), (100, 100, 100))
        textrect = text.get_rect()
        textrect.centerx = last[0]*square_size-square_size*3/2
        textrect.centery = last[1]*square_size-square_size*3/2
        self.DISPLAY.blit(text, textrect)
        text_score = self.basicfont.render(str(self.actual-1), True, (255, 0, 0), (100, 100, 100))
        textscore = text_score.get_rect()
        textscore.centerx = square_size*self.width-20
        textscore.centery = square_size*self.height+20       
        self.DISPLAY.blit(text_score, textscore)
        pygame.display.flip()

    def is_end(self,x,y):
        print x
        print y
        for m in [(x+j[0],y+j[1]) for j in self.jump]:
            #print (self.board[m]==0 and 0<=x<=self.width and 0<=y<=self.height)
            print m
            if (self.board[m]==0 and 1<=m[0]-1<=self.width and 1<=m[1]-1<=self.height):
                print 'denied on'
                print m
                return(False)
        return(True)
    def game_end(self):
        text = self.basicfont.render('The end. Your score was: '+str(self.actual-1), True, (255, 0, 0), (100, 100, 100))
        end_text = text.get_rect()
        end_text.centerx = self.width*square_size/2
        end_text.centery = self.height*square_size/2
        self.DISPLAY.blit(text, end_text)

if __name__ == "__main__":
    width=8
    height=8
    pygame.init()
    screen = pygame.display.set_mode((square_size*8, square_size*8+40))
    chess=chessboard(8,8,screen)
    basicfont = pygame.font.SysFont('Ariel', 28)
    text = basicfont.render('New game', True, (255, 0, 0), (100, 100, 100))
    button_text = text.get_rect()
    button_text.centerx = 60
    button_text.centery = height*square_size+20
    screen.blit(text, button_text)
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
                if pos[1]<square_size*8:
                    chess.on_click(pos)
                if button_text.collidepoint(pos):
                    print 'click'
                    pygame.draw.rect(screen,black,(width*square_size-40,height*square_size,40,40))
                    chess=chessboard(width,height,screen)
        pygame.display.update()

