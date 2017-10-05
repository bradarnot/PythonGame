#Created by Bradley Arnot
import pygame
from orb import Orb
from position import Position

class OrbGenerator:
	
	def __init__(self):
		pass

	#Generate rectangle of orbs starting at position x, y
	#width and height are measured in number of orbs
	#spacing is the amount of space in pixels between each orb
	def generateRect(self, x, y, width, height, spacing=30):
		orbs = []
		for i in range(0, width * spacing, spacing):
			for j in range(0, height * spacing, spacing):
				orbs.append(Orb(i + x, j + y))
		return orbs
