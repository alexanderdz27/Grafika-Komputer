from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut
def text(x, y, color, text):
    glColor3fv(color)
    glWindowPos2f(x, y)
    for c in text:
        glutBitmapCharacter(glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

def skor1():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    text(100, 100, (1, 0, 0), "Hello World!")
    # glutSwapBuffers()


# def update(value):
    
#     glutPostRedisplay()
#     glutTimerFunc(100,update,0)
   

# def main():
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
#     glutInitWindowSize(1000,600)
#     glutInitWindowPosition(100,100)
#     glutCreateWindow("Scooby Car")
#     glutDisplayFunc(skor1)
#     # glutSpecialFunc(input_keyboard)
#     glutTimerFunc(50, update, 0)
#     glutMainLoop()

# main()

