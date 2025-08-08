import pygame

# pygame setup
pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
WHITE = (255,255,255)

class Paddle:
    def __init__(self, x, y, w=10, h=100, s=5):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.s = s

    def move_up(self):
        if self.y >0:
            self.y = self.y - self.s

    def move_down(self):
        if self.y < HEIGHT - self.h:
            self.y = self.y + self.s

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.w, self.h))

class Ball:
    def __init__(self, position, speed, r=10):
        self.position = position
        self.speed = speed
        self.r = r

    def update_position(self):
        self.position = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])

    def bounce_paddle(self, paddle_position_left, paddle_position_right, paddle_height):
        if self.position[0] <= paddle_position_left[0]+self.r:
            if (self.position[1] > paddle_position_left[1]) and (self.position[1] < paddle_position_left[1] + paddle_height):
                self.speed = (-self.speed[0], self.speed[1])

        if self.position[0] >= paddle_position_right[0]-self.r:
            if (self.position[1] > paddle_position_right[1]) and (self.position[1] < paddle_position_right[1] + paddle_height):
                self.speed = (-self.speed[0], self.speed[1])

    def bounce(self):
        if self.position[1] <= 0 or self.position[1] >= HEIGHT:
            self.speed = (self.speed[0], -self.speed[1])

    def check_game_over(self):
        if self.position[0] <= 0 or self.position[0] >= WIDTH:
            print('GAMEOVER')
            return True
        else:
            return False

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, self.position, self.r)

left_paddle = Paddle(50, HEIGHT // 2 - 50)
right_paddle = Paddle(WIDTH - 60, HEIGHT // 2 - 50)
ball_position = (WIDTH//2, HEIGHT//2)
ball_speed = (-3,3)
ball = Ball(ball_position, ball_speed, r = 10)

while running:
    ## Events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down()
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down()
    # if keys[pygame.K_s] and paddle_y < HEIGHT - PADDLE_HEIGHT:
    #     paddle_y = paddle_y + paddle_speed
    ## Loop
    ball.bounce_paddle((left_paddle.x, left_paddle.y),(right_paddle.x, right_paddle.y), left_paddle.h)
    ball.update_position()
    ball.bounce()
    game_over = ball.check_game_over()
    running = not game_over

    ## Render
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # Draw paddle
    left_paddle.draw(screen)
    right_paddle.draw(screen)
    ball.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()