from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Background

x = 1
a = 3
m = 0

def init():
    glClearColor(255.0, 255.0, 255.0, 1.0)
    gluOrtho2D(-50.0, 50.0, -30.0, 30.0)

def body():
    glColor3ub(53, 83, 10)
    glBegin(GL_POLYGON)
    glVertex2f(22, 3 + m)
    glVertex2f(22, -3 + m)
    glVertex2f(26, -5 + m)
    glVertex2f(36, -5 + m)
    glVertex2f(40, -3 + m)
    glVertex2f(40, 3 + m)
    glVertex2f(36, 5 + m)
    glVertex2f(26, 5 + m)
    glVertex2f(22, 3 + m)
    glEnd()

def body1():
    glColor3ub(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(26, 2 + m)
    glVertex2f(26, -2 + m)
    glVertex2f(28, -3 + m)
    glVertex2f(34, -3 + m)
    glVertex2f(36, -2 + m)
    glVertex2f(36, 2 + m)
    glVertex2f(34, 3 + m)
    glVertex2f(28, 3 + m)
    glVertex2f(26, 2 + m)
    glEnd()

def body2():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(30, 1 + m)
    glVertex2f(30, -1 + m)
    glVertex2f(34, -1 + m)
    glVertex2f(34, 1 + m)
    glVertex2f(30, 1 + m)
    glEnd()

def meriam():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(26, -1 + m)
    glVertex2f(26, 1 + m)
    glVertex2f(22, 1 + m)
    glVertex2f(22, -1 + m)
    glVertex2f(26, -1 + m)
    glEnd()

def roda1():
    glColor3ub(141,145,141)
    glBegin(GL_POLYGON)
    glVertex2f(22, -3 + m)
    glVertex2f(22, -5 + m)
    glVertex2f(26, -5 + m)
    glVertex2f(22, -3 + m)
    glEnd()

def roda2():
    glColor3ub(141,145,141)
    glBegin(GL_POLYGON)
    glVertex2f(36, -5 + m)
    glVertex2f(40, -5 + m)
    glVertex2f(40, -3 + m)
    glVertex2f(36, -5 + m)
    glEnd()

def roda3():
    glColor3ub(141,145,141)
    glBegin(GL_POLYGON)
    glVertex2f(40, 3 + m)
    glVertex2f(40, 5 + m)
    glVertex2f(36, 5 + m)
    glVertex2f(40, 3 + m)
    glEnd()

def roda4():
    glColor3ub(141,145,141)
    glBegin(GL_POLYGON)
    glVertex2f(22, 3 + m)
    glVertex2f(22, 5 + m)
    glVertex2f(26, 5 + m)
    glVertex2f(22, 3 + m)
    glEnd()

def outline():
    glColor3ub(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(22, -5 + m)
    glVertex2f(22, 5 + m)
    glVertex2f(40, 5 + m)
    glVertex2f(40, -5 + m)
    glEnd()

def karakter1():
    global m
    if m >= 18 :
        m -= 2
    elif m <= -18 :
        m += 2

    glPushMatrix()
    body()
    body1()
    body2()
    meriam()
    roda1()
    roda2()
    roda3()
    roda4()
    outline()
    glPopMatrix()
    glFlush()



def all():
    global m, x, a
    glClear(GL_COLOR_BUFFER_BIT)
    Background.background1()
    # glPushMatrix()
    karakter1()
    # glPopMatrix()

def input_keyboard(key,x,y):
    global m
    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        m += 1
        print('m =', m)

    elif key == GLUT_KEY_DOWN:
        m -= 1
        print(m)

def update(value):

    glutPostRedisplay()
    glutTimerFunc(100,update,0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Scooby Car")
    glutDisplayFunc(all)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    init()
    glutMainLoop()

main()