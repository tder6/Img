path = "D:\\Desktop\\Project\\Img\\"
import sys; sys.path.append(path + "Sol\\template"); from seg import *

x1, y1 = -1, 1; x2, y2 = 0, -2; x3, y3 = 2, 0
eps = 0.25

class Sol(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		list = [
			point(x1, y1), point(x2, y2), point(x3, y3),
			Line([x1, y1, 0], [x2, y1, 0], color = BLACK),
			Line([x2, y2, 0], [x2, y1, 0], color = BLACK),
			Line([x3, y3, 0], [x2, y3, 0], color = BLACK),
			Tex(r"$a$", color = BLACK).move_to([(x1 + x2) / 2, y1 + eps, 0]).scale(0.8),
			Tex(r"$b$", color = BLACK).move_to([x2 - eps, (y1 + y3) / 2, 0]).scale(0.8),
			Tex(r"$c$", color = BLACK).move_to([x2 - eps, (y2 + y3) / 2, 0]).scale(0.8),
			Tex(r"$d$", color = BLACK).move_to([(x2 + x3) / 2, y3 - eps, 0]).scale(0.8),
		]
		add(self, list)