import pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game!")

# Frames per second
FPS = 105

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle and ball dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

# Font and winning score
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 5

class Paddle:
    COLOUR = WHITE  # Paddle color
    VEL = 3  # Paddle velocity

    def __init__(self, x, y, width, height):
        # Initialize paddle properties
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, window):
        # Draw paddle on the screen
        pygame.draw.rect(window, self.COLOUR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        # Move paddle up or down
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        # Reset paddle to its original position
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    MAX_VEL = 4  # Maximum ball velocity
    COLOUR = WHITE  # Ball color

    def __init__(self, x, y, radius):
        # Initialize ball properties
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, window):
        # Draw ball on the screen
        pygame.draw.circle(window, self.COLOUR, (self.x, self.y), self.radius)

    def move(self):
        # Move ball in the direction of velocity
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        # Reset ball position and reverse x direction
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

# Function to draw the game window
def draw(window, paddles, ball, left_score, right_score):
    window.fill(BLACK)  # Fill background with black

    # Display scores
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    window.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    window.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    # Draw paddles
    for paddle in paddles:
        paddle.draw(WINDOW)

    # Draw center line
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    # Draw the ball
    ball.draw(window)
    pygame.display.update()

# Function to handle ball collisions with paddles and walls
def handle_collision(ball, left_paddle, right_paddle):
    # Ball collision with top and bottom walls
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    # Ball collision with paddles
    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
                
                # Adjust ball's velocity based on impact position
                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                # Adjust ball's velocity based on impact position
                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

# Function to handle paddle movement based on key presses
def handle_paddle_movement(keys, left_paddle, right_paddle):
    # Move left paddle
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    # Move right paddle
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()

    # Initialize paddles and ball
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)  # Control game speed
        draw(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        # Check if ball goes past a paddle (score update)
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        # Check for winning condition
        if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:
            pygame.time.delay(5000)  # Delay before restarting game
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()

main()
