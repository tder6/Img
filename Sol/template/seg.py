from main import *
def seg(pos, color = BLACK, len = 0.25): return Line([pos, 0, 0], [pos, len, 0], color = color)
def line(left, right, color = BLACK): return Line([left, 0, 0], [right, 0, 0], color = color)
def tex(pos, text, color = BLACK, len = -0.325, scale = 0.8): return Tex("$" + text + "$", color = color).move_to([pos, len, 0]).scale(scale)
def point(type, x, y, color = BLACK, radius = 0.07): 
	if(type == 1): return Dot([x, y, 0], radius, color = color)
	else: return [point(1, x, y, WHITE, radius), Circle(radius, color).move_to([x, y, 0])]