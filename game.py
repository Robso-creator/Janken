import pygame

#images
button = pygame.image.load("assets/images/button.png")
button2 = pygame.image.load("assets/images/button2.png")
rock = pygame.image.load("assets/images/rock.png")
paper = pygame.image.load("assets/images/paper.png")
scissor = pygame.image.load("assets/images/scissor.png")

class Main():
    
    def __init__(self):

        pygame.init()
        
        #scene
        self.background = pygame.image.load("assets/images/start_screen.png")
        
        #display height & width definition
        size = width, height = 360, 640 
        self.screen = pygame.display.set_mode((size))
        #title defintion
        self.title = pygame.display.set_caption("RPS game")
        #icon definition
        icon = pygame.image.load("assets/images/icon.png")
        self.icon = pygame.display.set_icon(icon)


        self.loop = True
        self.scene = False
        self.rockt = False
        self.papert = False
        self.scissort = False
        



    def draw(self):
        self.screen.blit(self.background, (0,0))

        if self.scene:
            self.rocky, self.rockx = 50, 550
            self.papery, self.paperx = 155, 550
            self.scissory, self.scissorx = 250, 550
            self.screen.blit(rock, (self.rocky, self.rockx))
            self.screen.blit(paper, (self.papery, self.paperx))
            self.screen.blit(scissor, (self.scissory, self.scissorx))

            midposx, midposy = 155,400
            if self.rockt:
                self.screen.blit(rock, (midposx, midposy))
            elif self.papert:
                self.screen.blit(paper, (midposx, midposy))
            elif self.scissort:
                self.screen.blit(scissor, (midposx, midposy))
            else:
                pass

            mouse = pygame.mouse.get_pos()
            buttonx, buttony = 170,25
            if 160 <= mouse[0] <= 192 and 25 <= mouse[1] <= 57:
                self.screen.blit(button, (buttonx, buttony))
          
            else:
                self.screen.blit(button2, (buttonx, buttony))


    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    self.scene = True
                    self.background = pygame.image.load("assets/images/game_bg.png")

            
            if events.type == pygame.MOUSEBUTTONDOWN and self.scene:
                mouse = pygame.mouse.get_pos()
                if 160 <= mouse[0] <= 192 and 25 <= mouse[1] <= 57:
                    self.loop = False
                #rock
                if self.rocky <= mouse[0] <= self.rocky+64 and self.rockx <= mouse[1] <= self.rockx+64:
                    self.rockt = True
                    self.papert = False
                    self.scissort = False
                #paper
                if self.papery <= mouse[0] <= self.papery+64 and self.paperx <= mouse[1] <= self.paperx+64:
                    self.rockt = False
                    self.papert = True
                    self.scissort = False
                #scissor
                if self.scissory <= mouse[0] <= self.scissory+64 and self.scissorx <= mouse[1] <= self.scissorx+64:
                    self.rockt = False
                    self.papert = False
                    self.scissort = True
                    

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()

Main().update()