import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_triangle():
    glColor3f(0.5, 0.0, 0.5)
    
    glBegin(GL_TRIANGLES)
    
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    
    glEnd()

def main():
    pygame.init()
    
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Purple Triangle with PyOpenGL")
    
    glOrtho(-1, 1, -1, 1, -1, 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_triangle()
        
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
