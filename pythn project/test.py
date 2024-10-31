import pygame
import random

pygame.init()

#setup display
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

#define color
WHITE = (255, 255, 255)
BLUE = (0, 225, 0)
BLACK = (0, 0, 0)

#define constant
FPS = 30
GRAVITY = 1
JUMP = -15
PIPE_WIDTH = 70
PIPE_GAP = 300

#load bird image
bird_img = pygame.Surface((30, 30))
bird_img.fill((255, 255, 0))

#bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.vel = 0
        self.rect = pygame.Rect(self.x, self.y, 30, 30)

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.vel = JUMP
        
    def draw(self, win):
        win.blit(bird_img, (self.x, self.y))

#pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(30, HEIGHT - PIPE_GAP - 30)
        self.top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP)
    
    def update(self):
        self.x -= 5
        self.top.topleft = (self.x, 0)
        self.bottom.topleft = (self.x, self.height + PIPE_GAP)

    def draw(self, win):
        pygame.draw.rect(win, BLUE, self.top)
        pygame.draw.rect(win, BLUE, self.bottom)

#game over screen
def game_over(win, score):
    font_big = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)

    game_over_text = font_big.render("Game Over", True, BLACK)
    score_text = font_big.render(f"Score: {score}", True, BLACK)
    restart_text = font_small.render("Press any key to exit", True, BLACK)

    win.fill(WHITE)
    win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 3 + 50))
    win.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 100))
    pygame.display.update()
    wait_for_exit()

#wait for any key press to exit
def wait_for_exit():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False 

#main game loop
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    font = pygame.font.SysFont(None, 36)

    run = True
    while run:
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                bird.jump()
        
        #update bird
        bird.update()

       #update pipe
        if pipes[-1].x < WIDTH // 2:
            pipes.append(Pipe())

        for pipe in pipes[:]:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                score += 1
#check collisions
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top) or bird.rect.colliderect(pipe.bottom):
                game_over(win, score)
                run = False

        if bird.y > HEIGHT or bird.y < 0:
            game_over(win, score)
            run = False
             
#draw everything
        win.fill (BLACK)
        bird.draw(win)
        for pipe in pipes:
            pipe.draw(win)
        score_text = font.render(f"Score: {score}", True, BLACK)
        win.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()