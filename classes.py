import math, pygame
X_MAX = 800
Y_MAX = 600
class Clown(pygame.sprite.Sprite):
    def __init__(self, position, color, speed, direct):
        self.color = color
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.direct = direct
    def update(self):
        self.rect.x += self.direct[0]*self.speed[0] 
        self.rect.y += self.direct[1]*self.speed[1]
        self.collide(X_MAX,Y_MAX)
    def collide(self,x,y):
        if self.rect.x > x:
            self.rect.x = x
            self.direct[0] *= -1
        if self.rect.y > y:
            self.rect.y = y
            self.direct[1] *= -1
        if self.rect.x < 0:
            self.rect.x = 0
            self.direct[0] *= -1
        if self.rect.y < 0:
            self.rect.y = 0
            self.direct[1] *= -1
