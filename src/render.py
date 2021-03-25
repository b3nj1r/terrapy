import data
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
print("successful import")

print(data.x,data.y,data.z)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #flush screen buffers

# window settings
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("terrapy")
glutDisplayFunc(display)
glutIdleFunc(display)
glutMainLoop()
