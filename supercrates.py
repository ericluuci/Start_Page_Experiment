# Eric Lu

import pygame
import sys
import time

class GameApp:

    def __init__(self):

        self.start = False
        #self.start = True ### REMOVE THIS AND UNCOMMENT ABOVE
        self.appear = True
        self.block_list = []

        # Creates a window and title
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Super Crates - Eric Lu')

        # Plays music
        pygame.mixer.music.load('background.mp3')
        pygame.mixer.music.play(-1)

        # Loads 'platform.txt' into a list
        infile = open('platform.txt', 'r')
        lines = infile.readlines()
        self.block_list = []
        for x in lines:
            self.block_list.append(x.split())

        # Loads background
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (800, 600))

        # Load 'block.jpg' image
        self.block = pygame.image.load('block.jpg')
        self.block = pygame.transform.scale(self.block, (25, 25))

    def renderBack(self):

        self.screen.blit(self.bg, (0,0))

    def renderStart(self):

        self.renderBack()
        
        # Creates 'SUPER CRATES'
        title_font = pygame.font.SysFont('Times New Roman', 72)
        title1 = title_font.render('SUPER CRATES', 1, (255, 255, 255))
        title2 = title_font.render('SUPER CRATES', 1, (220, 220, 220))
        self.screen.blit(title2, (153, 73))
        self.screen.blit(title1, (150, 70))

        if (self.appear == True):
            
            # Creates 'CLICK TO START'
            start_font = pygame.font.SysFont('Times New Roman', 36)
            start1 = start_font.render('CLICK TO START', 1, (255, 255, 255))
            start2 = start_font.render('CLICK TO START', 1, (220, 220, 220))
            self.screen.blit(start2, (259, 442))
            self.screen.blit(start1, (257, 440))
            pygame.display.update()
            pygame.time.wait(700)
            self.appear = False
            
        else:
            
            pygame.display.update()
            pygame.time.wait(500)
            self.appear = True
        
    def renderPlatform(self):

        for col in range(0, len(self.block_list), 1):
            for row in range(0, len(self.block_list[col]), 1):

                if (self.block_list[col][row] == '1'):
                    self.screen.blit(self.block, (row*25,col*25))

    def renderGame(self):

        self.renderBack()
        self.renderPlatform()
        pygame.display.update()

    def mainloop(self):

        while True:

            for event in pygame.event.get():

                pressed = pygame.key.get_pressed()

                if (event.type == pygame.QUIT):    
                    pygame.quit()
                    sys.exit()

                if (self.start == False and event.type == pygame.MOUSEBUTTONDOWN):
                    self.start = True
            
            if (self.start == False):
                self.renderStart()
            else:
                self.renderGame()

    def update(self):
        pass

if __name__ == '__main__':
    GameApp().mainloop()
