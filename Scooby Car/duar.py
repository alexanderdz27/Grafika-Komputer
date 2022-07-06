from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut

def init():
    glClearColor(255.0, 255.0, 255.0, 1.0)
    gluOrtho2D(-50.0, 50.0, -30.0, 30.0)
    

def duar():
    glBegin(GL_POLYGON)
    glVertex2f(3.46361, 1.43656)
    glVertex2f(3.93035, 2.09164)
    glVertex2f(4.28245, 1.58395)
    glVertex2f(4.35615, 2.19809)
    glVertex2f(5.06854, 1.88693)
    glVertex2f(4.59361, 2.4683)
    glVertex2f(5.12586, 2.48468)
    glVertex2f(4.68368, 2.77946)
    glVertex2f(5.01122, 3.22164)
    glVertex2f(4.49535, 3.22164)
    glVertex2f(4.82289, 3.92584)
    glVertex2f(4.20875, 3.38541)
    glVertex2f(3.9631, 3.93403)
    glVertex2f(3.79933, 3.38541)
    glVertex2f(3.0, 4.0)
    glVertex2f(3.3981, 3.12338)
    glVertex2f(2.91498, 3.22164)
    glVertex2f(3.25071, 2.6812)
    glVertex2f(2.85766, 2.12439)
    glVertex2f(3.50455, 2.24722)
    glEnd()
    

def boom():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glPushMatrix()
    glScalef(2.0, 2.0, 0.0)
    glTranslate(-2,-1,0)
    glColor3ub(255, 51, 0)
    duar()
    glFlush()
    glPopMatrix()  
    
    glPushMatrix()
    glScalef(1.5, 1.5, 0.0)
    glTranslate(-1.5,-0.5,0)
    glColor3ub(255, 102, 0)
    duar()
    glFlush()
    glPopMatrix() 
    
    glPushMatrix()
    glColor3ub(255, 255, 0)
    duar()
    glFlush()
    glPopMatrix()
    

def update(value):
    
    glutPostRedisplay()
    glutTimerFunc(100,update,0)
   

def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Scooby Car")
    glutDisplayFunc(boom)
    init()
    glutTimerFunc(50, update, 0)
    glutMainLoop()

main()
