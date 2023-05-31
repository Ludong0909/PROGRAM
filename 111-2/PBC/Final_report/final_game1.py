import math
import pygame
import random

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dodging')

# Character properties
character_size = 20
character_speed = 2.5
character_color = (255, 0, 0)  # Red
character_position = [width // 2 - character_size // 2, height // 2 - character_size // 2]

# Enemy properties
enemy_size = 16
enemy_color = (0, 0, 255)  # Blue
enemy_speed = 2
enemies = []

# Score and Time
kill = 0
start_time = pygame.time.get_ticks()  # Get the initial time in milliseconds
font = pygame.font.Font(None, 36)  # Choose the font and size

# Game states
GAME_STATE_PLAYING = 0
GAME_STATE_GAME_OVER = 1
game_state = GAME_STATE_PLAYING
restart_text = font.render('Restart', True, (255, 0, 0))
quit_text = font.render('  Quit  ', True, (255, 0, 0))

# Game loop
running = True
spawn_timer = 0
attack_timer = 0
clock = pygame.time.Clock()


def character_move():
    if keys[pygame.K_w]:
        character_position[1] -= character_speed
    if keys[pygame.K_s]:
        character_position[1] += character_speed
    if keys[pygame.K_a]:
        character_position[0] -= character_speed
    if keys[pygame.K_d]:
        character_position[0] += character_speed


def move_towards_character(enemy):
    dx = character_position[0] - enemy.x
    dy = character_position[1] - enemy.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    dx = dx / distance
    dy = dy / distance
    enemy.x += dx * enemy_speed + 4 * (random.random() - 0.5) * enemy_speed
    enemy.y += dy * enemy_speed + 4 * (random.random() - 0.5) * enemy_speed


def spawn_enemy():
    r = random.randint(100 + int(enemy_size / 2), 150 + int(enemy_size / 2))
    r_angle = 2 * math.pi * random.random()
    x = character_position[0] + int(r * math.cos(r_angle))
    y = character_position[1] + int(r * math.sin(r_angle))
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))


def check_collision():
    for enemy in enemies:
        if character_rect.colliderect(enemy):
            return True
    if character_position[0] < 0 or character_position[1] < 0:
        return True
    if character_position[0] > width or character_position[1] > height:
        return True
    return False


def update_score():
    score_text = font.render('Kill: ' + str(kill), True, (255, 255, 255))  # Render the text surface
    screen.blit(score_text, (10, 10))  # Blit the text surface onto the screen


def update_time():
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
    elapsed_time = (current_time - start_time) // 1000  # Calculate the elapsed time in seconds
    time_text = font.render('Time: ' + str(elapsed_time), True, (255, 255, 255))  # Render the time text surface
    screen.blit(time_text, (10, 50))  # Blit the time text surface onto the screen


def update_cd():
    global attack_timer
    if attack_timer < 3600:
        cd_text = font.render('CD: ' + str(round((3600 - attack_timer) / 600, 1)), True, (255, 255, 255))
    else:
        cd_text = font.render('CD: 0', True, (255, 255, 255))
    screen.blit(cd_text, (10, 90))


def attack():
    global kill
    for enemy in enemies[::-1]:
        x, y = enemy.x - character_position[0], enemy.y - character_position[1]
        if keys[pygame.K_w]:
            if abs(y) > abs(x) and y < 0:
                enemies.remove(enemy)
                kill += 1
        elif keys[pygame.K_a]:
            if abs(x) > abs(y) and x < 0:
                enemies.remove(enemy)
                kill += 1
        elif keys[pygame.K_s]:
            if abs(y) > abs(x) and y > 0:
                enemies.remove(enemy)
                kill += 1
        elif keys[pygame.K_d]:
            if abs(x) > abs(y) and x > 0:
                enemies.remove(enemy)
                kill += 1


def game_over_screen():
    global game_state, running, start_time

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Game Over !
    game_over_text = font.render('Game Over !', True, (255, 255, 255))
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 100))

    # Display final score
    final_score_text = font.render('Final Score: ' + str(kill), True, (255, 255, 255))
    screen.blit(final_score_text, (width // 2 - final_score_text.get_width() // 2, height // 2 - 50))
    
    # Calculate the final elapsed time in seconds
    elapsed_time = (end_time - start_time) // 1000  
    final_time_text = font.render('Survival Time: ' + str(elapsed_time) + " seconds", True, (255, 255, 255))
    screen.blit(final_time_text, (width // 2 - final_time_text.get_width() // 2, height // 2))

    # Fill color at the bottom of quit option
    restart_rect = pygame.Rect(width // 2 - restart_text.get_width() // 2 - 10,
                               height // 2 + 40,
                               restart_text.get_width() + 20,
                               restart_text.get_height() + 20)
    quit_rect = pygame.Rect(width // 2 - quit_text.get_width() // 2 - 10,
                            height // 2 + 90,
                            quit_text.get_width() + 20,
                            quit_text.get_height() + 20)
    pygame.draw.rect(screen, (100, 100, 100), restart_rect)
    pygame.draw.rect(screen, (100, 100, 100), quit_rect)

    # Display restart and quit options
    screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 50))
    screen.blit(quit_text, (width // 2 - quit_text.get_width() // 2, height // 2 + 100))


while running:
    for event in pygame.event.get():
        if game_state == GAME_STATE_GAME_OVER and event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouse_position = pygame.mouse.get_pos()
            if restart_text.get_rect(x=width // 2 - restart_text.get_width() // 2,
                                        y=height // 2 + 50).collidepoint(mouse_position):
                # Restart the game if the "Restart" option is clicked
                kill = 0
                enemies.clear()
                game_state = GAME_STATE_PLAYING
                start_time = pygame.time.get_ticks()
                character_position = [width // 2 - character_size // 2, height // 2 - character_size // 2]
            elif quit_text.get_rect(x=width // 2 - quit_text.get_width() // 2,
                                    y=height // 2 + 100).collidepoint(mouse_position):
                # Quit the game if the "Quit" option is clicked
                running = False

    if game_state == GAME_STATE_PLAYING:
        # Keyboard input
        keys = pygame.key.get_pressed()
        character_move()

        # set cd of attack it reset after using it
        attack_timer += clock.tick(60)
        if attack_timer >= 3600:
            screen.fill((0, 255, 0))
            if keys[pygame.K_SPACE]:
                attack()
                attack_timer = 0
        else:
            screen.fill((0, 0, 0))

        # Spawn enemies randomly
        spawn_timer += clock.tick(60)  # Limit the frame rate to 60 FPS
        if spawn_timer >= 1000:
            spawn_enemy()  # Spawn an enemy every 1.5 second
            spawn_timer = 0

        # Move enemies towards the character
        for enemy in enemies:
            move_towards_character(enemy)

        # Check for collision with enemies
        character_rect = pygame.Rect(character_position[0], character_position[1], character_size, character_size)
        if check_collision():
            game_state = GAME_STATE_GAME_OVER
            end_time = pygame.time.get_ticks()  # Get the time when the game ends

        # Draw the character and enemies to update their positions on screen
        pygame.draw.rect(screen, character_color, (character_position, (character_size, character_size)))
        for enemy in enemies:
            pygame.draw.rect(screen, enemy_color, enemy)

        # Update time, score and cd
        update_score()
        update_time()
        update_cd()
    else:
        game_over_screen()

    pygame.display.flip()  # Update the display

pygame.quit()