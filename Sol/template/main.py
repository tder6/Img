from manim import *
def add(self, elements): 
	for element in elements: 
		# print(element)
		if(type(element) == list): add(self, element)
		else: self.add(element)