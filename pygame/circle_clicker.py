import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
class Circle:
    def __init__(self):
      self.x = random.randint(0, 500)
      self.y = random.randint(0, 500)
      self.radius = 5
      self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)
        self.radius += 1
    def detectMouse(self, mousePos):
        distance = math.sqrt((mousePos[0] - self.x) ** 2 + (mousePos[1] - self.y) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False

circles = []
number = random.randint(3, 5)
for i in range(number):
    circles.append(Circle())
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for c in circles:
        c.draw()
        if pygame.mouse.get_pressed()[0] == True:
            mousePos = pygame.mouse.get_pos()
            if c.detectMouse(mousePos) == True and c in circles:
                circles.remove(c)
                circles.append(Circle())
    pygame.display.flip()
pygame.quit()
