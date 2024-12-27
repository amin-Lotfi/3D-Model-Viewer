import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtCore import Qt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL_accelerate import *
import numpy

class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.obj_file = 'obj.obj'
        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0
        self.zoom = 0.09
        self.points = []
        self.points_array = None
        self.selected_point = None

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 1.0, 1.0, 0.0))

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glScalef(self.zoom, self.zoom, self.zoom)
        glRotatef(self.rotation_x, 1.0, 0.0, 0.0)
        glRotatef(self.rotation_y, 0.0, 1.0, 0.0)
        glRotatef(self.rotation_z, 0.0, 0.0, 1.0)
        self.draw_points()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def draw_points(self):
        glColor3f(1.0, 1.0, 1.0)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.points_array)
        glDrawArrays(GL_POINTS, 0, len(self.points))
        glDisableClientState(GL_VERTEX_ARRAY)

        if self.selected_point is not None:
            glPointSize(10.0)
            glColor3f(1.0, 0.0, 0.0)
            glBegin(GL_POINTS)
            glVertex3f(self.selected_point[0], self.selected_point[1], self.selected_point[2])
            glEnd()

        glPointSize(1.0)
        default_color = (1.0, 1.0, 1.0)
        glColor3f(*default_color)
        glDrawArrays(GL_POINTS, 0, len(self.points))
        glDisableClientState(GL_VERTEX_ARRAY)

    def load_obj_file(self, x, y, z):
        self.points = []
        with open(self.obj_file, 'r') as f:
            for line in f:
                if line.startswith('v '):
                    _, x_val, y_val, z_val = line.split()
                    self.points.append((float(x_val), float(y_val), float(z_val)))

        self.points_array = numpy.array(self.points, dtype=numpy.float32)
        self.selected_point = (x, y, z)

    def show_coordinate_dialog(self):
        dialog = QInputDialog()
        dialog.setWindowTitle("Coordinate Input")
        dialog.setLabelText("Enter coordinates:")
        dialog.setOptions(QInputDialog.UsePlainTextEditForTextInput)
        if dialog.exec_() == QInputDialog.Accepted:
            entered_text = dialog.textValue()
            coordinates = entered_text.split(",")
            if len(coordinates) == 3:
                x = float(coordinates[0].strip())
                y = float(coordinates[1].strip())
                z = float(coordinates[2].strip())
                self.load_obj_file(x, y, z)
                print(f"Coordinates: x={x}, y={y}, z={z}")

    def contextMenuEvent(self, event):
        self.show_coordinate_dialog()
        self.update()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            dx = event.x() - self.last_pos.x()
            dy = event.y() - self.last_pos.y()
            self.rotation_x += dy
            self.rotation_y += dx
            self.update()
            self.last_pos = event.pos()

    def wheelEvent(self, event):
        self.zoom += event.angleDelta().y() / 1200
        if self.zoom < 0.01:
            self.zoom = 0.01
        self.update()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("3D Model Viewer")
        self.resize(800, 600)
        self.gl_widget = GLWidget(self)
        self.setCentralWidget(self.gl_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
