import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game dimensions
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH + 200  # Additional space for score and next piece
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
GAME_AREA_WIDTH = BLOCK_SIZE * GRID_WIDTH

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),    # I - Cyan
    (0, 0, 255),      # J - Blue
    (255, 165, 0),    # L - Orange
    (255, 255, 0),    # O - Yellow
    (0, 255, 0),      # S - Green
    (128, 0, 128),    # T - Purple
    (255, 0, 0)       # Z - Red
]

# Define tetromino shapes
SHAPES = [
    [
        ['.....',
         '.....',
         'IIII.',
         '.....',
         '.....'],
        ['..I..',
         '..I..',
         '..I..',
         '..I..',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.JJJ.',
         '...J.',
         '.....'],
        ['.....',
         '..J..',
         '..J..',
         '.JJ..',
         '.....'],
        ['.....',
         '.J...',
         '.JJJ.',
         '.....',
         '.....'],
        ['.....',
         '.JJ..',
         '.J...',
         '.J...',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.LLL.',
         '.L...',
         '.....'],
        ['.....',
         '.LL..',
         '..L..',
         '..L..',
         '.....'],
        ['.....',
         '...L.',
         '.LLL.',
         '.....',
         '.....'],
        ['.....',
         '.L...',
         '.L...',
         '.LL..',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.OO..',
         '.OO..',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '..SS.',
         '.SS..',
         '.....'],
        ['.....',
         '.S...',
         '.SS..',
         '..S..',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.TTT.',
         '..T..',
         '.....'],
        ['.....',
         '..T..',
         '.TT..',
         '..T..',
         '.....'],
        ['.....',
         '..T..',
         '.TTT.',
         '.....',
         '.....'],
        ['.....',
         '.T...',
         '.TT..',
         '.T...',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.ZZ..',
         '..ZZ.',
         '.....'],
        ['.....',
         '..Z..',
         '.ZZ..',
         '.Z...',
         '.....']
    ]
]

# Game variables
score = 0
level = 1
lines_cleared = 0
fall_speed = 0.5  # Initial fall speed in seconds
last_fall_time = 0

# Create a grid
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    
    return grid

# Create a random shape
def get_shape():
    shape_idx = random.randint(0, len(SHAPES) - 1)
    return SHAPES[shape_idx], COLORS[shape_idx], shape_idx

# Convert shape format to positions
def convert_shape_format(shape, shape_pos):
    positions = []
    format = shape
    
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column != '.' and column != ' ':
                positions.append((shape_pos[0] + j - 2, shape_pos[1] + i - 2))
    
    return positions

# Check if position is valid
def valid_space(shape, grid, shape_pos):
    accepted_pos = [[(x, y) for x in range(GRID_WIDTH) if grid[y][x] == BLACK] for y in range(GRID_HEIGHT)]
    accepted_pos = [item for sublist in accepted_pos for item in sublist]
    
    formatted = convert_shape_format(shape, shape_pos)
    
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] >= 0:  # Only check positions on the grid
                return False
    
    return True

# Check if game is lost
def check_lost(locked_positions):
    for pos in locked_positions:
        if pos[1] < 1:
            return True
    return False

# Draw the grid
def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Draw next shape in the side panel
def draw_next_shape(shape, color):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, WHITE)
    
    # Position for the next shape display
    sx = GAME_AREA_WIDTH + 50
    sy = 100
    
    format = shape[0]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column != '.' and column != ' ':
                pygame.draw.rect(screen, color, (sx + j*20, sy + i*20, 20, 20), 0)
    
    screen.blit(label, (sx, sy - 40))

# Draw the score and level information
def draw_score_level(score, level, lines_cleared):
    font = pygame.font.SysFont('comicsans', 30)
    
    score_label = font.render(f'Score: {score}', 1, WHITE)
    level_label = font.render(f'Level: {level}', 1, WHITE)
    lines_label = font.render(f'Lines: {lines_cleared}', 1, WHITE)
    
    sx = GAME_AREA_WIDTH + 20
    
    screen.blit(score_label, (sx, 250))
    screen.blit(level_label, (sx, 300))
    screen.blit(lines_label, (sx, 350))

# Check for completed lines
def clear_rows(grid, locked):
    inc = 0  # increment for score
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if BLACK not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    
    if inc > 0:
        # Sort locked positions and shift them down
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    
    return inc

