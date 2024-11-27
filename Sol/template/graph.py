from main import *
def tex(x, y, text, color, scale): return Tex("$" + text + "$", color = color).move_to([x, y, 0]).scale(scale)
def circle(x, y, color, radius): return Circle(radius, color).move_to([x, y, 0])
def node(x, y, text, color = BLACK, radius = 0.35, scale = 0.8): return [circle(x, y, color, radius), tex(x, y, text, color, scale)]
def edge(u, v, color = BLACK): return Line(u.get_bottom(), v.get_top(), color = color)
def graph(nodes, edges):
	points = {}; list = []
	for t, x, y, color in nodes: 
		t = str(t)
		circle, text = node(x, y, t, color)
		points[t] = circle
		list.append(circle), list.append(text)
	for u, v in edges: 
		u, v = str(u), str(v)
		list.append(edge(points[u], points[v]))
	list.reverse()
	return list