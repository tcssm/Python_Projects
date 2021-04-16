import pygame
import random
pygame.init()
screen = pygame.display.set_mode((750, 750))
running = True
class Piece:
    def __init__(self, image, x, y, rotation, scale):
        self.scale = scale
        self.x = x
        self.y = y
        self.rotation = rotation
        self.image = pygame.image.load(image)
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 1
        elif keys[pygame.K_d]:
            self.x += 1
        if keys[pygame.K_w]:
            self.rotation += 90
        if keys[pygame.K_s]:
            self.y += 3
        else:
            self.y += 1
    def draw(self):
        scaledImage = pygame.transform.rotozoom(self.image, self.rotation, self.scale)
        center = scaledImage.get_rect().center
        screen.blit(scaledImage, (self.x - center[0], self.y - center[1]))
    def collide(self):
        for piece in playedPieces:
            if not (self == piece):
                p1 = pygame.transform.rotozoom(self.image, self.rotation, self.scale)
                p = pygame.transform.rotozoom(piece.image, piece.rotation, piece.scale)
                if self.x < piece.x + p.get_rect().width and self.x + p1.get_rect().width > piece.x:
                    if self.y < piece.y + p.get_rect().height and self.y + p1.get_rect().height > piece.y:
                        playedPieces.append(random.choice(pieces))
                        return True
        if self.y >= 750:
            playedPieces.append(random.choice(pieces))
            return True
        return False
pieces = [Piece("blue.png", 375, 50, 0, 0.3)]
playedPieces = [random.choice(pieces)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    playedPieces[-1].control()
    playedPieces[-1].collide()
    screen.fill((0, 0, 0))
    for piece in playedPieces:
        piece.draw()
    pygame.display.update()
pygame.quit()














