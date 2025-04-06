import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800   # Setting window resolution (can be adjusted for your device specification)
FPS = 60                    # Simply describe frame per second
PLAYER_VELOCITY = 5         # The speed of player

window = pygame.display.set_mode((WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):  # Player is the most complicated aspect of the game, there is a lot of movement wi
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)  # Making easier to move player
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):
        """Move the player by dx, dy."""
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.rect.x = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.rect.x = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        """Every frame the loop updating Player stats by moving, updating animation and so on"""
        self.move(self.x_velocity, self.y_velocity)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)



def get_background(name):
    image = pygame.image.load(join('assets', 'Background', name))  # Get background by provided name and static dir path
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):  # How many tiles need to fill the full screen
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)  # Draw window tile by tile with provided image and position

    player.draw(window)

    pygame.display.update()  # Updating the screen needed every frame to ensure we d`ont have old draws still on


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background('Pink.png')

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)  # Ensure for power machines, that FPS will not go ahead of set FPS

        for event in pygame.event.get():  # Checking events of pygame
            if event.type == pygame.QUIT:  # Quitting the game
                run = False
                break

        draw(window, background, bg_image, player)
    pygame.quit()  # Quit pygame
    quit()  # Quit python program


if __name__ == '__main__':
    main(window)
