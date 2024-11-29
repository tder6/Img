path = "D:\\Desktop\\Project\\Img\\"
import sys; sys.path.append(path + "Sol\\template"); from seg import *

eps1, eps2 = 0.25, 0.35
delta = 3.5
scale = 1.5

class Sol(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		x11, y11 = 1 * scale - delta, 1 * scale; x12, y12 = -1 * scale - delta, -1 * scale; x2, y2 = 0.5 * scale - delta, -0.5 * scale; x3, y3 = -0.5 * scale - delta, 0.5 * scale
		list = [
			point(1, x11, y11), point(1, x12, y12), point(1, x2, y2), point(1, x3, y3),
			Line([x3, y3, 0], [x2, y2, 0], color = BLACK),
			Tex(r"$(x_1,y_1)$", color = BLACK).move_to([x11, y11 + eps1, 0]).scale(0.8).align_to([x11 + eps1, y11, 0], LEFT),
			Tex(r"$(x_2,y_2)$", color = BLACK).move_to([x12, y12 - eps1, 0]).scale(0.8).align_to([x12 - eps1, y12, 0], RIGHT),
			Tex(r"$(i,j)$", color = BLACK).move_to([x2, y2 - eps2, 0]).scale(0.8),
			Tex(r"$(k,k-(i-j))$", color = BLACK).move_to([x3, y3 + eps2, 0]).scale(0.8),
			Line([x3, y3 - 2 * (x2 - x3), 0], [x2 - 2 * (x2 - x3), y2, 0], color = BLACK),
			Line([x3 + 2 * (x2 - x3), y3, 0], [x2, y2 + 2 * (x2 - x3), 0], color = BLACK),
			point(0, x3, y3 - 2 * (x2 - x3)), point(0, x2 - 2 * (x2 - x3), y2),
			point(0, x3 + 2 * (x2 - x3), y3), point(0, x2, y2 + 2 * (x2 - x3)),
		]
		add(self, list)

		x11, y11 = -1 * scale + delta, 1 * scale; x12, y12 = 1 * scale + delta, -1 * scale; x2, y2 = -0.5 * scale + delta, -0.5 * scale; x3, y3 = 0.5 * scale + delta, 0.5 * scale
		list = [
			point(1, x11, y11), point(1, x12, y12), point(1, x2, y2), point(1, x3, y3),
			Line([x3, y3, 0], [x2, y2, 0], color = BLACK),
			Tex(r"$(x_1,y_1)$", color = BLACK).move_to([x11, y11 + eps1, 0]).scale(0.8).align_to([x11 - eps1, y11, 0], RIGHT),
			Tex(r"$(x_2,y_2)$", color = BLACK).move_to([x12, y12 - eps1, 0]).scale(0.8).align_to([x12 + eps1, y12, 0], LEFT),
			Tex(r"$(i,j)$", color = BLACK).move_to([x2, y2 - eps2, 0]).scale(0.8),
			Tex(r"$(k,(i+j)-k)$", color = BLACK).move_to([x3, y3 + eps2, 0]).scale(0.8),
			Line([x3, y3 - 2 * (x3 - x2), 0], [x2 + 2 * (x3 - x2), y2, 0], color = BLACK),
			Line([x3 - 2 * (x3 - x2), y3, 0], [x2, y2 + 2 * (x3 - x2), 0], color = BLACK),
			point(0, x3, y3 - 2 * (x3 - x2)), point(0, x2 + 2 * (x3 - x2), y2),
			point(0, x3 - 2 * (x3 - x2), y3), point(0, x2, y2 + 2 * (x3 - x2)),
		]
		add(self, list)

		list = [
			Line([0, delta, 0], [0, -delta, 0], color = BLACK),
		]
		add(self, list)