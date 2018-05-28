import pygame
from rpigl import glesutils, transforms
from rpigl.gles2 import *

# save each vertex
vertices = [(0.0, 0.0, 0.0), (0.5, 0.0, 0.0), (0.5, 0.5, 0.0), (0.0, 0.5, 0.0),
            (0.0, 0.0, -0.5), (0.5, 0.0, -0.5), (0.5, 0.5, -0.5), (0.0, 0.5, -0.5)]

outer_vertices = [(-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5),
                  (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5)]

# subscript of vertices, representing a surface of cube
indices_face_1 = (0, 1, 2, 0, 3)

indices_face_2 = (4, 5, 6, 4, 7)

indices_face_3 = (1, 5, 6, 1, 2)

indices_face_4 = (0, 4, 7, 0, 3)

indices_outer = (0, 1, 2, 3, 0, 4, 5, 1, 5, 6, 2, 6, 7, 3, 7, 4)

indices_points = (0, 1, 2, 3)

# arg: vertex_attrib, 3d floating vector
array_spec = glesutils.ArraySpec("vertex_attrib:3f")

# Graphics Library Shader Language(GLSL) for GPU Programming
vertex_glsl = array_spec.glsl() + """
uniform mat4 transform_matrix;
void main(void) {
  gl_Position = transform_matrix * vec4(vertex_attrib, 1.0);
  gl_PointSize = 2.0;
}
"""

fragment_glsl = """
uniform vec4 color;
void main(void) {
  gl_FragColor = color;
}
"""


class MyWindow(glesutils.GameWindow):
    def init(self):
        self.angle = 10
        self.framerate = 20
        # embedded program: vertex_glsl stands for vertex shader, fragment_glsl stands for fragment shader.
        self.vertex_shader = glesutils.VertexShader(vertex_glsl)
        self.fragment_shader = glesutils.FragmentShader(fragment_glsl)

        # bind painter object with executable OpenGL program which can exist more than one instance
        self.program1 = glesutils.Program(self.vertex_shader, self.fragment_shader)
        # use() method to switch between OpenGL program
        self.program1.use()

        # set OpenGL
        glClearDepthf(1.0)  # clean cache and set to 1.0
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

        glClearColor(0.5, 0.5, 0.5, 1)  # clean color cache and set color to medium gray scale(rbg,alpha)

        self.program1.uniform.light_dir.value = ((0, 1, -1))

        # load data to GPU
        self.verteces_buffer = array_spec.create_buffer(vertex_attrib=vertices)

        self.elements_face_1 = glesutils.ElementBuffer(indices_face_1)
        self.elements_face_2 = glesutils.ElementBuffer(indices_face_2)
        self.elements_face_3 = glesutils.ElementBuffer(indices_face_3)
        self.elements_face_4 = glesutils.ElementBuffer(indices_face_4)

        self.elements_outer = glesutils.ElementBuffer(indices_outer)
        self.elements_points = glesutils.ElementBuffer(indices_points)

        # transforms.compose combine several matrix as one
        # transforms.rotation_degrees returns a rotated matrix
        # transforms.scaling returns a zoomed matrix
        # transforms.stretching returns a stretching matrix
        self.outer_matrix = transforms.compose(transforms.rotation_degrees(20, "z"),
                                               transforms.rotation_degrees(20, "y"),
                                               transforms.rotation_degrees(20, "x"),
                                               transforms.scaling(1.2))

        self.points_matrix = transforms.compose(transforms.stretching(0.1, 1, 1.5),
                                                transforms.translation(-0.5, -0.5, -0.5))

    def on_frame(self, time):
        self.angle = self.angle + time * 0.02
        self.redraw()

    def draw(self):
        # Draw outer lines
        self.program1.uniform.transform_matrix.value = self.outer_matrix
        self.program1.uniform.color.value = (1, 1, 1, 1)
        self.verteces_buffer.draw(elements=self.elements_outer, mode=GL_LINE_STRIP)
        # Draw points
        self.program1.uniform.transform_matrix.value = self.points_matrix
        self.program1.uniform.color.value = (0, 0, 0, 1)
        self.verteces_buffer.draw(elements=self.elements_points, mode=GL_POINTS)

        # Draw spinning cube
        rotation_matrix = transforms.compose(transforms.rotation_degrees(self.angle, "z"),
                                             transforms.rotation_degrees(self.angle, "y"),
                                             transforms.compose(transforms.rotation_degrees(self.angle, "x")))

        self.program1.uniform.transform_matrix.value = rotation_matrix
        self.program1.uniform.color.value = (1, 0, 0, 1)
        self.verteces_buffer.draw(elements=self.elements_face_1, mode=GL_TRIANGLE_STRIP)
        self.program1.uniform.color.value = (0, 1, 0, 1)
        self.verteces_buffer.draw(elements=self.elements_face_2, mode=GL_TRIANGLE_STRIP)
        self.program1.uniform.color.value = (0, 0, 1, 1)
        self.verteces_buffer.draw(elements=self.elements_face_3, mode=GL_TRIANGLE_STRIP)
        self.program1.uniform.color.value = (0, 1, 1, 1)
        self.verteces_buffer.draw(elements=self.elements_face_4, mode=GL_TRIANGLE_STRIP)


MyWindow(200, 200, pygame.RESIZABLE).run()
