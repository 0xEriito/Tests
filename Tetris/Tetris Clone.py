import pygame
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128),
    (0, 255, 255)
]

# Tetrimino shapes with colors
SHAPES = [
    ([[1, 1, 1, 1]], COLORS[1]),
    ([[1, 1], [1, 1]], COLORS[2]),
    ([[0, 1, 1], [1, 1, 0]], COLORS[3]),
    ([[1, 1, 0], [0, 1, 1]], COLORS[4]),
    ([[1, 1, 1], [0, 1, 0]], COLORS[5]),
    ([[1, 1, 1], [1, 0, 0]], COLORS[6]),
    ([[1, 1, 1], [0, 0, 1]], COLORS[7])
]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.score = 0
        self.current_tetrimino = self.new_tetrimino()
        self.next_tetrimino = self.new_tetrimino()
        self.current_pos = [GRID_WIDTH // 2, 0]
        self.game_over = False
        self.font = pygame.font.SysFont('comicsansms', 35)

    def new_tetrimino(self):
        return random.choice(SHAPES)

    def rotate_tetrimino(self):
        shape = self.current_tetrimino[0]
        rotated = list(zip(*shape[::-1]))
        if self.valid_position(rotated, self.current_pos):
            self.current_tetrimino = (rotated, self.current_tetrimino[1])

    def valid_position(self, shape, offset):
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if x + off_x < 0 or x + off_x >= GRID_WIDTH or y + off_y >= GRID_HEIGHT:
                        return False
                    if y + off_y >= 0 and self.grid[y + off_y][x + off_x]:
                        return False
        return True

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        self.grid = new_grid
        self.score += lines_cleared ** 2

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(
                    self.screen,
                    COLORS[self.grid[y][x]],
                    (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                    0
                )
        for x in range(GRID_WIDTH):
            pygame.draw.line(self.screen, (128, 128, 128), (x * GRID_SIZE, 0), (x * GRID_SIZE, SCREEN_HEIGHT))
        for y in range(GRID_HEIGHT):
            pygame.draw.line(self.screen, (128, 128, 128), (0, y * GRID_SIZE), (SCREEN_WIDTH, y * GRID_SIZE))

    def draw_tetrimino(self, shape, offset):
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen,
                        self.current_tetrimino[1],
                        ((x + off_x) * GRID_SIZE, (y + off_y) * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                        0
                    )

    def run(self):
        last_fall_time = pygame.time.get_ticks()
        fall_interval = 500
        self.current_pos = [GRID_WIDTH // 2, 0]

        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.draw_grid()
            self.draw_tetrimino(self.current_tetrimino[0], self.current_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.valid_position(self.current_tetrimino[0], (self.current_pos[0] - 1, self.current_pos[1])):
                            self.current_pos[0] -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_position(self.current_tetrimino[0], (self.current_pos[0] + 1, self.current_pos[1])):
                            self.current_pos[0] += 1
                    elif event.key == pygame.K_DOWN:
                        if self.valid_position(self.current_tetrimino[0], (self.current_pos[0], self.current_pos[1] + 1)):
                            self.current_pos[1] += 1
                    elif event.key == pygame.K_UP:
                        self.rotate_tetrimino()

            current_time = pygame.time.get_ticks()
            if current_time - last_fall_time > fall_interval:
                if self.valid_position(self.current_tetrimino[0], (self.current_pos[0], self.current_pos[1] + 1)):
                    self.current_pos[1] += 1
                else:
                    for y, row in enumerate(self.current_tetrimino[0]):
                        for x, cell in enumerate(row):
                            if cell:
                                self.grid[self.current_pos[1] + y][self.current_pos[0] + x] = COLORS.index(self.current_tetrimino[1])
                    self.current_tetrimino = self.next_tetrimino
                    self.next_tetrimino = self.new_tetrimino()
                    self.current_pos = [GRID_WIDTH // 2, 0]
                    if not self.valid_position(self.current_tetrimino[0], self.current_pos):
                        self.game_over = True
                    self.clear_lines()
                last_fall_time = current_time

            score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()