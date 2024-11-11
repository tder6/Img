from manim import *
len = 4
xa = 1.5
xb = 3
class Sol(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		line = Line([-len, 0, 0], [len, 0, 0], color = BLACK)
		seg1 = Line([-len, 0, 0], [-len, 0.25, 0], color = BLACK)
		seg2 = Line([len, 0, 0], [len, 0.25, 0], color = BLACK)
		seg3 = Line([0, 0, 0], [0, 0.25, 0], color = BLACK)
		l = Tex(r"$l$", color = BLACK).move_to([-len, -0.5, 0])
		r = Tex(r"$r$", color = BLACK).move_to([len, -0.5, 0])
		mid = Tex(r"$\text{mid}$", color = BLACK).move_to([0, -0.5, 0])
		sega = Line([xa, 0, 0], [xa, 0.25, 0], color = RED)
		segb = Line([xb, 0, 0], [xb, 0.25, 0], color = RED)
		a = Tex(r"$a$", color = RED).move_to([xa, -0.5, 0])
		b = Tex(r"$b$", color = RED).move_to([xb, -0.5, 0])
		lines = Line([xa, 0, 0], [xb, 0, 0], color = RED)
		self.add(line, seg1, seg2, seg3, l, r, mid, sega, segb, a, b, lines)