#Created by Bradley Arnot
import random
import pygame
from position import Position

class Orb:

	def __init__(self, x, y):
		self.position = Position(x, y)
		#Point value for each orb -- default one point
		self.value = 1
		self.size = 5
		self.surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA, 32)
		self.surface = self.surface.convert_alpha()

	def draw(self, screen, camera):
		#draws circle of random color every time it is called
		pygame.draw.circle(self.surface, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (self.size, self.size), self.size)
		screen.blit(self.surface, (self.position.x - camera.position.x, self.position.y - camera.position.y))

	#For collisions
	def rect(self):
		return pygame.Rect((self.position.x, self.position.y), (self.size * 2, self.size *2))
