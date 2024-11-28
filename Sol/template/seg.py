from main import *
def seg(pos, color = BLACK, len = 0.25): return Line([pos, 0, 0], [pos, len, 0], color = color)
def line(left, right, color = BLACK): return Line([left, 0, 0], [right, 0, 0], color = color)
def tex(pos, text, color = BLACK, len = -0.325, scale = 0.8): return Tex("$" + text + "$", color = color).move_to([pos, len, 0]).scale(scale)
def point(x, y, color = BLACK, radius = 0.07): return Dot([x, y, 0], radius, color = color)