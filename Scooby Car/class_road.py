from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut

# def init():
#     glClearColor(255.0, 255.0, 255.0, 1.0)
#     gluOrtho2D(-50.0, 50.0, -30.0, 30.0)
    
class road:
    def __init__(self):
        pass

    def marka(self, p ,o):
        glBegin(GL_POLYGON)
        glColor3ub(255,255,255)
        glVertex2f(35.0 - p + o, -10.0)
        glVertex2f(35.0 - p + o, -5.0)
        glVertex2f(50 - p + o, -5.0)
        glVertex2f(50 - p + o, -10.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3ub(255,255,255)
        glVertex2f(20.0 - p, 5.0)
        glVertex2f(20.0 - p, 10.0)
        glVertex2f(35.0 - p, 10.0)
        glVertex2f(35.0 - p, 5.0)
        glEnd()
        glFlush()
    def jalan(self):
        glBegin(GL_POLYGON)
        glColor3ub(0,0,0)
        glVertex2f(50.0, 20.0 )
        glVertex2f(50.0, -20.0 )
        glVertex2f(-50.0, -20.0 )
        glVertex2f(-50.0, 20.0 )
        glEnd() 
        glFlush()
        
    def batu(self,v ,u ):
        glTranslate
        glBegin(GL_POLYGON)
        glColor3ub(170,169,173)
        glVertex2f(-35+u-v , 5)
        glVertex2f(-34+u-v, 7)
        glVertex2f(-33+u-v, 6)
        glVertex2f(-32+u-v, 9)
        glVertex2f(-31+u-v, 6)
        glVertex2f(-30+u-v, 7)
        glVertex2f(-29+u-v, 5)
        glVertex2f(-35+u-v, 5)
        glEnd()
        glFlush()


        
# def panggil():
#     road.marka(1)
    

# def update(value):
    
#     glutPostRedisplay()
#     glutTimerFunc(100,update,0)
   

# def main():
    
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
#     glutInitWindowSize(1000,600)
#     glutInitWindowPosition(100,100)
#     glutCreateWindow("Scooby Car")
#     glutDisplayFunc(panggil)
#     # glutSpecialFunc(input_keyboard)
#     glutTimerFunc(50, update, 0)
#     glutMainLoop()

# main()

