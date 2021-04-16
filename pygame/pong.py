import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 75
        self.up = False
        self.down = False
        self.score = 0
    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        color = (255, 255, 255)
        pygame.draw.rect(screen, color, rect)
    def move(self):
        if self.up:
            self.y -= 1
        elif self.down:
            self.y += 1
class Ball:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.radius = 10
        self.xspeed = -1
        self.yspeed = 0
    def draw(self):
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
    def collide(self, player):
        if self.x - self.radius < player.x + player.width and self.x + self.radius > player.x:
           if self.y - self.radius < player.y + player.height and self.y + self.radius > player.y:
               return True
        return False
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.collide(player) == True:
            angle = random.randint(95, 265)
            self.xspeed = math.cos(math.radians(angle)) * -1
            self.yspeed = math.sin(math.radians(angle)) * 1
        if self.collide(computer) == True:
            angle = random.randint(95, 265)
            self.xspeed = math.cos(math.radians(angle)) * 1
            self.yspeed = math.sin(math.radians(angle)) * 1
        if self.x - self.radius < 0:
            self.x = 250
            self.y = 250
            computer.score += 1
        elif self.x + self.radius > 500:
            self.x = 250
            self.y = 250
            player.score += 1
        if self.y - self.radius < 0 or self.y + self.radius > 500:
            self.yspeed *= -1
class Computer(Paddle):
    def __init__(self):
        super().__init__(465, 217.5)
    def move(self):
        randnumber = random.randint(0, 1)
        if ball.xspeed > 0 and ball.x > 250 and randnumber == 1:
            if self.y + self.height/2 < ball.y:
                self.y += 1
            elif self.y + self.height/2 > ball.y:
                self.y -= 1
ball = Ball()
player = Paddle(10, 217.5)
computer = Computer()
def drawScores():
    font = pygame.font.SysFont(None, 50)
    score1 = font.render(str(player.score), True, (255, 255, 255))
    score2 = font.render(str(computer.score), True, (255, 255, 255))
    screen.blit(score1, (125, 50))
    screen.blit(score2, (375, 50))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.up = True
            if event.key == pygame.K_s:
                player.down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.up = False
            if event.key == pygame.K_s:
                player.down = False
    screen.fill((0, 0, 0))
    drawScores()
    player.draw()
    computer.draw()
    ball.draw()
    ball.move()
    player.move()
    computer.move()
    pygame.display.flip()
pygame.quit()
