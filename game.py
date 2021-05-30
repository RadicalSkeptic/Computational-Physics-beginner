import os
import pygame
import sys
import random

pygame.init()

speed = 5
width = 800
height = 600
x = width/2-25
y = height-50
player_pos = [x, y]
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
player_size = 50
enemy_size = 50
enemy_pos = [random.randint(0, width-enemy_size), 0]
enemy_list = []
screen = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont("monospace", 20)
clock = pygame.time.Clock()
game_over = False
i = 0
score = 0


def drop_enemies(enemy_list):
    if len(enemy_list) < 10:
        x_pos = random.randint(0, width-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(
            screen, blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def detect_collision(player_pos, enemy_pos):
    px = player_pos[0]
    py = player_pos[1]
    ex = enemy_pos[0]
    ey = enemy_pos[1]

    if ex > px and ex < (px+player_size) or px > ex and px < (ex+enemy_size):
        if ey > py and ey < (py+player_size) or py > ey and py < (ey+enemy_size):
            return True
    return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_pos[0] -= 40
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += 40
    screen.fill(black)
    for enemy_pos in enemy_list:
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:
            enemy_pos[1] += (speed+i/200)/2
        else:
            enemy_pos[0] = random.randint(0, width-enemy_size)
            enemy_pos[1] = 0
            score += 1
    clock.tick(60)

    text = "Score:" + str(score)
    label = myfont.render(text, True, 'white')
    screen.blit(label, dest=(width-150, height-50))

    if i % 50 == 0:
        drop_enemies(enemy_list)
    draw_enemies(enemy_list)
    pygame.draw.rect(
        screen, red, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.update()
    i += 1
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            game_over = True
os.system('cls')
print("GAME OVER")
print("Score:", score)
