path = "D:\\Desktop\\Project\\Img\\"
import sys; sys.path.append(path + "Sol\\template"); from seg import *

i, i_bi = 3, 0; x, x_bx = 1.5, -3; y, y_by = 2.25, -1.5
begin, end = -5, 5
colori, colorx, colory = RED, BLUE, GREEN
class Sol(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		list = [
			line(begin, end), 
			seg(x, colorx), tex(x, r"x", colorx), seg(x_bx, colorx), tex(x_bx, r"x-b_x", colorx), line(x_bx, x, colorx),
			seg(y, colory), tex(y, r"y", colory), seg(y_by, colory), tex(y_by, r"y-b_y", colory), line(y_by, y, colory),
			seg(i, colori), tex(i, r"i", colori), seg(i_bi, colori), tex(i_bi, r"i-b_i", colori), line(i_bi, i, colori),
			tex((x + x_bx) / 2, r"\overbrace{~~~~~~~~~~~~~~~~~~~~~~~~~~~}", colorx, 0.5, 1), tex((x + x_bx) / 2, r"P(x)", colorx, 0.95),
			tex((y + y_by) / 2, r"\underbrace{~~~~~~~~~~~~~~~~~~~~~~}", colory, -0.7, 1), tex((y + y_by) / 2, r"P(y)", colory, -1.15),
		]
		add(self, list)