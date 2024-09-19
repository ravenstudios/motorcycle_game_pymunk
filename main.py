from constants import *
import pymunk
import pymunk.pygame_util
import pygame

import motorcycle
import walls
import ramp

pygame.init()



surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


clock = pygame.time.Clock()


space = pymunk.Space()
space.gravity = (0, 1000)  # Example for Earth-like gravity, adjust as needed


motorcycle = motorcycle.Motorcycle(space)
wall = walls.Wall((0, GAME_HEIGHT - BLOCK_SIZE, GAME_WIDTH, GAME_HEIGHT - BLOCK_SIZE), space)
ramp = ramp.Ramp(GAME_WIDTH // 2, GAME_HEIGHT - BLOCK_SIZE, space)



static_body = space.static_body

options = pymunk.pygame_util.DrawOptions(surface)





def main():
    running = True
    global drone_balance
    while running:

        clock.tick(TICK_RATE)
        space.step(1 / TICK_RATE)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    motorcycle.reset()
                if event.key == pygame.K_q:
                    running = False


            # if event.type == pygame.VIDEORESIZE:
            #     screen_width, screen_height = event.w, event.h
            #     screen_height = (screen_width / 16) * 9
            #     surface = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            #
            #     for obj in objects:
            #         obj.screen_resize(surface, space)
            #     althold_pid_ui.slider_values[0] = [0, screen_width, 1, screen_height // 2]
            #     althold_pid_ui.update(events)
            #     balance_pid_ui.update(events)



        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     drone_balance.body.apply_impulse_at_local_point((10, 0), (0, -255))


        draw()
        update(events)
        pygame.display.update()

    pygame.quit()




def draw():
    surface.fill((75, 75, 75))#background

    space.debug_draw(options)

    camera_offset = motorcycle.body.position.x - GAME_WIDTH / 2

    motorcycle.draw(surface, camera_offset)
    ramp.draw(surface, camera_offset)
    wall.draw(surface)
    pygame.display.update()



def update(events):


    motorcycle.update()



if __name__ == "__main__":
    main()
