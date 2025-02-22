import pygame
import sys

# تنظیمات اولیه
pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)
BOARD = [[None] * 4 for _ in range(4)]
PLAYER = 'X'

# ساخت پنجره
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# رسم خطوط جدول
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * 100), (WIDTH, i * 100), 3)
        pygame.draw.line(screen, LINE_COLOR, (i * 100, 0), (i * 100, HEIGHT), 3)

def draw_symbol(row, col):
    global PLAYER
    x, y = col * 100 + 50, row * 100 + 50
    if PLAYER == 'X':
        pygame.draw.line(screen, X_COLOR, (x - 25, y - 25), (x + 25, y + 25), 3)
        pygame.draw.line(screen, X_COLOR, (x + 25, y - 25), (x - 25, y + 25), 3)
    else:
        pygame.draw.circle(screen, O_COLOR, (x, y), 30, 3)
    BOARD[row][col] = PLAYER
    PLAYER = 'O' if PLAYER == 'X' else 'X'

def check_winner():
    for row in BOARD:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if BOARD[0][col] == BOARD[1][col] == BOARD[2][col] and BOARD[0][col] is not None:
            return BOARD[0][col]
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] and BOARD[0][0] is not None:
        return BOARD[0][0]
    if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] and BOARD[0][2] is not None:
        return BOARD[0][2]
    return None

def show_winner(winner):
    font = pygame.font.Font(None, 40)
    text = font.render(f"Player {winner} Wins!", True, (0, 128, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BG_COLOR)
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

def reset_game():
    global BOARD, PLAYER
    BOARD = [[None] * 3 for _ in range(3)]
    PLAYER = 'X'
    screen.fill(BG_COLOR)
    draw_grid()

draw_grid()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // 100, x // 100
            if BOARD[row][col] is None:
                draw_symbol(row, col)
                winner = check_winner()
                if winner:
                    show_winner(winner)
                    reset_game()
    pygame.display.update()