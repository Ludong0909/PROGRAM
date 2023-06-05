# -*- coding: utf-8 -*-

print('1. 想遊玩「打敗爛天氣」或「閃避紅方塊」請輸入數字「1」(需下載pygame)')
print('2. 想遊玩「我要活下去」,請輸入數字「2」(需下載numpy跟matplotlib套件)')
print('3. 還未下載套件者請輸入數字「3」查看下載步驟')
choice = input('請輸入數字:')

if choice == '1':
    # import packages needed in the game
    import math
    import pygame
    import random

    # initialize the game
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game Center')

    game_center_image = pygame.image.load('game_center.png')
    
    font_title = pygame.font.SysFont('Stsong', 64)
    weather_game_text = font_title.render('Beat the bad weather', True, (255, 255, 255))
    whe_text_width, whe_text_height = weather_game_text.get_size()
    whe_text_x = screen.get_width() / 4 - whe_text_width / 2 + 20
    whe_text_y = (screen.get_height() - whe_text_height) / 2 - 60
    wheather_game_rect = pygame.Rect(whe_text_x - 10, whe_text_y, whe_text_width + 15, whe_text_height)
    
    square_game_text = font_title.render('Watch out!', True, (255, 255, 255))
    squa_text_width, squa_text_height = square_game_text.get_size()
    squa_text_x = (3 * screen.get_width() / 4 - squa_text_width / 2) + 20
    square_game_rect = pygame.Rect(squa_text_x - 10, whe_text_y, squa_text_width + 15, whe_text_height)

    instruct_text = font_title.render('Instruction', True, (255, 255, 255))
    instruct_width, instruct_height = instruct_text.get_size()
    whe_instruct_rect = pygame.Rect(whe_text_x + 20, whe_text_y + 90, instruct_width + 20, instruct_height)
    squa_instruct_rect = pygame.Rect(squa_text_x - 10, whe_text_y + 90, squa_text_width + 15, instruct_height)

    time = 0
    choose = False
    clock = pygame.time.Clock()
    
    # Game Center
    running = True
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not choose:
            # reset first choice
            first_choice = True

            # game center image
            screen.blit(game_center_image, (0, 0))
            
            # Draw labels for users to choose
            # wheather game
            pygame.draw.rect(screen, (0, 0, 255), wheather_game_rect)
            screen.blit(weather_game_text, (whe_text_x, whe_text_y - 5))
            
            # wheather game instruction
            pygame.draw.rect(screen, (100, 100, 100), whe_instruct_rect)
            screen.blit(instruct_text, (whe_text_x + 30, whe_text_y + 85))
            
            # square game
            pygame.draw.rect(screen, (255, 0, 0), square_game_rect)
            screen.blit(square_game_text, (squa_text_x, whe_text_y - 5))

            # square game instruction
            pygame.draw.rect(screen, (100, 100, 100), squa_instruct_rect)
            screen.blit(instruct_text, (squa_text_x + 30, whe_text_y + 85))

            # Enter different interface by user's options
            mouse_position = pygame.mouse.get_pos()
            if whe_instruct_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
                choose = True
                choose_type = 1
            elif squa_instruct_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
                choose = True
                choose_type = 2
            elif wheather_game_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
                choose = True
                choose_type = 3
            elif square_game_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
                choose = True
                choose_type = 4


        # tornado instructions
        if choose and choose_type == 1:
            if first_choice:
                first_choice = False

                # Set the font properties
                font_size = 30
                font_color = (255, 255, 255)  # White color in RGB format

                # Create a font object
                font = pygame.font.Font(None, font_size)

                # Define the instructions
                instructions = [
                    "Welcome to the game!",
                    "Instructions:",
                    "You are a cloud, press the keys up, down, right, left (or WSAD) to move.",
                    "Do not touch the thunder, ocean and tornado! or you will die!",
                    "But the sun and rainbow is good! you can eat them.",
                    "If you eat three suns, a rainbow will appear.",
                    "If you eat a rainbow, the tornado will stop for a while.",
                    "Try to suvive as long as you can, good luck!",
                    "Enter Q on the keyboard to exit this page."
                ]

                # Create a list of text surfaces
                text_surfaces = []
                for line in instructions:
                    text_surfaces.append(font.render(line, True, font_color))

                # Calculate the vertical spacing between lines
                line_spacing = font_size // 2

                # Calculate the initial position to start rendering the text
                start_x = 800 // 2
                start_y = (600 - (len(text_surfaces) * font_size + (len(text_surfaces) - 1) * line_spacing)) // 2

            screen.fill((0, 0, 0))
            # Render and display the text surfaces
            for i, text_surface in enumerate(text_surfaces):
                text_x = start_x - text_surface.get_width() // 2
                text_y = start_y + (font_size + line_spacing) * i
                screen.blit(text_surface, (text_x, text_y))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                choose = False
            pygame.display.flip()


                # square instructions
        if choose and choose_type == 2:
            if first_choice:
                first_choice = False

                # Set the font properties
                font_size = 28
                font_color = (255, 255, 255)  # White color in RGB format

                # Create a font object
                font = pygame.font.Font(None, font_size)

                # Define the instructions
                instructions = [
                    "Welcome to the game!",
                    "Instructions:",
                    "You are the red square, press the keys up, down, right, left (or WSAD) to move.",
                    "Blue squares will spawn every few seconds and move towards you.",
                    "If you touch the blue squares then you'll die.",
                    "You will have a chance to attack every few seconds and the screen will turn green.",
                    "You need to press the 'space' on keyboard and press WSAD at the same time.",
                    "Then all the blue squares at that direction will be killed!",
                    "Try to suvive and kill more blue squares to win higher score.",
                    "Enter Q on the keyboard to exit this page."
                ]

                # Create a list of text surfaces
                text_surfaces = []
                for line in instructions:
                    text_surfaces.append(font.render(line, True, font_color))

                # Calculate the vertical spacing between lines
                line_spacing = font_size // 2

                # Calculate the initial position to start rendering the text
                start_x = 800 // 2
                start_y = (600 - (len(text_surfaces) * font_size + (len(text_surfaces) - 1) * line_spacing)) // 2

            screen.fill((0, 0, 0))
            # Render and display the text surfaces
            for i, text_surface in enumerate(text_surfaces):
                text_x = start_x - text_surface.get_width() // 2
                text_y = start_y + (font_size + line_spacing) * i
                screen.blit(text_surface, (text_x, text_y))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                choose = False
            pygame.display.flip()


        # tornado game
        if choose and choose_type == 3:
            if first_choice:
                first_choice = False    

                # Set Captions
                pygame.display.set_caption('Cloud')

                # Load cloud image and create main character
                cloud = pygame.image.load('cloud.png')
                cloud = pygame.transform.scale_by(cloud, 0.1)

                # Set elementary characteristic of cloud
                cloud_speed = 2.78
                cloud_position = [screen.get_width() // 2 - cloud.get_width() // 2, screen.get_height() // 2 - cloud.get_height() // 2]

                # Create ocean
                ocean_color = (0, 0, 255)
                ocean_width = screen.get_width()
                ocean_height = 0
                ocean_speed = 0.25

                # Create Thunder
                thunder = pygame.image.load('thunder.png')
                thunder = pygame.transform.scale_by(thunder, 0.1)
                thunder_speed = 2.5
                thunder_position = [random.randint(0, screen.get_width() - thunder.get_width()), screen.get_height()]

                # Create Sun
                sun = pygame.image.load('sun.png')
                sun = pygame.transform.scale_by(sun, 0.9)
                sun_position = [random.randint(0, screen.get_width() - sun.get_width()), random.randint(0, screen.get_height() - ocean_height - sun.get_height())]

                # Create Rainbow
                rainbow = pygame.image.load('rainbow.png')
                rainbow = pygame.transform.scale_by(rainbow, 0.1)
                rainbow_position = [-200, -200]

                # Create Tornado
                tornado = pygame.image.load('tornado.png')
                tornado = pygame.transform.scale_by(tornado, 0.2)
                tornado_position = [random.randint(0, screen.get_width() - tornado.get_width()), random.randint(0, screen.get_height() - tornado.get_height())]
                tornado_direction = [random.random() + 0.01, random.random() + 0.01]
                tornado_speed = 3.33

                # Game over image
                game_over_image = pygame.image.load('game_over.png')
                game_over_image = pygame.transform.scale(game_over_image, (screen.get_width(), screen.get_height()))

                # Countdown settings
                font_count = pygame.font.Font(None, 108)
                countdown_labels = [font_count.render(str(i), True, (255, 255, 255)) for i in range(3, 0, -1)]
                text_x, text_y = countdown_labels[0].get_size()
                text_x = (screen.get_width() - text_x) / 2
                text_y = (screen.get_height() - text_y) / 2
                countdown_timer = 0
                countdown_index = 0
                show_countdown = True
                current_time = 0
                end_timer = 0

                # Set timers
                sun_timer = 0
                sun_touch_times = 0
                tornado_timer = 300
                tornado_touch_times = 0
                sun_touch = False
                rainbow_touch = False
                rainbow_stay = False
                game_over = False


                # Functions of game
                def countdown():
                    global countdown_index, countdown_timer, show_countdown, start_time
                    countdown_timer += 1
                    screen.blit(countdown_labels[countdown_index], (text_x, text_y))
                    if countdown_timer % 60 == 0:
                        countdown_index += 1
                        if countdown_index == 3:
                            show_countdown = False
                            start_time = pygame.time.get_ticks()


                def final_screen():
                    global elapsed_time, restart_text, back_center_text, quit_text, squa_screen_width, squa_screen_height
                    # Fill the screen with black
                    screen.fill((0, 0, 0))
                    squa_screen_width, squa_screen_height = 800, 600

                    # Game Over !
                    font = pygame.font.Font(None, 36)  # Choose the font and size
                    game_over_text = font.render('Game Over !', True, (255, 255, 255))
                    screen.blit(game_over_text, (squa_screen_width // 2 - game_over_text.get_width() // 2, squa_screen_height // 2 - 50))
                    
                    # Calculate the final elapsed time in seconds 
                    final_time_text = font.render('Survival Time: ' + str(elapsed_time) + " seconds", True, (255, 255, 255))
                    screen.blit(final_time_text, (squa_screen_width // 2 - final_time_text.get_width() // 2, squa_screen_height // 2))

                    # Text
                    restart_text = font.render('Restart', True, (255, 0, 0))
                    back_center_text = font.render('Game Center', True, (255, 0, 0))
                    quit_text = font.render('Quit Game', True, (255, 0, 0))

                    # Fill color at the bottom of quit option
                    restart_rect = pygame.Rect(squa_screen_width // 2 - restart_text.get_width() // 2 - 180,
                                                squa_screen_height // 2 + 40,
                                                restart_text.get_width() + 20,
                                                restart_text.get_height() + 20)
                    back_center_rect = pygame.Rect(squa_screen_width // 2 - back_center_text.get_width() // 2 - 20, 
                                                    squa_screen_height // 2 + 40, restart_text.get_width() + 100,
                                                    restart_text.get_height() + 20)
                    quit_rect = pygame.Rect(squa_screen_width // 2 - quit_text.get_width() // 2 + 160,
                                            squa_screen_height // 2 + 40,
                                            quit_text.get_width() + 20,
                                            quit_text.get_height() + 20)
                    pygame.draw.rect(screen, (100, 100, 100), restart_rect)
                    pygame.draw.rect(screen, (100, 100, 100), back_center_rect)
                    pygame.draw.rect(screen, (100, 100, 100), quit_rect)

                    # Display restart and quit options
                    screen.blit(restart_text, (squa_screen_width // 2 - restart_text.get_width() // 2 - 170, squa_screen_height // 2 + 50))
                    screen.blit(back_center_text, (squa_screen_width // 2 - restart_text.get_width() // 2 - 40, squa_screen_height // 2 + 50))
                    screen.blit(quit_text, (squa_screen_width // 2 - quit_text.get_width() // 2 + 170, squa_screen_height // 2 + 50))


                game_over = False
                font_time = pygame.font.Font(None, 36)
                def update_time():
                    global current_time, elapsed_time
                    current_time += 1  # Get the current time in milliseconds
                    elapsed_time = current_time // 60  # Calculate the elapsed time in seconds
                    time_text = font_time.render('Time: ' + str(elapsed_time), True, (255, 255, 255))  # Render the time text surface
                    screen.blit(time_text, (10, 15))  # Blit the time text surface onto the screen


                def cloud_move():
                    if keys[pygame.K_w] or keys[pygame.K_UP]:
                        cloud_position[1] -= cloud_speed
                    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                        cloud_position[1] += cloud_speed
                    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                        cloud_position[0] -= cloud_speed
                    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                        cloud_position[0] += cloud_speed


                def thunder_move():
                    thunder_position[1] += thunder_speed
                    if thunder_position[1] > screen.get_height():
                        thunder_position[0] = random.randint(0, screen.get_width() - thunder.get_width())
                        thunder_position[1] = 0


                def sun_spawn():
                    global sun_position, sun_timer, sun_touch
                    sun_timer += 1
                    if sun_timer >=200 and sun_touch:
                        sun_timer = 0
                        sun_touch = False
                        sun_position[0] = random.randint(0, screen.get_width() - sun.get_width())
                        sun_position[1] = random.randint(0, int(screen.get_height() - ocean_height - sun.get_width()))
                    elif sun_timer >= 200 and not sun_touch:
                        sun_position[1] = -200
                        if sun_timer >= 300:
                            sun_timer = 0
                            sun_position[0] = random.randint(0, screen.get_width() - sun.get_width())
                            sun_position[1] = random.randint(0, int(screen.get_height() - ocean_height - sun.get_width()))


                def rainbow_spawn():
                    global rainbow_position, rainbow_stay, rainbow_touch, sun_touch_times
                    if tornado_touch_times >= 2 and sun_touch_times >= 3:
                        if rainbow_touch == False and rainbow_stay == False:
                            rainbow_position[0] = random.randint(0, screen.get_width() - rainbow.get_width())
                            rainbow_position[1] = random.randint(screen.get_height() - rainbow.get_height() - 100, screen.get_height() - rainbow.get_height())
                            rainbow_stay = True
                        elif rainbow_touch:
                            rainbow_position[0] = -200
                            rainbow_position[1] = -200
                            sun_touch_times = 0
                            rainbow_touch = False
                            rainbow_stay = False


                def tornado_move():
                    global tornado_direction, tornado_timer
                    tornado_timer += 1
                    if tornado_touch_times >= 2:
                        if rainbow_touch == False and tornado_timer >= 300:
                            if 0 > tornado_position[0] or  tornado_position[0] > screen.get_width() - tornado.get_width():
                                tornado_direction[0] *= -1
                            elif 0 > tornado_position[1] or  tornado_position[1] > screen.get_height() - tornado.get_height():
                                tornado_direction[1] *= -1
                            tornado_position[0] += tornado_direction[0] * tornado_speed
                            tornado_position[1] += tornado_direction[1] * tornado_speed
                        elif rainbow_touch:
                            tornado_timer = 0

            if not game_over:
                screen.fill((0, 0, 0))

                if show_countdown:
                    countdown()
                else:
                    keys = pygame.key.get_pressed()
                    update_time()
                    cloud_move()
                    thunder_move()
                    sun_spawn()
                    screen.blit(cloud, cloud_position)
                    screen.blit(thunder, thunder_position)
                    screen.blit(sun, sun_position)
                    screen.blit(rainbow, rainbow_position)
                    if tornado_touch_times >= 2:
                        screen.blit(tornado, tornado_position)
                    ocean_height += ocean_speed
                    pygame.draw.rect(screen, ocean_color, (0, screen.get_height() - ocean_height, screen.get_width(), ocean_height+10))
                    
                    # Create "Rect" to determine collisions
                    cloud_rect = cloud.get_rect(center=cloud_position)
                    thunder_rect = thunder.get_rect(center=thunder_position)
                    sun_rect = sun.get_rect(center=sun_position)
                    rainbow_rect = rainbow.get_rect(center=rainbow_position)       
                    tornado_rect = tornado.get_rect(center=tornado_position)

                    # Touch sun to return sea level to 0
                    if cloud_rect.colliderect(sun_rect):
                        ocean_height = 0
                        sun_touch = True
                        sun_timer = 0
                        sun_position[1] = -200
                        sun_touch_times += 1
                        tornado_touch_times += 1

                    # Touch rainbow to stop tornado
                    if cloud_rect.colliderect(rainbow_rect):
                        rainbow_touch = True
                    tornado_move()
                    rainbow_spawn()

                    # Game over when:
                    # Hit by thunder
                    if cloud_rect.colliderect(thunder_rect):
                        game_over = True
                    
                    # Blow by tornado
                    if tornado_touch_times >= 2:
                        if cloud_rect.colliderect(tornado_rect):
                            game_over = True
                    
                    # Submerge to the sea
                    if cloud_position[1] > screen.get_height() - ocean_height - cloud.get_height():
                        game_over = True
                    
                    # Touch the edge
                    if 0 > cloud_position[0] or cloud_position[0] > screen.get_width() - cloud.get_width():
                        game_over = True
                    if 0 > cloud_position[1] or cloud_position[1] > screen.get_height() - cloud.get_height():
                        game_over = True
            else:
                end_timer += 1
                if end_timer >= 180:
                    final_screen()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                        mouse_position = pygame.mouse.get_pos()
                        if restart_text.get_rect(x=squa_screen_width // 2 - restart_text.get_width() // 2 - 170,
                                                y=squa_screen_height // 2 + 50).collidepoint(mouse_position):
                        # Restart the game if the "Restart" option is clicked
                            cloud_position = [squa_screen_width // 2, squa_screen_width // 2] 
                            ocean_height = 0
                            countdown_timer = 0
                            countdown_index = 0
                            show_countdown = True
                            current_time = 0
                            end_timer = 0
                            game_over = False
                            sun_timer = 0
                            sun_touch_times = 0
                            tornado_timer = 300
                            tornado_touch_times = 0
                            sun_touch = False
                            rainbow_touch = False
                            rainbow_stay = False
                            game_over = False
                            rainbow_position = [-200, -200]
                            thunder_position = [random.randint(0, screen.get_width() - thunder.get_width()), 0]
                        elif back_center_text.get_rect(x=squa_screen_width // 2 - back_center_text.get_width() // 2 - 40,
                                                y=squa_screen_height // 2 + 50).collidepoint(mouse_position):
                            choose = False
                        elif quit_text.get_rect(x=squa_screen_width // 2 - quit_text.get_width() // 2 + 170,
                                                y=squa_screen_height // 2 + 50).collidepoint(mouse_position):
                            running = False
                        else:
                            screen.blit(game_over_image, (0, 0))
                else:
                    screen.blit(game_over_image, (0, 0))

        # Square game
        if choose and choose_type == 4:
            if first_choice:
                first_choice = False

                # Set Captions
                pygame.display.set_caption('Dodge')

                # Character properties
                squa_screen_width, squa_screen_height = 800, 600
                character_size = 20
                character_speed = 2.5
                character_color = (255, 0, 0)  # Red
                character_position = [800 // 2 - character_size // 2, squa_screen_height // 2 - character_size // 2]

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
                back_center_text = font.render('Game Center', True, (255, 0, 0))
                quit_text = font.render('Quit Game', True, (255, 0, 0))

                # Game loop
                running = True
                spawn_timer = 0
                attack_timer = 0

                def character_move():
                    if keys[pygame.K_w] or keys[pygame.K_UP]:
                        character_position[1] -= character_speed
                    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                        character_position[1] += character_speed
                    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                        character_position[0] -= character_speed
                    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
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
                    if character_position[0] > squa_screen_width or character_position[1] > squa_screen_height:
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
                    screen.blit(game_over_text, (squa_screen_width // 2 - game_over_text.get_width() // 2, squa_screen_height // 2 - 100))

                    # Display final score
                    final_score_text = font.render('Final Score: ' + str(kill), True, (255, 255, 255))
                    screen.blit(final_score_text, (squa_screen_width // 2 - final_score_text.get_width() // 2, squa_screen_height // 2 - 50))
                    
                    # Calculate the final elapsed time in seconds
                    elapsed_time = (end_time - start_time) // 1000  
                    final_time_text = font.render('Survival Time: ' + str(elapsed_time) + " seconds", True, (255, 255, 255))
                    screen.blit(final_time_text, (squa_screen_width // 2 - final_time_text.get_width() // 2, squa_screen_height // 2))

                    # Fill color at the bottom of quit option
                    restart_rect = pygame.Rect(squa_screen_width // 2 - restart_text.get_width() // 2 - 180,
                                                squa_screen_height // 2 + 40,
                                                restart_text.get_width() + 20,
                                                restart_text.get_height() + 20)
                    back_center_rect = pygame.Rect(squa_screen_width // 2 - back_center_text.get_width() // 2 - 20, 
                                                    squa_screen_height // 2 + 40, restart_text.get_width() + 100,
                                                    restart_text.get_height() + 20)
                    quit_rect = pygame.Rect(squa_screen_width // 2 - quit_text.get_width() // 2 + 160,
                                            squa_screen_height // 2 + 40,
                                            quit_text.get_width() + 20,
                                            quit_text.get_height() + 20)
                    pygame.draw.rect(screen, (100, 100, 100), restart_rect)
                    pygame.draw.rect(screen, (100, 100, 100), back_center_rect)
                    pygame.draw.rect(screen, (100, 100, 100), quit_rect)

                    # Display restart and quit options
                    screen.blit(restart_text, (squa_screen_width // 2 - restart_text.get_width() // 2 - 170, squa_screen_height // 2 + 50))
                    screen.blit(back_center_text, (squa_screen_width // 2 - restart_text.get_width() // 2 - 40, squa_screen_height // 2 + 50))
                    screen.blit(quit_text, (squa_screen_width // 2 - quit_text.get_width() // 2 + 170, squa_screen_height // 2 + 50))

            if game_state == GAME_STATE_GAME_OVER and event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                mouse_position = pygame.mouse.get_pos()
                if restart_text.get_rect(x=squa_screen_width // 2 - restart_text.get_width() // 2 - 170,
                                            y=squa_screen_height // 2 + 50).collidepoint(mouse_position):
                    # Restart the game if the "Restart" option is clicked
                    kill = 0
                    enemies.clear()
                    game_state = GAME_STATE_PLAYING
                    start_time = pygame.time.get_ticks()
                    character_position = [squa_screen_width // 2 - character_size // 2, squa_screen_height // 2 - character_size // 2]
                elif back_center_text.get_rect(x=squa_screen_width // 2 - back_center_text.get_width() // 2 - 40,
                                            y=squa_screen_height // 2 + 50).collidepoint(mouse_position):
                    choose = False
                elif quit_text.get_rect(x=squa_screen_width // 2 - quit_text.get_width() // 2 + 170,
                                            y=squa_screen_height // 2 + 50).collidepoint(mouse_position):
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
        pygame.display.flip()
    pygame.quit()

elif choice == '2':
    import class_and_function as c
    import numpy as np 
    import matplotlib.pyplot as mp 

    # Opening
    print('Hello! We are group 43 of Programming of Business Computing!')
    name = input('Welcome to the survial game! Input your character name please: ')

    # Print_delay_time setting
    delay_time_1 = 0.008
    delay_time_2 = 0.03

    # Introduction and instruction
    c.print_with_delay('===================Rule instruction===================',delay_time_1)
    c.print_with_delay('Hello, '+name+'. You are trapped on an isolated island.',delay_time_2)
    c.print_with_delay('You need to try to survive on this island by yourself and survive more day as possible as you can. Try your best to survive on this dangerous place!',delay_time_2)
    print('')
    c.print_with_delay('===================Resource instruction===================',delay_time_1)
    c.print_with_delay('From now on, you have to collect and use 4 kind of resources: water, food, material and medkit.',delay_time_2)
    c.print_with_delay('Water and food can help you increase your body state.',delay_time_2)
    c.print_with_delay('If your shelter is damaged, you\'ll need material to repair it.',delay_time_2)
    c.print_with_delay('If your health points drop, you can use medkit to heal yourself.',delay_time_2)
    print('')
    c.print_with_delay('===================Action instruction===================',delay_time_1)
    c.print_with_delay('You can take an action everyday.',delay_time_2)
    c.print_with_delay('1. If you go to explore, you can get some resources but you\'ll feel thirsty and hungry. Meanwhile the durability of your shelter will decrease too.',delay_time_2)
    c.print_with_delay('2. If you decide to repair your shelter today, you\'ll consume 20 materials and your shelter\'s durability will increase 15 points. Your state will drop also.',delay_time_2)
    c.print_with_delay('3. You can also do nothing today, but every state will drop slightly.',delay_time_2)
    print('')
    c.print_with_delay('===================Weather instruction===================',delay_time_1)
    c.print_with_delay('There are 4 kinds of weather on this island: Sunny, cloudy, thunderstrom and cold.',delay_time_2)
    c.print_with_delay('If it\'s sunny, you\'ll waste more thirst if you go out to explore or repair your shelter.',delay_time_2)
    c.print_with_delay('If it\'s cloudy, nothing will happen.',delay_time_2)
    c.print_with_delay('If it\'s thunderstrom, your thirst will add to 100 directly but you can\'t go out to explore today. Meanwhile, your shelter will drop more durability if you do nothing.',delay_time_2)
    c.print_with_delay('If it\'s cold, your hunger will drop more. But your thirst will drop less.',delay_time_2)
    print('')
    c.print_with_delay('===================Supply instruction===================',delay_time_1)
    c.print_with_delay('Don\'t forget that you can use food/water/medkit at the beginning of the day.',delay_time_2)
    c.print_with_delay('Food will increase your hunger 18 points, water will increase your thirst 15 points, and medkit will increase your health 20 points.',delay_time_2)
    print('')
    c.print_with_delay('======================================================',delay_time_1)
    c.print_with_delay('If your hunger or thirst is lower than 40, then your health will start to drop.',delay_time_2)
    c.print_with_delay('If your shelter durability or your health drop to 0, you\'ll die and lose the game.',delay_time_2)
    c.print_with_delay('Try your best to survive on this island!',delay_time_2)
    c.print_with_delay('You can start the game after you read all the instructions, Good luck!',delay_time_2)

    # Initial survival state
    alive = True 
    shelter = True
    health = 100
    thirst = 100
    hunger = 100
    shelter_hp = 100 
    day = 0

    # Initial supplies
    medkit = c.medkit(1)
    food = c.food(2)
    water = c.water(4)
    material = c.material(12)

    # Weather system
    weather = ['Sunny','Thunderstorm','Cold','Cloudy']

    # Create arrays for plotting below
    medkit_quantity = []
    water_quantity = []
    food_quantity = []
    material_quantity = []
    health_array = []
    thirst_array = []
    hunger_array = []
    shelter_health_array = []

    # Main loop 
    while alive and shelter:
        day = day + 1 
        today_weather = c.random_weather(weather)
        print('===============Day '+str(day)+'===============')
        print('It\'s '+today_weather+' today!')
        if today_weather == 'Thunderstorm':
            thirst = 100

        c.print_with_delay('-----Current state-----',delay_time_2)
        print('Health: '+str(health))
        print('Thirst: '+str(thirst))
        print('Hunger: '+str(hunger))
        print('Shelter durability: '+str(shelter_hp))
        c.print_with_delay('-----Current resources-----',delay_time_2)
        print('Water: '+str(water.get_quantity()))
        print('Food: '+str(food.get_quantity()))
        print('Material: '+str(material.get_quantity()))
        print('Medkit: '+str(medkit.get_quantity()))
        
        while True: # Supplies consuming 
            print('-----------------------------------------------')
            print('What supplies do you want to use? ')
            print('=====Using supplies=====')
            print('1: Water')
            print('2: Food')
            print('3: Medkit')    
            print('4: No need to use now')
            print('5: Show current state')
            print('6: Show current resources')
            action = input('Please input number 1 ~ 6: ')
            if action.isdigit() == False:
                print('Wrong input!')
                continue
            elif action == '1' and water.get_quantity() > 0:
                water.consume_water(1)
                thirst = thirst + 15
                if thirst >= 100:
                    thirst = 100
                print('Your thirst now is '+str(thirst)+'.')
            elif action == '2' and food.get_quantity() > 0:
                food.consume_food(1)
                hunger = hunger + 18
                if hunger >= 100:
                    hunger = 100
                print('Your hunger now is '+str(hunger)+'.')
            elif action == '3' and medkit.get_quantity() > 0:
                medkit.consume_medkit(1)
                health = health + 20
                if health >= 100:
                    health = 100
                print('Your health now is '+str(health)+'.')
            elif action == '4':
                break
            elif action == '5':
                c.print_with_delay('-----Current state-----',delay_time_1)
                print('Health: '+str(health))
                print('Thirst: '+str(thirst))
                print('Hunger: '+str(hunger))
                print('Shelter durability: '+str(shelter_hp))
            elif action == '6':
                c.print_with_delay('-----Current resources-----',delay_time_1)
                print('Water: '+str(water.get_quantity()))
                print('Food: '+str(food.get_quantity()))
                print('Material: '+str(material.get_quantity()))
                print('Medkit: '+str(medkit.get_quantity()))
            else:
                print('Wrong input or you don\'t have enough supplies!')
                continue

        while True: # Today's action
            c.print_with_delay('What action you want to take today?',delay_time_2)
            c.print_with_delay('1: Go out to explore.',delay_time_1)
            c.print_with_delay('2: Repair shelter.',delay_time_1)
            c.print_with_delay('3: Nothing.',delay_time_1)
            action = input('Please input number 1 ~ 3: ')
            if action == '1':
                if today_weather == 'Thunderstorm':
                    c.print_with_delay('You can\'t go out to explore when the weather is thunderstorm!',delay_time_1)
                    continue
                food.add_food(c.random_number(1,2))
                water.add_water(c.random_number(1,3))
                medkit.add_medkit(c.random_number(0,1))
                material.add_material(c.random_number(10,18))
                if today_weather == 'Sunny':
                    hunger = hunger - c.random_number(15,25)
                    thirst = thirst - c.random_number(25,35)
                    shelter_hp = shelter_hp - c.random_number(10,20)   
                    break
                elif today_weather == 'Cold':
                    hunger = hunger - c.random_number(25,30)
                    thirst = thirst - c.random_number(10,15)
                    shelter_hp = shelter_hp - c.random_number(10,20)   
                    break
                hunger = hunger - c.random_number(15,25)
                thirst = thirst - c.random_number(20,25)
                shelter_hp = shelter_hp - c.random_number(10,20)
                break
            elif action == '2' and material.get_quantity() >= 20:
                material.consume_material(20)
                shelter_hp = shelter_hp + 15
                if shelter_hp >= 100:
                    shelter_hp = 100
                if today_weather == 'Sunny':
                    hunger = hunger - c.random_number(12,25)
                    thirst = thirst - c.random_number(25,35)  
                    break
                if today_weather == 'Cold':
                    hunger = hunger - c.random_number(25,30)
                    thirst = thirst - c.random_number(10,15)
                hunger = hunger - c.random_number(12,25)
                thirst = thirst - c.random_number(15,25)
                break
            elif action == '3':
                if today_weather == 'Thunderstorm':
                    hunger = hunger - c.random_number(10,18)
                    shelter_hp = shelter_hp - c.random_number(20,30)
                    break
                if today_weather == 'Cold':
                    hunger = hunger - c.random_number(20,25)
                    thirst = thirst - c.random_number(8,15)
                    shelter_hp = shelter_hp - c.random_number(10,15)
                    break
                hunger = hunger - c.random_number(10,20)
                thirst = thirst - c.random_number(15,20)
                shelter_hp = shelter_hp - c.random_number(10,15)
                break
            else:
                print('Wrong input or you don\'t have enough material!')
                continue
        
        # Lower limit of state
        if hunger < 0:
            hunger = 0
        if thirst < 0:
            thirst = 0

        # Health decreasing
        if thirst <= 10 or hunger <= 10:
            health = health - c.random_number(25,30)
        elif (thirst <= 20 and thirst > 10) or (hunger <= 20 and hunger > 10):
            health = health - c.random_number(20,25)
        elif (thirst <= 30 and thirst > 20) or (hunger <= 30 and hunger > 20):
            health = health - c.random_number(15,20)
        elif (thirst <= 40 and thirst > 30) or (hunger <= 40 and hunger > 30):
            health = health - c.random_number(10,15)
            
        # Condition for losing game 
        if health <= 0:
            c.print_with_delay('You died...',delay_time_2)
            alive = False
        if shelter_hp <= 0:
            c.print_with_delay('Your shelter has been destroyed.',delay_time_2)
            shelter = False
        
        # Collect data (unit:[day])
        medkit_quantity.append(medkit.get_quantity())
        water_quantity.append(water.get_quantity())
        food_quantity.append(food.get_quantity())
        material_quantity.append(material.get_quantity())
        health_array.append(health)
        thirst_array.append(thirst)
        hunger_array.append(hunger)
        shelter_health_array.append(shelter_hp)

        continue

    x = np.linspace(1,day,day)
    f,(ax1,ax2) = mp.subplots(1,2,figsize=(15,9))

    ax1.grid(color='tab:grey',linestyle=':',linewidth=0.5)
    ax1.plot(x,health_array,color='tab:red')
    ax1.plot(x,thirst_array,color='tab:blue')
    ax1.plot(x,hunger_array,color='tab:orange')
    ax1.plot(x,shelter_health_array,color='green')
    ax1.set_xticks(np.linspace(1,day,day))
    ax1.set_yticks(np.linspace(0,100,11))
    ax1.set_xlim([1,day])
    ax1.set_ylim([-5,101])
    ax1.legend(['Health','Thirst','Hunger','Shelter durability'],loc='lower left')
    ax1.set_xlabel('Day',fontsize=15)
    ax1.set_ylabel('Value',fontsize=15)

    ax2.grid(color='tab:grey',linestyle=':',linewidth=0.5)
    ax2.plot(x,medkit_quantity,color='tab:red')
    ax2.plot(x,water_quantity,color='tab:blue')
    ax2.plot(x,food_quantity,color='tab:orange')
    ax2.plot(x,material_quantity,color='green')
    ax2.set_xticks(np.linspace(1,day,day))
    ax2.set_xlim([1,day])
    ax2.set_ylim([-0.2,max(material_quantity)])
    ax2.legend(['Medkit','Water','Food','Material'],loc='best')
    ax2.set_xlabel('Day',fontsize=15)
    ax2.set_ylabel('Quantity',fontsize=15)
    f.suptitle('Evolution of your gaming data',x=0.5,y=0.92,fontsize=18)
    mp.show()

elif choice == '3':
    print('\n如為pip環境請在終端機直接輸入"pip install pygame"即可')
    print('終端機在底下工具列直接搜尋「cmd」即可找到\n')
    print('Anaconda環境則在Anaconda Powershell的終端機先輸入"conda install pip"')
    print('接著再"pip install pygame"即可使用')
    print('Anaconda Powershell 同樣在底下工具列搜尋即可找到')

else:
    print('輸入錯誤!請輸入「1」,「2」,或「3」來選擇!')