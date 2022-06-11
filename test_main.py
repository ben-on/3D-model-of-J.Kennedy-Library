from OpenGL.GL import *
from OpenGL.GLU import *

import random
import pygame
import os

from pygame.locals import *
from test_pro import *
from test_pro1 import CubeMesh, ChairMesh

os.environ["SDL_VIDEO_CENTERED"]='1'


# def random_color():
#     x = 1/255
#     y = 1/255
#     z = 1/255
#     color = (x, y, z)
#     return color
#
# colors_list= []
#
# for n in range(len(chair_faces_vector4)):
#     colors_list.append(random_color())


def main():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)
    glRotatef(-45, 2, 0, 0)


main()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glRotatef(6, 6, -10, -45)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    ChairMesh()
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
quit()
