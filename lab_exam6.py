import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    
    gluOrtho2D(0, display[0], display[1], 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)

        draw_line(100, 100, 700, 500)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
