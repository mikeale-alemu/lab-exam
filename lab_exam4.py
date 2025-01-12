import pygame
import sys

def main():
    pygame.init()

    width, height = 500, 400
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Pygame Canvas Example")

    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (255, 0, 0), (50, 50), (50 + 200, 50), 3)

    triangle_points = [(200, 100), (250, 200), (150, 200)]
    pygame.draw.polygon(screen, (0, 255, 0), triangle_points)

    center_x, center_y = width // 2, height // 2
    pygame.draw.circle(screen, (255, 0, 255), (center_x, center_y), 5)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
