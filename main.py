import pygame

pygame.init()
screen_size = (400, 400)
screen_color = (160, 160, 160)
border_thickness = 1
square_size = 40
line_width = 6
markers = []
clicked = False
pos = []
player = 1
FPS = 120
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode(screen_size)


def draw_screen():
    screen.fill(screen_color)
    i = 0
    while i < 1000:
        pygame.draw.line(screen, (0, 0, 0), (i, 0),
                         (i, 1000), border_thickness)
        pygame.draw.line(screen, (0, 0, 0), (0, i),
                         (1000, i), border_thickness)
        i += square_size
    return screen


# def newBoard():
for x in range(10):
    row = [0] * 10
    markers.append(row)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, BLACK, (x_pos * 40 + 15, y_pos *
                                40 + 15), (x_pos * 40 + 25, y_pos * 40 + 25), line_width)
                pygame.draw.line(screen, BLACK, (x_pos * 40 + 15, y_pos *
                                40 + 25), (x_pos * 40 + 25, y_pos * 40 + 15), line_width)
            if y == -1:
                pygame.draw.circle(
                    screen, RED, (x_pos * 40 + 20, y_pos * 40 + 20), 10, line_width)
            y_pos += 1
        x_pos += 1

def main():
    run = True
    clicked = False
    player = 1
    clock = pygame.time.Clock()
    
    while run:
        screen = draw_screen()
        draw_markers()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 40][cell_y // 40] == 0:
                    markers[cell_x // 40][cell_y // 40] = player
                    player *= -1
        
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
