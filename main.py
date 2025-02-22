import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game!")

FPS = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:
    COLOUR = WHITE

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, self.COLOUR, (self.x, self.y, self.width, self.height))

def draw(window, paddles):
    window.fill(BLACK)

    for paddle in paddles:
        paddle.draw(WINDOW)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WINDOW, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


main()