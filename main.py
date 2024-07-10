import pygame
import random

pygame.init()
screen = pygame.display.set_mode((720, 720), pygame.RESIZABLE)
pygame.display.set_caption('Square.io')
clock = pygame.time.Clock()
running = True
dt = 0

height = 25
width = 25
border_width = int(height / 6)
player_rect = pygame.Rect(360 - width/2, 360 - height/2, width, height)
border_rect = pygame.Rect(360 - width/2 - border_width/2, 360 - height/2 - border_width/2, width + border_width, height + border_width)
player_vel = 60
player_color = (random.randrange(250), random.randrange(250), random.randrange(250))

food_color = (random.randrange(250), random.randrange(250), random.randrange(250))
food_pos = (random.randrange(screen.get_width()), random.randrange(screen.get_height()))

eat_sound = pygame.mixer.Sound("eat_sound.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

bomb_sprite = pygame.image.load("bomb.png")
bomb_sprite = pygame.transform.scale(bomb_sprite, (50, 50))

bomb_pos = (-100, -100)
bomb_pos_2 = (-100, -100)
bomb_pos_3 = (-100, -100)
bomb_pos_4 = (-100, -100)
bomb_pos_5 = (-100, -100)

score = 0

font_info = pygame.font.SysFont('Comic Sans MS', 30)
font_gameOver = pygame.font.SysFont('Comic Sans MS', 100)
font_score = pygame.font.SysFont('Comic Sans MS', 75)

text_gameOver = font_gameOver.render("Game Over", True, (0, 0, 0))
text_gameOver_rect = text_gameOver.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 40))

counter = 100
timer = str(counter).rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1
            timer = str(counter).rjust(3) if counter > 0 else '0'
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    screen.blit(font_info.render("Score: " + str(score), True, (0, 0, 0)), (50, 25))
    screen.blit(font_info.render("Time: " + timer, True, (0, 0, 0)), (screen.get_width() - 120 - 50, 25))

    bomb = screen.blit(bomb_sprite, bomb_pos)
    bomb_2 = screen.blit(bomb_sprite, bomb_pos_2)
    bomb_3 = screen.blit(bomb_sprite, bomb_pos_3)
    bomb_4 = screen.blit(bomb_sprite, bomb_pos_4)
    bomb_5 = screen.blit(bomb_sprite, bomb_pos_5)

    food = pygame.draw.circle(screen, food_color, food_pos, 10, 10)
    player = pygame.draw.rect(screen, player_color, player_rect)
    border = pygame.draw.rect(screen, "black", border_rect, border_width, 2 * border_width)

    if player.colliderect(food):

        pygame.mixer.Sound.play(eat_sound)

        player_vel += 5
        height += 5
        width += 5

        player_rect = pygame.Rect(player.x, player.y, width, height)
        border_rect = pygame.Rect(border.x, border.y, width + border_width, height + border_width)
        food_color = (random.randrange(250), random.randrange(250), random.randrange(250))
        food_pos = (random.randrange(screen.get_width()), random.randrange(screen.get_width()))

        score += 10

        text = font_info.render("Score: " + str(score), True, (0, 0, 0))

        # For debugging
        print(food.x, food.y)

    if player.colliderect(bomb) or player.colliderect(bomb_2) or player.colliderect(bomb_3) or player.colliderect(bomb_4) or player.colliderect(bomb_5):
        pygame.mixer.Sound.play(explosion_sound)
        counter = -1
        bomb_pos = (-100, -100)
        bomb_pos_2 = (-100, -100)
        bomb_pos_3 = (-100, -100)
        bomb_pos_4 = (-100, -100)
        bomb_pos_5 = (-100, -100)

    if pygame.time.get_ticks() % 500 == 0:
        bomb_pos = (random.randrange(screen.get_width()), random.randrange(screen.get_height()))
        screen.blit(bomb_sprite, bomb_pos)

    if pygame.time.get_ticks() % 500 == 100:
        bomb_pos_2 = (random.randrange(screen.get_width()), random.randrange(screen.get_height()))
        screen.blit(bomb_sprite, bomb_pos_2)

    if pygame.time.get_ticks() % 500 == 200:
        bomb_pos_3 = (random.randrange(screen.get_width()), random.randrange(screen.get_height()))
        screen.blit(bomb_sprite, bomb_pos_3)

    if pygame.time.get_ticks() % 500 == 300:
        bomb_pos_4 = (random.randrange(screen.get_width()), random.randrange(screen.get_height()))
        screen.blit(bomb_sprite, bomb_pos_4)

    if pygame.time.get_ticks() % 500 == 400:
        bomb_pos_5 = (random.randrange(screen.get_width()), random.randrange(screen.get_height()))
        screen.blit(bomb_sprite, bomb_pos_5)

    text_score = font_score.render("Your score is " + str(score), True, (0, 0, 0))
    text_score_rect = text_score.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 40))

    if counter < 0:
        screen.blit(text_gameOver, text_gameOver_rect)
        screen.blit(text_score, text_score_rect)

    if counter > 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_rect.y -= player_vel * dt
            border_rect.y -= player_vel * dt
        if keys[pygame.K_s]:
            player_rect.y += player_vel * dt
            border_rect.y += player_vel * dt
        if keys[pygame.K_a]:
            player_rect.x -= player_vel * dt
            border_rect.x -= player_vel * dt
        if keys[pygame.K_d]:
            player_rect.x += player_vel * dt
            border_rect.x += player_vel * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
