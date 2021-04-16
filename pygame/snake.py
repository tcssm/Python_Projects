import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
class Part:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    def draw(self):
        color = (255, 255, 255)
        pygame.draw.rect(screen, color, self.rect)
class Snake:
    def __init__(self):
        self.parts = [Part(250, 250)]
        self.direction = ""
    def draw(self):
        for p in self.parts:
            p.draw()
    def add(self, index):
        part = None
        if self.direction == "right":
            if index == 0:
                part = Part(self.parts[0].x + 20, self.parts[0].y)
            else:
                part = Part(self.parts[-1].x - 20, self.parts[-1].y)
        if self.direction == "left":
            if index == 0:
                part = Part(self.parts[0].x - 20, self.parts[0].y)
            else:
                part = Part(self.parts[-1].x + 20, self.parts[-1].y)
        if self.direction == "up":
            if index == 0:
                part = Part(self.parts[0].x, self.parts[0].y - 20)
            else:
                part = Part(self.parts[-1].x, self.parts[-1].y + 20)
        if self.direction == "down":
            if index == 0:
                part = Part(self.parts[0].x, self.parts[0].y + 20)
            else:
                part = Part(self.parts[-1].x, self.parts[-1].y - 20)
        self.parts.insert(index, part)
        if index == 0:
            self.parts.pop()
    def edge(self):
        global running
        p = self.parts[0]
        if p.x < 0 or p.x + p.size > 500 or p.y < 0 or p.y + p.size > 500:
            running = False
    def collide(self):
        global running
        s0 = self.parts[0]
        for index in range(2, len(self.parts)):
            sTemp = self.parts[index]
            if s0.x < sTemp.x + sTemp.size and s0.x + s0.size > sTemp.x:
                if s0.y < sTemp.y + sTemp.size and s0.y + s0.size > sTemp.y:
                    running = False
class Apple:
    def __init__(self):
        self.x = random.randint(20, 480)
        self.y = random.randint(20, 480)
        self.radius = 10
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
    def collide(self):
        global a
        s0 = s.parts[0]
        if s0.x < self.x + self.radius and s0.x + s0.size > self.x - self.radius:
            if s0.y < self.y + self.radius and s0.y + s0.size > self.y - self.radius:
                s.add(-1)
                a = Apple()
a = Apple()
s = Snake()
font = pygame.font.SysFont(None, 30)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and s.direction != "down":
        s.direction = "up"
    elif keys[pygame.K_s] and s.direction != "up":
        s.direction = "down"
    elif keys[pygame.K_a] and s.direction != "right":
        s.direction = "left"
    elif keys[pygame.K_d] and s.direction != "left":
        s.direction = "right"
    if s.direction != "":
        s.add(0)
    a.collide()
    s.edge()
    s.collide()
    pygame.time.delay(100)
    screen.fill((0, 0, 0))
    score = font.render(str(len(s.parts) - 1), True, (255, 255, 255))
    screen.blit(score, (0, 0))
    a.draw()
    s.draw()
    pygame.display.flip()
pygame.quit()
