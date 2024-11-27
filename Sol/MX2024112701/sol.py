path = "D:\\Desktop\\Project\\Img\\"
import sys; sys.path.append(path + "Sol\\template"); from graph import *

class Sol(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		list = graph([
				[0, 0, 3, BLACK],
				[1, 0, 1.7, RED],
				[2, -1, 0.4, BLUE],
				[3, 1, 0.4, BLUE],
				[4, -2, -0.9, RED],
				[5, 0, -0.9, RED],
				[6, 2, -0.9, RED],
				[7, -1, -2.2, BLUE],
			], [
				[0, 1],
				[1, 2],
				[1, 3],
				[2, 4],
				[2, 5],
				[3, 6],
				[5, 7],
		])
		add(self, list)