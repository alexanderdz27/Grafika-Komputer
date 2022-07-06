from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x = 1
a = 1
if x >= 300:
    a *= 1.2
    if x >= 1000:
        a *= 1.2
        if x>= 2000 :
            a *= 1.2

def init():
    glClearColor(255.0, 255.0, 255.0, 1.0)
    gluOrtho2D(-50.0, 50.0, -30.0, 30.0)

def background1():
    global x,a
    x += a
    kanvas()
    jalan()
    bekgrond()   
    glFlush()

def bekgrond():
    global x,a
    x += a
    garis_putus()
    if x >= 1000:
        glPushMatrix()
        glTranslate(-1000,0,0)
        garis_putus()
        glPopMatrix()
        if x >= 2030:
            glPushMatrix()
            glTranslate(-2030,0,0)
            garis_putus()
            glPopMatrix()
        
def kanvas():    
    print(x)
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(-1000.0 + x,-30.0)
    glColor3ub(0, 255, 0)
    glVertex2f(-1000.0 + x, 30.0)
    glColor3ub(0, 0, 255)
    glVertex2f(50.0 + x, 30.0)
    glColor3ub(255, 0, 255)
    glVertex2f(50.0 + x , -30.0)
    glEnd()

def jalan():
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    glVertex2f(50.0, 20.0 )
    glVertex2f(50.0, -20.0 )
    glVertex2f(-5000.0, -20.0 )
    glVertex2f(-5000.0, 20.0 )
    glEnd()

