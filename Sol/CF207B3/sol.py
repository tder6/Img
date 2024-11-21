from manim import *
i = 3; y = 2.25; x = 1.5; i_bi = 0; y_by = -1.5; x_bx = -3
begin = -5; end = 5; height = 0.25
colori = RED; colorx = BLUE; colory = GREEN
def seg(pos, color = BLACK, len = height): return Line([pos, 0, 0], [pos, len, 0], color = color)
def line(left, right, color = BLACK): return Line([left, 0, 0], [right, 0, 0], color = color)
def tex(pos, text, color = BLACK, len = -0.325, scale = 0.8): return Tex("$" + text + "$", color = color).move_to([pos, len, 0]).scale(scale)
class Sol(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		add = [
			line(begin, end), 
			seg(x, colorx), tex(x, r"x", colorx), seg(x_bx, colorx), tex(x_bx, r"x-b_x", colorx), line(x_bx, x, colorx),
			seg(y, colory), tex(y, r"y", colory), seg(y_by, colory), tex(y_by, r"y-b_y", colory), line(y_by, y, colory),
			seg(i, colori), tex(i, r"i", colori), seg(i_bi, colori), tex(i_bi, r"i-b_i", colori), line(i_bi, i, colori),
			tex((x + x_bx) / 2, r"\overbrace{~~~~~~~~~~~~~~~~~~~~~~~~~~~}", colorx, 0.5, 1), tex((x + x_bx) / 2, r"P(x)", colorx, 0.95),
			tex((y + y_by) / 2, r"\underbrace{~~~~~~~~~~~~~~~~~~~~~~}", colory, -0.7, 1), tex((y + y_by) / 2, r"P(y)", colory, -1.15),
		]
		for element in add: self.add(element)