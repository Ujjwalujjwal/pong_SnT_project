import pygame
import random

class Ball:
    def __init__(self, radius, xposi, yposi, surf, scrht, scrwt) -> None:
        self.radius = radius
        self.xposi = xposi
        self.yposi = yposi
        self.surf = surf
        self.scrht = scrht
        self.scrwt = scrwt
        self.color = (255,255,255)
        self.rect = pygame.draw.circle(self.surf,self.color,(self.xposi,self.yposi), self.radius )
        self.delvel = 0.5
        self.dx = self.delvel
        self.dy = self.delvel

    def draw(self):
        self.move()
        self.rect = pygame.draw.circle(self.surf,self.color,(self.xposi,self.yposi), self.radius )

    def move(self):
        if self.yposi <0 or self.yposi > self.scrht:
            self.dy *= -1

        if self.xposi <0 or self.xposi > self.scrwt:
            self.xposi = self.scrwt/2
            self.yposi = self.scrht/2
        self.xposi += self.dx
        self.yposi += self.dy

    def checkCollision(self, Lrect, Rrect):
        if pygame.Rect.colliderect(self.rect, Lrect) or pygame.Rect.colliderect(self.rect, Rrect):
            self.dy = self.delvel * random.random() * (self.dy/ abs(self.dy))
            self.dx *= -1