def garis_putus():
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(35.0+x, -10.0)
    glVertex2f(35.0+x, -5.0)
    glVertex2f(42.5+x, -5.0)
    glVertex2f(42.5+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(20.0+x, 5.0)
    glVertex2f(20.0+x, 10.0)
    glVertex2f(35.0+x, 10.0)
    glVertex2f(35.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(5.0+x, -10.0)
    glVertex2f(5.0+x, -5.0)
    glVertex2f(20.0+x, -5.0)
    glVertex2f(20.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-10.0+x, 5.0)
    glVertex2f(-10.0+x, 10.0)
    glVertex2f(5.0+x, 10.0)
    glVertex2f(5.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-25.0+x, -10.0)
    glVertex2f(-25.0+x, -5.0)
    glVertex2f(-10.0+x, -5.0)
    glVertex2f(-10.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-40.0+x, 5.0)
    glVertex2f(-40.0+x, 10.0)
    glVertex2f(-25.0+x, 10.0)
    glVertex2f(-25.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-55.0+x, -10.0)
    glVertex2f(-55.0+x, -5.0)
    glVertex2f(-40.0+x, -5.0)
    glVertex2f(-40.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-70.0+x, 5.0)
    glVertex2f(-70.0+x, 10.0)
    glVertex2f(-55.0+x, 10.0)
    glVertex2f(-55.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-85.0+x, -10.0)
    glVertex2f(-85.0+x, -5.0)
    glVertex2f(-70.0+x, -5.0)
    glVertex2f(-70.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-100.0+x, 5.0)
    glVertex2f(-100.0+x, 10.0)
    glVertex2f(-85.0+x, 10.0)
    glVertex2f(-85.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-115.0+x, -10.0)
    glVertex2f(-115.0+x, -5.0)
    glVertex2f(-100.0+x, -5.0)
    glVertex2f(-100.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-130.0+x, 5.0)
    glVertex2f(-130.0+x, 10.0)
    glVertex2f(-115.0+x, 10.0)
    glVertex2f(-115.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-145.0+x, -10.0)
    glVertex2f(-145.0+x, -5.0)
    glVertex2f(-130.0+x, -5.0)
    glVertex2f(-130.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-160.0+x, 5.0)
    glVertex2f(-160.0+x, 10.0)
    glVertex2f(-145.0+x, 10.0)
    glVertex2f(-145.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-175.0+x, -10.0)
    glVertex2f(-175.0+x, -5.0)
    glVertex2f(-160.0+x, -5.0)
    glVertex2f(-160.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-190.0+x, 5.0)
    glVertex2f(-190.0+x, 10.0)
    glVertex2f(-175.0+x, 10.0)
    glVertex2f(-175.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-205.0+x, -10.0)
    glVertex2f(-205.0+x, -5.0)
    glVertex2f(-190.0+x, -5.0)
    glVertex2f(-190.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-220.0+x, 5.0)
    glVertex2f(-220.0+x, 10.0)
    glVertex2f(-205.0+x, 10.0)
    glVertex2f(-205.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-235.0+x, -10.0)
    glVertex2f(-235.0+x, -5.0)
    glVertex2f(-220.0+x, -5.0)
    glVertex2f(-220.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-250.0+x, 5.0)
    glVertex2f(-250.0+x, 10.0)
    glVertex2f(-235.0+x, 10.0)
    glVertex2f(-235.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-265.0+x, -10.0)
    glVertex2f(-265.0+x, -5.0)
    glVertex2f(-250.0+x, -5.0)
    glVertex2f(-250.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-280.0+x, 5.0)
    glVertex2f(-280.0+x, 10.0)
    glVertex2f(-265.0+x, 10.0)
    glVertex2f(-265.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-295.0+x, -10.0)
    glVertex2f(-295.0+x, -5.0)
    glVertex2f(-280.0+x, -5.0)
    glVertex2f(-280.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-310.0+x, 5.0)
    glVertex2f(-310.0+x, 10.0)
    glVertex2f(-295.0+x, 10.0)
    glVertex2f(-295.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-325.0+x, -10.0)
    glVertex2f(-325.0+x, -5.0)
    glVertex2f(-310.0+x, -5.0)
    glVertex2f(-310.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-340.0+x, 5.0)
    glVertex2f(-340.0+x, 10.0)
    glVertex2f(-325.0+x, 10.0)
    glVertex2f(-325.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-355.0+x, -10.0)
    glVertex2f(-355.0+x, -5.0)
    glVertex2f(-340.0+x, -5.0)
    glVertex2f(-340.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-370.0+x, 5.0)
    glVertex2f(-370.0+x, 10.0)
    glVertex2f(-355.0+x, 10.0)
    glVertex2f(-355.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-385.0+x, -10.0)
    glVertex2f(-385.0+x, -5.0)
    glVertex2f(-370.0+x, -5.0)
    glVertex2f(-370.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-400.0+x, 5.0)
    glVertex2f(-400.0+x, 10.0)
    glVertex2f(-385.0+x, 10.0)
    glVertex2f(-385.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-415.0+x, -10.0)
    glVertex2f(-415.0+x, -5.0)
    glVertex2f(-400.0+x, -5.0)
    glVertex2f(-400.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-430.0+x, 5.0)
    glVertex2f(-430.0+x, 10.0)
    glVertex2f(-415.0+x, 10.0)
    glVertex2f(-415.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-445.0+x, -10.0)
    glVertex2f(-445.0+x, -5.0)
    glVertex2f(-430.0+x, -5.0)
    glVertex2f(-430.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-460.0+x, 5.0)
    glVertex2f(-460.0+x, 10.0)
    glVertex2f(-445.0+x, 10.0)
    glVertex2f(-445.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-475.0+x, -10.0)
    glVertex2f(-475.0+x, -5.0)
    glVertex2f(-460.0+x, -5.0)
    glVertex2f(-460.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-490.0+x, 5.0)
    glVertex2f(-490.0+x, 10.0)
    glVertex2f(-475.0+x, 10.0)
    glVertex2f(-475.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-505.0+x, -10.0)
    glVertex2f(-505.0+x, -5.0)
    glVertex2f(-490.0+x, -5.0)
    glVertex2f(-490.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-520.0+x, 5.0)
    glVertex2f(-520.0+x, 10.0)
    glVertex2f(-505.0+x, 10.0)
    glVertex2f(-505.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-535.0+x, -10.0)
    glVertex2f(-535.0+x, -5.0)
    glVertex2f(-520.0+x, -5.0)
    glVertex2f(-520.0+x, -10.0)
    glEnd()     

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-550.0+x, 5.0)
    glVertex2f(-550.0+x, 10.0)
    glVertex2f(-535.0+x, 10.0)
    glVertex2f(-535.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-565.0+x, -10.0)
    glVertex2f(-565.0+x, -5.0)
    glVertex2f(-550.0+x, -5.0)
    glVertex2f(-550.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-580.0+x, 5.0)
    glVertex2f(-580.0+x, 10.0)
    glVertex2f(-565.0+x, 10.0)
    glVertex2f(-565.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-595.0+x, -10.0)
    glVertex2f(-595.0+x, -5.0)
    glVertex2f(-580.0+x, -5.0)
    glVertex2f(-580.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-610.0+x, 5.0)
    glVertex2f(-610.0+x, 10.0)
    glVertex2f(-595.0+x, 10.0)
    glVertex2f(-595.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-625.0+x, -10.0)
    glVertex2f(-625.0+x, -5.0)
    glVertex2f(-610.0+x, -5.0)
    glVertex2f(-610.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-640.0+x, 5.0)
    glVertex2f(-640.0+x, 10.0)
    glVertex2f(-625.0+x, 10.0)
    glVertex2f(-625.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-655.0+x, -10.0)
    glVertex2f(-655.0+x, -5.0)
    glVertex2f(-640.0+x, -5.0)
    glVertex2f(-640.0+x, -10.0)
    glEnd()  

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-670.0+x, 5.0)
    glVertex2f(-670.0+x, 10.0)
    glVertex2f(-655.0+x, 10.0)
    glVertex2f(-655.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-685.0+x, -10.0)
    glVertex2f(-685.0+x, -5.0)
    glVertex2f(-670.0+x, -5.0)
    glVertex2f(-670.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-700.0+x, 5.0)
    glVertex2f(-700.0+x, 10.0)
    glVertex2f(-685.0+x, 10.0)
    glVertex2f(-685.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-715.0+x, -10.0)
    glVertex2f(-715.0+x, -5.0)
    glVertex2f(-700.0+x, -5.0)
    glVertex2f(-700.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-730.0+x, 5.0)
    glVertex2f(-730.0+x, 10.0)
    glVertex2f(-715.0+x, 10.0)
    glVertex2f(-715.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-745.0+x, -10.0)
    glVertex2f(-745.0+x, -5.0)
    glVertex2f(-730.0+x, -5.0)
    glVertex2f(-730.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-760.0+x, 5.0)
    glVertex2f(-760.0+x, 10.0)
    glVertex2f(-745.0+x, 10.0)
    glVertex2f(-745.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-775.0+x, -10.0)
    glVertex2f(-775.0+x, -5.0)
    glVertex2f(-760.0+x, -5.0)
    glVertex2f(-760.0+x, -10.0)
    glEnd()  

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-790.0+x, 5.0)
    glVertex2f(-790.0+x, 10.0)
    glVertex2f(-775.0+x, 10.0)
    glVertex2f(-775.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-805.0+x, -10.0)
    glVertex2f(-805.0+x, -5.0)
    glVertex2f(-790.0+x, -5.0)
    glVertex2f(-790.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-820.0+x, 5.0)
    glVertex2f(-820.0+x, 10.0)
    glVertex2f(-805.0+x, 10.0)
    glVertex2f(-805.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-835.0+x, -10.0)
    glVertex2f(-835.0+x, -5.0)
    glVertex2f(-820.0+x, -5.0)
    glVertex2f(-820.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-850.0+x, 5.0)
    glVertex2f(-850.0+x, 10.0)
    glVertex2f(-835.0+x, 10.0)
    glVertex2f(-835.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-865.0+x, -10.0)
    glVertex2f(-865.0+x, -5.0)
    glVertex2f(-850.0+x, -5.0)
    glVertex2f(-850.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-880.0+x, 5.0)
    glVertex2f(-880.0+x, 10.0)
    glVertex2f(-865.0+x, 10.0)
    glVertex2f(-865.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-895.0+x, -10.0)
    glVertex2f(-895.0+x, -5.0)
    glVertex2f(-880.0+x, -5.0)
    glVertex2f(-880.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-910.0+x, 5.0)
    glVertex2f(-910.0+x, 10.0)
    glVertex2f(-895.0+x, 10.0)
    glVertex2f(-895.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-925.0+x, -10.0)
    glVertex2f(-925.0+x, -5.0)
    glVertex2f(-910.0+x, -5.0)
    glVertex2f(-910.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-940.0+x, 5.0)
    glVertex2f(-940.0+x, 10.0)
    glVertex2f(-925.0+x, 10.0)
    glVertex2f(-925.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-955.0+x, -10.0)
    glVertex2f(-955.0+x, -5.0)
    glVertex2f(-940.0+x, -5.0)
    glVertex2f(-940.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-970.0+x, 5.0)
    glVertex2f(-970.0+x, 10.0)
    glVertex2f(-955.0+x, 10.0)
    glVertex2f(-955.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-985.0+x, -10.0)
    glVertex2f(-985.0+x, -5.0)
    glVertex2f(-970.0+x, -5.0)
    glVertex2f(-970.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-1000.0+x, 5.0)
    glVertex2f(-1000.0+x, 10.0)
    glVertex2f(-985.0+x, 10.0)
    glVertex2f(-985.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-1015.0+x, -10.0)
    glVertex2f(-1015.0+x, -5.0)
    glVertex2f(-1000.0+x, -5.0)
    glVertex2f(-1000.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-1030.0+x, 5.0)
    glVertex2f(-1030.0+x, 10.0)
    glVertex2f(-1015.0+x, 10.0)
    glVertex2f(-1015.0+x, 5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-1045.0+x, -5.0)
    glVertex2f(-1045.0+x, -10.0)
    glVertex2f(-1030.0+x, -10.0)
    glVertex2f(-1030.0+x, -5.0)
    glEnd()

    
    glFlush()


# def input_keyboard(key,x,y):
#     global m
#     # Untuk mengubah posisi kotak
#     if key == GLUT_KEY_UP:
#         m += 1
        
#     elif key == GLUT_KEY_DOWN:
#         m -= 1

def update(value):
    
    glutPostRedisplay()
    glutTimerFunc(100,update,0)
   
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("bekgron")
    glutDisplayFunc(background1)
    # glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    init()
    glutMainLoop()

main()