# Main function
def main():
    global score, level, lines_cleared, fall_speed, last_fall_time
    
    # Game variables
    locked_positions = {}
    grid = create_grid(locked_positions)
    
    change_piece = False
    run = True
    
    # Current and next tetromino
    current_piece_data = get_shape()
    current_piece_shapes = current_piece_data[0]
    current_piece_color = current_piece_data[1]
    current_piece_idx = current_piece_data[2]
    current_piece_rotation = 0
    current_piece_pos = [GRID_WIDTH // 2, 0]
    
    next_piece_data = get_shape()
    next_piece_shapes = next_piece_data[0]
    next_piece_color = next_piece_data[1]
    next_piece_idx = next_piece_data[2]
    
    clock = pygame.time.Clock()
    fall_time = 0
    
    while run:
        # Fall speed increases with level
        fall_speed = 0.5 - (level - 1) * 0.05
        if fall_speed < 0.1:
            fall_speed = 0.1
        
        # Update grid
        grid = create_grid(locked_positions)
        
        # Increase fall time and move piece down if enough time has passed
        fall_time += clock.get_rawtime()
        last_fall_time = pygame.time.get_ticks()
        
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece_pos[1] += 1
            if not valid_space(current_piece_shapes[current_piece_rotation], grid, current_piece_pos):
                current_piece_pos[1] -= 1
                change_piece = True
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            # Key press handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece_pos[0] -= 1
                    if not valid_space(current_piece_shapes[current_piece_rotation], grid, current_piece_pos):
                        current_piece_pos[0] += 1
                
                elif event.key == pygame.K_RIGHT:
                    current_piece_pos[0] += 1
                    if not valid_space(current_piece_shapes[current_piece_rotation], grid, current_piece_pos):
                        current_piece_pos[0] -= 1
                
                elif event.key == pygame.K_DOWN:
                    current_piece_pos[1] += 1
                    if not valid_space(current_piece_shapes[current_piece_rotation], grid, current_piece_pos):
                        current_piece_pos[1] -= 1
                
                elif event.key == pygame.K_UP:
                    # Rotate the piece
                    current_piece_rotation = (current_piece_rotation + 1) % len(current_piece_shapes)
                    if not valid_space(current_piece_shapes[current_piece_rotation], grid, current_piece_pos):
                        current_piece_rotation = (current_piece_rotation - 1) % len(current_piece_shapes)
        
        # Get the positions of the tetromino
        piece_pos = convert_shape_format(current_piece_shapes[current_piece_rotation], current_piece_pos)
        
        # Draw the tetromino on the grid
        for i in range(len(piece_pos)):
            x, y = piece_pos[i]
            if y >= 0:  # Only draw if the piece is on the visible grid
                grid[y][x] = current_piece_color
        
        # If the piece has landed
        if change_piece:
            for pos in piece_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece_color
            
            # Get the next piece
            current_piece_data = next_piece_data
            current_piece_shapes = current_piece_data[0]
            current_piece_color = current_piece_data[1]
            current_piece_idx = current_piece_data[2]
            current_piece_rotation = 0
            current_piece_pos = [GRID_WIDTH // 2, 0]
            
            next_piece_data = get_shape()
            next_piece_shapes = next_piece_data[0]
            next_piece_color = next_piece_data[1]
            next_piece_idx = next_piece_data[2]
            
            # Check for cleared rows and update score
            rows_cleared = clear_rows(grid, locked_positions)
            if rows_cleared > 0:
                # Score calculation based on Tetris scoring system
                if rows_cleared == 1:
                    score += 100 * level
                elif rows_cleared == 2:
                    score += 300 * level
                elif rows_cleared == 3:
                    score += 500 * level
                elif rows_cleared == 4:
                    score += 800 * level
                
                lines_cleared += rows_cleared
                
                # Level up every 10 lines
                level = (lines_cleared // 10) + 1
            
            change_piece = False
        
        # Draw everything
        screen.fill(BLACK)
        
        # Draw the grid
        draw_grid(grid)
        
        # Draw the border for the game area
        pygame.draw.rect(screen, WHITE, (0, 0, GAME_AREA_WIDTH, SCREEN_HEIGHT), 4)
        
        # Draw the next piece preview
        draw_next_shape(next_piece_shapes, next_piece_color)
        
        # Draw score and level
        draw_score_level(score, level, lines_cleared)
        
        # Check if game is lost
        if check_lost(locked_positions):
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render("GAME OVER", 1, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, SCREEN_HEIGHT/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
        
        # Update the display
        pygame.display.update()
        
        # Cap the frame rate
        clock.tick(60)

# Main game execution
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()