# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:47:26 2023

@author: 安柔
"""
import pyglet
import random
import time

# Set up the game window
window = pyglet.window.Window(width=800, height=600)
label = pyglet.text.Label('Time:0', font_size=25, x=20, y=560)  # Create a label for the timer
start_time = None
start = True

# Load cloud image
cloud_image = pyglet.image.load('cloud.png')
# Scale the cloud image
cloud_scale = 0.1  # Change the scale factor as desired
cloud_image = cloud_image.get_region(0, 0, cloud_image.width, cloud_image.height).get_texture()
cloud_image.width = int(cloud_image.width * cloud_scale)
cloud_image.height = int(cloud_image.height * cloud_scale)
# Create cloud sprite
cloud_sprite = pyglet.sprite.Sprite(cloud_image)
# Set the initial position of the cloud
cloud_sprite.x = window.width // 2 - cloud_sprite.width // 2
cloud_sprite.y = window.height // 2 - cloud_sprite.height // 2
# Set the cloud movement speed and distance
cloud_speed = 500  # Change the speed as desired (pixels per second)
cloud_distance = 3  # Change the distance as desired (pixels)

# Create ocean rectangle
ocean_color = (0, 0, 255)  # Blue color
ocean_width = window.width
ocean_height = 0
ocean_x = 0
ocean_y = 0
# Set the ocean growth speed
ocean_growth_speed = 15  # Change the growth speed as desired (pixels per second)

# Create thunder sprite
thunder_image = pyglet.image.load('thunder.png')
# Scale the thunder image
thunder_scale = 0.1  # Change the scale factor as desired
thunder_image = thunder_image.get_region(0, 0, thunder_image.width, thunder_image.height).get_texture()
thunder_image.width = int(thunder_image.width * thunder_scale)
thunder_image.height = int(thunder_image.height * thunder_scale)
# Create initial thunder sprite
thunder_sprite = pyglet.sprite.Sprite(thunder_image)
thunder_sprite.x = random.randint(0, window.width - thunder_sprite.width)
thunder_sprite.y = window.height
# Set the thunder fall speed
thunder_speed = 150  # Change the speed as desired (pixels per second)

# Create sun sprite
sun_image = pyglet.image.load('sun.png')
# Scale the sun image
sun_scale = 0.9  # Change the scale factor as desired
sun_image = sun_image.get_region(0, 0, sun_image.width, sun_image.height).get_texture()
sun_image.width = int(sun_image.width * sun_scale)
sun_image.height = int(sun_image.height * sun_scale)
# Create initial sun sprite
sun_sprite = pyglet.sprite.Sprite(sun_image)
sun_sprite.x = random.randint(0, window.width - sun_sprite.width)
sun_sprite.y = random.randint(ocean_height, window.height - sun_sprite.height)

# Create rainbow sprite
rainbow_image = pyglet.image.load('rainbow.png')
# Scale the rainbow image
rainbow_scale = 0.1  # Change the scale factor as desired
rainbow_image = rainbow_image.get_region(0, 0, rainbow_image.width, rainbow_image.height).get_texture()
rainbow_image.width = int(rainbow_image.width * rainbow_scale)
rainbow_image.height = int(rainbow_image.height * rainbow_scale)
# Create initial rainbow sprite
rainbow_sprite = pyglet.sprite.Sprite(rainbow_image)
rainbow_sprite.x = -200
rainbow_sprite.y = -200

# Load tornado image
tornado_image = pyglet.image.load('tornado.png')
# Scale the tornado image
tornado_scale = 0.2  # Change the scale factor as desired
tornado_image = tornado_image.get_region(0, 0, tornado_image.width, tornado_image.height).get_texture()
tornado_image.width = int(tornado_image.width * tornado_scale)
tornado_image.height = int(tornado_image.height * tornado_scale)
# Create initial tornado
tornado_sprite = pyglet.sprite.Sprite(tornado_image)
tornado_sprite.x = random.randint(0, window.width - tornado_sprite.width)
tornado_sprite.y = random.randint(0, window.height - tornado_sprite.height)
tornado_speed = 200
tornado_direction_x = random.random() + 0.01
tornado_direction_y = random.random() + 0.01

# Load game over image
game_over_image = pyglet.image.load('game_over.png')
game_over_sprite = pyglet.sprite.Sprite(game_over_image)
game_over_sprite.x = window.width // 2 - game_over_sprite.width // 2
game_over_sprite.y = window.height // 2 - game_over_sprite.height // 2
game_over = False

# Countdown animation
countdown_labels = [pyglet.text.Label(str(i), font_size=72,
                                      x=window.width // 2, y=window.height // 2,
                                      anchor_x='center', anchor_y='center')
                    for i in range(3, 0, -1)]
countdown_index = 0
show_countdown = True
countdown_time = 1  # Time between countdown numbers

# Set timer and condition
sun_touch_times = 0
tornado_touch_times = 0
sun_timer = 0
tornado_timer = 300
sun_touch = False
rainbow_touch = False
rainbow_stay = False

# Keyboard event handlers
pressed_keys = set()

@window.event
def on_key_press(symbol, modifiers):
    global start_time, start
    global show_countdown, countdown_index
    pressed_keys.add(symbol)
    if show_countdown:
        show_countdown = False
        countdown_index = 0
    elif not game_over and start == True:
        start_time = time.time()
        start = False
  
@window.event
def on_key_release(symbol, modifiers):
    pressed_keys.discard(symbol)


@window.event
def on_draw():
    window.clear()
    label.draw()
    if show_countdown:
        countdown_labels[countdown_index].draw()
    elif not game_over:
        if tornado_touch_times >= 2:
            tornado_sprite.draw()
        sun_sprite.draw()
        cloud_sprite.draw()
        thunder_sprite.draw()
        rainbow_sprite.draw()
        pyglet.shapes.Rectangle(ocean_x, ocean_y, ocean_width, ocean_height, color=ocean_color).draw()
    else:
        game_over_sprite.draw()



def update(dt):
    global game_over, countdown_index, show_countdown, ocean_height, countdown_time, sun_timer, sun_touch, sun_touch_times, \
          rainbow_touch, rainbow_stay, tornado_touch_times, tornado_timer, tornado_direction_x, tornado_direction_y
    if start_time is not None:
                elapsed_time = int(time.time() - start_time)  # Calculate the elapsed time
                label.text = 'Time:' + str(elapsed_time)  # Update the label text
    if not game_over:
        if show_countdown:
            countdown_time -= dt
            if countdown_time <= 0:
                countdown_index += 1
                countdown_time = 1  # Time between countdown numbers
                if countdown_index >= len(countdown_labels):
                    show_countdown = False
        else:
            for key in pressed_keys:
                if key == pyglet.window.key.UP:
                    cloud_sprite.y += cloud_distance
                elif key == pyglet.window.key.DOWN:
                    cloud_sprite.y -= cloud_distance
                elif key == pyglet.window.key.LEFT:
                    cloud_sprite.x -= cloud_distance
                elif key == pyglet.window.key.RIGHT:
                    cloud_sprite.x += cloud_distance

            thunder_sprite.y -= thunder_speed * dt
            if thunder_sprite.y < -thunder_sprite.height:
                thunder_sprite.x = random.randint(0, window.width - thunder_sprite.width)
                thunder_sprite.y = window.height

            if cloud_sprite.y < thunder_sprite.y + thunder_sprite.height and \
                    cloud_sprite.y + cloud_sprite.height > thunder_sprite.y and \
                    cloud_sprite.x < thunder_sprite.x + thunder_sprite.width and \
                    cloud_sprite.x + cloud_sprite.width > thunder_sprite.x:
                game_over = True
                pyglet.clock.unschedule(update)  # Stop the update function

            # when touching the sun, reset the height of ocean and timer
            if cloud_sprite.y < sun_sprite.y + sun_sprite.height and \
                cloud_sprite.y + cloud_sprite.height > sun_sprite.y and \
                cloud_sprite.x < sun_sprite.x + sun_sprite.width and \
                cloud_sprite.x + cloud_sprite.width > sun_sprite.x:
                ocean_height = 0
                sun_sprite.y = -200
                sun_timer = 0
                sun_touch_times += 1
                tornado_touch_times += 1
                sun_touch = True

            # set the location and sun by timer
            sun_timer += 1
            if sun_timer >= 200 and sun_touch:
                sun_sprite.x = random.randint(0, window.width - sun_sprite.width)
                sun_sprite.y = random.randint(int(ocean_height), window.height - sun_sprite.height)
                sun_timer = 0
                sun_touch = False
            elif sun_timer >= 200 and sun_touch == False:
                sun_sprite.y = -200
                if sun_timer >= 300:
                    sun_sprite.x = random.randint(0, window.width - sun_sprite.width)
                    sun_sprite.y = random.randint(int(ocean_height), window.height - sun_sprite.height)
                    sun_timer = 0
            
            # when touching the rainbow
            if cloud_sprite.y < rainbow_sprite.y + rainbow_sprite.height and \
                cloud_sprite.y + cloud_sprite.height > rainbow_sprite.y and \
                cloud_sprite.x < rainbow_sprite.x + rainbow_sprite.width and \
                cloud_sprite.x + cloud_sprite.width > rainbow_sprite.x:
                rainbow_touch = True

            # when touching the tornado
            if tornado_touch_times >= 2:
                if cloud_sprite.y < tornado_sprite.y + tornado_sprite.height and \
                    cloud_sprite.y + cloud_sprite.height > tornado_sprite.y and \
                    cloud_sprite.x < tornado_sprite.x + tornado_sprite.width and \
                    cloud_sprite.x + cloud_sprite.width > tornado_sprite.x :
                    game_over = True

            # Increase ocean height gradually
            ocean_height += ocean_growth_speed * dt * 1.04
            if cloud_sprite.y < ocean_height:
                game_over = True

            # movemoent of tornado   
            tornado_timer += 1
            if tornado_touch_times >= 2:
                if rainbow_touch == False and tornado_timer >= 300:
                    if 0 > tornado_sprite.x or tornado_sprite.x > 800 - tornado_sprite.width:
                        tornado_direction_x = - tornado_direction_x
                    elif  tornado_sprite.y < 0 or tornado_sprite.y + tornado_sprite.height > 600:
                        tornado_direction_y = - tornado_direction_y
                    tornado_sprite.x += tornado_direction_x * tornado_speed * dt * 1.03
                    tornado_sprite.y += tornado_direction_y * tornado_speed * dt * 1.03
                elif rainbow_touch:
                    tornado_timer = 0
            
            # when and where rainbow appear
            if tornado_touch_times >= 2 and sun_touch_times >= 3:
                if rainbow_touch == False and rainbow_stay == False:
                    rainbow_sprite.x = random.randint(0, window.width - rainbow_sprite.width)
                    rainbow_sprite.y = random.randint(0, 100)
                    rainbow_stay = True
                elif rainbow_touch:
                    rainbow_sprite.x = -200
                    rainbow_sprite.y = -200
                    sun_touch_times = 0
                    rainbow_touch = False
                    rainbow_stay = False

            # Game is over when touching the edge
            if 0 > cloud_sprite.x or cloud_sprite.x > 800 - cloud_sprite.width \
                or cloud_sprite.y < 0 or cloud_sprite.y + cloud_sprite.height > 600:
                game_over = True
                pyglet.clock.unschedule(update)  # Stop the update function

# Start the game loop
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()
