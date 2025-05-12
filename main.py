# main.py
import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("끼끼귀신의 저택")
clock = pygame.time.Clock()

# 귀신 이미지 로드
ghost_ra = pygame.image.load("assets/sprites/ghost_ra_naeng.png")
ghost_ju = pygame.image.load("assets/sprites/ghost_ju_naeng.png")

# 사운드
kiki_sound = pygame.mixer.Sound("assets/sounds/kiki_jump.wav")

font = pygame.font.SysFont("malgungothic", 36)
appear = False
timer = 0

while True:
    screen.fill((20, 20, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not appear:
        timer += 1
        if timer > random.randint(300, 600):
            appear = True
            kiki_sound.play()
            timer = 0
    else:
        ghost = ghost_ra if random.choice([True, False]) else ghost_ju
        screen.blit(ghost, (random.randint(100, 600), random.randint(100, 400)))
        appear = False

    msg = font.render("라냉이랑 쥬냉이 귀신이 놀러와요...♡", True, (255, 180, 180))
    screen.blit(msg, (180, 540))

    pygame.display.update()
    clock.tick(60)
