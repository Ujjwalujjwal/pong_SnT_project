import pygame

class Paddle:
    def __init__(self, xpos, centhi, len, surf, screenht) -> None:
        self.xpos = xpos
        self.ypos = centhi
        self.len = len
        self.width = 20
        self.surf = surf
        self.rect = pygame.Rect(self.xpos, self.ypos,self.width, self.len)
        self.color = (255,255,255)
        self.vel = 2
        self.upact = False
        self.downact = False
        self.screenht = screenht

    def draw(self):
        self.move()
        pygame.draw.rect(self.surf, self.color,self.rect)

    def checkInp(self, key, isdown):
        if (key == pygame.K_UP) and isdown:
            self.upact = True
        if (key == pygame.K_DOWN) and isdown:
            self.downact = True
        if (key == pygame.K_UP) and not isdown:
            self.upact = False
        if (key == pygame.K_DOWN) and not isdown:
            self.downact = False



    def move(self):
        if(self.upact and self.ypos > 0):
            self.ypos -= self.vel

        if (self.downact and self.ypos < self.screenht - self.len):
            self.ypos += self.vel

        self.rect = pygame.Rect(self.xpos, self.ypos,self.width, self.len)