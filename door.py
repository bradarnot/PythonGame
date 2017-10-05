#Created by Bradley Arnot
import pygame
from wall import Wall
from position import Position

class Door(Wall):

	def __init__(self, x, y, width, height, visible=True):
		Wall.__init__(self, x, y, width, height)
		self.color = (0, 0, 0)
		self.image.fill(self.color)
		self.visible = visible

	def rect(self):
		if not self.visible:
			return pygame.Rect((0, 0), (0, 0))
		else:
			return Wall.rect(self)

	def toggleDoor(self):
		self.visible = not self.visible
		if self.visible:
			self.image = pygame.Surface((self.width, self.height))
			self.image.fill(self.color)
		else:
			self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
			self.image = self.image.convert_alpha()
			if self.width > self.height:
				pygame.draw.rect(self.image, self.color, pygame.Rect((0, 0), (10, self.height)))
				pygame.draw.rect(self.image, self.color, pygame.Rect((self.width - 10, 0), (10, self.height)))
			else:
				pygame.draw.rect(self.image, self.color, pygame.Rect((0, 0), (self.width, 10)))
				pygame.draw.rect(self.image, self.color, pygame.Rect((0, self.height - 10), (self.width, 10)))


	def __str__(self):
		return "Door: " + str(self.position) + " visbile: " + str(self.visible)
