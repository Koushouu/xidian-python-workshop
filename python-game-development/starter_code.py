import pygame

# pygame setup
pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_x = 50
paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 5

while running:
    ## Events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ## Loop


    ## Render
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()