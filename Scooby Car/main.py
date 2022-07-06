from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut
import karakter_1


m = 0 #karakter
a = 0 #Skor
b = 0 #marka
g = 0
h = 0
s = 1
t = 1

def init():
    glClearColor(255.0, 255.0, 255.0, 1.0) 
    gluOrtho2D(-50.0, 50.0, -30.0, 30.0) 
    
def text(x, y, color, text):
    glColor3fv(color)
    glWindowPos2f(x, y)
    for c in text:
        glutBitmapCharacter(glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

def skor():
    text(100, 100, (1, 0, 0), str(a) )
    text(100, 130, (1, 0, 0), "Score" )
    glutSwapBuffers()

def garis_putus(x, r):
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(35.0+x-r, -10.0)
    glVertex2f(35.0+x-r, -5.0)
    glVertex2f(50+x-r, -5.0)
    glVertex2f(50+x-r, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(20.0+x-r, 5.0)
    glVertex2f(20.0+x-r, 10.0)
    glVertex2f(35.0+x-r, 10.0)
    glVertex2f(35.0+x-r, 5.0)
    glEnd()

def jalan():
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    glVertex2f(50.0, 20.0 )
    glVertex2f(50.0, -20.0 )
    glVertex2f(-50.0, -20.0 )
    glVertex2f(-50.0, 20.0 )
    glEnd() 
    glFlush()

def batu1(u,v):
    glBegin(GL_POLYGON)
    glColor3ub(51, 51, 51)
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

def batu2(u,v):
    glBegin(GL_POLYGON)
    glColor3ub(100, 100, 100)
    glVertex2f(-35+u-v, -10)
    glVertex2f(-34+u-v, -8)
    glVertex2f(-33+u-v, -9)
    glVertex2f(-32+u-v, -6)
    glVertex2f(-32+u-v, -9)
    glVertex2f(-31+u-v, -8)
    glVertex2f(-30+u-v, -10)
    glVertex2f(-35+u-v, -10)
    glEnd()

def batu3(u,v):
    glBegin(GL_POLYGON)
    glColor3ub(51, 51, 51)
    glVertex2f(-35+u-v , 15)
    glVertex2f(-34+u-v, 17)
    glVertex2f(-33+u-v, 16)
    glVertex2f(-32+u-v, 19)
    glVertex2f(-31+u-v, 16)
    glVertex2f(-30+u-v, 17)
    glVertex2f(-29+u-v, 15)
    glVertex2f(-35+u-v, 15)
    glEnd()
    glFlush()

def batu4(u,v):
    glBegin(GL_POLYGON)
    glColor3ub(51, 51, 51)
    glVertex2f(-35+u-v, -20)
    glVertex2f(-34+u-v, -18)
    glVertex2f(-33+u-v, -19)
    glVertex2f(-32+u-v, -16)
    glVertex2f(-32+u-v, -19)
    glVertex2f(-31+u-v, -18)
    glVertex2f(-30+u-v, -20)
    glVertex2f(-35+u-v, -20)
    glEnd()

def batu5(u,v):
    glBegin(GL_POLYGON)
    glColor3ub(51, 51, 51)
    glVertex2f(-35+u-v , -2)
    glVertex2f(-34+u-v, 0)
    glVertex2f(-33+u-v, -1)
    glVertex2f(-32+u-v, 2)
    glVertex2f(-31+u-v, 0)
    glVertex2f(-30+u-v, 0)
    glVertex2f(-29+u-v, -2)
    glVertex2f(-35+u-v, -2)
    glEnd()
    glFlush()

def duar1(u,v):
    glPushMatrix()
    glTranslate(-8,3.5,0)
    glColor3ub(255, 51, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()  
    
    
    glPushMatrix()
    
    glTranslate(-4.5,3.25,0)
    glColor3ub(255, 102, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()   
    
    glPushMatrix()
    
    glTranslate(-6,3.5,0)
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 
    
    
    glPushMatrix()
    glTranslate(-6,4.5,0)
    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()

def duar2(u,v):
    glPushMatrix()
    glTranslate(-8,-11.5,0)
    glColor3ub(255, 51, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()  
    
    
    glPushMatrix()
    
    glTranslate(-4.5,-11.25,0)
    glColor3ub(255, 102, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()   
    
    glPushMatrix()
    
    glTranslate(-6,-11.5,0)
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 
    
    
    glPushMatrix()
    glTranslate(-6,-10.5,0)
    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()
    
def duar3(u,v):
    glPushMatrix()
    glTranslate(-8,14.5,0)
    glColor3ub(255, 51, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()  
    
    
    glPushMatrix()
    
    glTranslate(-4.5,14.25,0)
    glColor3ub(255, 102, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()   
    
    glPushMatrix()
    
    glTranslate(-6,14.5,0)
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 
    
    
    glPushMatrix()
    glTranslate(-6,14.5,0)
    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 
    
def duar4(u,v):
    glPushMatrix()
    glTranslate(-8,-20.5,0)
    glColor3ub(255, 51, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()  
    
    
    glPushMatrix()
    
    glTranslate(-4.5,-20.25,0)
    glColor3ub(255, 102, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()   
    
    glPushMatrix()
    
    glTranslate(-6,-20.5,0)
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 
    
    
    glPushMatrix()
    glTranslate(-6,-19.5,0)
    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 
    
def duar5(u,v):
    
    glPushMatrix()
    glTranslate(-8,-3.5,0)
    glColor3ub(255, 51, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()  
    
    
    glPushMatrix()
    
    glTranslate(-4.5,-3.25,0)
    glColor3ub(255, 102, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix()   
    
    glPushMatrix()
    
    glTranslate(-6,-3.5,0)
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 
    
    
    glPushMatrix()
    glTranslate(-6,-2.5,0)
    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(3.46361+u-v, 1.43656)
    glVertex2f(3.93035+u-v, 2.09164)
    glVertex2f(4.28245+u-v, 1.58395)
    glVertex2f(4.35615+u-v, 2.19809)
    glVertex2f(5.06854+u-v, 1.88693)
    glVertex2f(4.59361+u-v, 2.4683)
    glVertex2f(5.12586+u-v, 2.48468)
    glVertex2f(4.68368+u-v, 2.77946)
    glVertex2f(5.01122+u-v, 3.22164)
    glVertex2f(4.49535+u-v, 3.22164)
    glVertex2f(4.82289+u-v, 3.92584)
    glVertex2f(4.20875+u-v, 3.38541)
    glVertex2f(3.9631+u-v, 3.93403)
    glVertex2f(3.79933+u-v, 3.38541)
    glVertex2f(3.0+u-v, 4.0)
    glVertex2f(3.3981+u-v, 3.12338)
    glVertex2f(2.91498+u-v, 3.22164)
    glVertex2f(3.25071+u-v, 2.6812)
    glVertex2f(2.85766+u-v, 2.12439)
    glVertex2f(3.50455+u-v, 2.24722)
    glEnd()
    glFlush()
    glPopMatrix() 

def stop1(u,v):
    global s
    game_over()
    s *= 0 
    duar1(u,v+30)

def stop2(u,v):
    global s
    game_over()
    s *= 0 
    duar2(u,v+30)

def stop3(u,v):
    global s
    game_over()
    s *= 0 
    duar3(u,v+30)

def stop4(u,v):
    global s
    game_over()
    s *= 0 
    duar4(u,v+30)
    
def stop5(u,v): 
    global s
    game_over()
    s *= 0 
    duar5(u,v+30)    

def finish(u):
    glColor3ub(255,0,255)
    glBegin(GL_LINES)
    glVertex2f(-3120+u, -20)
    glVertex2f(-3120+u, 20)
    
    glVertex2f(-3122+u, -20)
    glVertex2f(-3122+u, 20)
    
    glVertex2f(-3124+u, -20)
    glVertex2f(-3124+u, 20)
    
    glVertex2f(-3126+u, -20)
    glVertex2f(-3126+u, 20)
    
    glVertex2f(-3128+u, -20)
    glVertex2f(-3128+u, 20)
    glEnd()

def menang():
    text(500, 300, (100, 200, 100), "YOU WIN" )
    glutSwapBuffers()

def game_over():
    text(100, 160, (100, 200, 0), "GAME OVER" )
    glutSwapBuffers()

def rintangan():
    global s,t
    
    for i in (1,3,5,6,8,9,11,12,14,15,18,19,21,23,25,26,28,30):
        batu5(g,100*i)
        for j in (1,3):
            if 100*j+50<a<100*j+70  and -6<m<6:
                stop5(g,100*i)
        for k in (5,6,8,9,11,12,14,15):
            if 50*(k-4)+425<a<50*(k-4)+435  and -6<m<6:
                stop5(g,100*i)
        for l in (18,19,21,23,25,26,28,30):
            if 25*(l-16)+1012.5<a<25*(l-16)+1017.5  and -6<m<6:
                stop5(g,100*i)

    for i in (1,2,4,6,7,8,10,11,13,14,16,17,18,20,22,24,26,29,30):
        batu4(g,100*i)
        for j in(1,2):
            if 100*j+50<a<100*j+70  and -16<m<-12:
                stop4(g,100*i)
        for k in (4,6,7,8,10,11,13,14):
            if 50*(k-4)+425<a<50*(k-4)+435  and -16<m<-12:
                stop4(g,100*i)
        for l in (16,17,18,20,22,24,26,29,30):
            if 25*(l-16)+1012.5<a<25*(l-16)+1017.5  and -16<m<-12:
                stop4(g,100*i)

    for i in (1,3,4,5,7,8,11,13,14,17,18,19,21,22,23,25,27,28,30):
        batu3(g,100*i)
        for j in (1,3):    
            if 100*j+50<a<100*j+70  and 11<m<=16:
                stop3(g,100*i)
        for k in (4,5,7,8,11,13,14):
            if 50*(k-4)+425<a<50*(k-4)+435  and 11<m<=16:
                stop3(g,100*i)
        for l in (17,18,19,21,22,23,25,27,28,30):
            if 25*(l-16)+1012.5<a<25*(l-16)+1017.5  and 11<m<=16:
                stop3(g,100*i)
   
    for i in (2,3,4,6,9,10,12,13,15,16,20,22,23,24,26,27,29):
        batu2(g,100*i)
        for j in(2,3):
            if 100*j+50<a<100*j+70  and -14<m<-2:
                stop2(g,100*i)
        for k in (4,6,9,10,12,13,15):
            if 50*(k-4)+425<a<50*(k-4)+435  and -14<m<-2:
                stop2(g,100*i)
        for l in (16,20,22,23,24,26,27,29):
            if 25*(l-16)+1012.5<a<25*(l-16)+1017.5  and -14<m<-2:
                stop2(g,100*i)
    
    for i in (2,3,5,7,9,10,12,15,17,19,20,21,24,25,27,28,29):
        batu1(g,100*i)
        for j in (2,3):
            if 100*j+50<a<100*j+70  and 1<m<13:
                stop1(g,100*i)
        for k in (5,7,9,10,12,15):
            if 50*(k-4)+425<a<50*(k-4)+435  and 1<m<13:
                stop1(g,100*i) 
        for l in (17,19,20,21,24,25,27,28,29):
            if 25*(l-16)+1012.5<a<25*(l-16)+1017.5  and 1<m<13:
                stop1(g,100*i)
                       
    if 1572< a < 1578 :
        s*=0
        menang()  

    if s == 0:
        t *= 0

def speed():
    text(100, 525, (1, 0, 0), "Speed: " )
    text(170, 525, (1, 0, 0), str(s) )
    glutSwapBuffers()

def speed_increase():
    text(100, 550, (1, 0, 1), "Speed Increase" )
    glutSwapBuffers()

def all():
    global m,a,b,g,s,t
    a += t
    b += s
    g += s

    glClear(GL_COLOR_BUFFER_BIT)
    
    if a == 400:
        s *= 2
        speed_increase()
    if a == 1000:
        s *= 2
        speed_increase() 
  
    jalan()
    #garis putus
    for i in range (120):
        garis_putus(b,i*30)
        
    finish(b) 
    skor()    
    karakter_1.karakter1(m)
    rintangan()
    speed()
  
def input_keyboard(key,x,y):
    global m,s
    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        if -16<= m < 16:
            if 1<= s <= 4:
                m += 1
                print('m =', m)
            elif s == 0:
                m += 0
            
        
        
    elif key == GLUT_KEY_DOWN:
        if -16< m <= 16:
            if 1<= s <= 4:
                m -= 1
                print('m =', m)
            elif s == 0:
                m += 0

def update(value):
    glutPostRedisplay()
    glutTimerFunc(80,update,0)
   
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Scooby Car")
    glutDisplayFunc(all)
    glutSpecialFunc(input_keyboard)
    init()
    glutTimerFunc(50, update, 0)
    
    glutMainLoop()
    
main()
