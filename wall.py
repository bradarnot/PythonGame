#Created by Bradley Arnot
import pygame
from position import Position

class Wall:

	def __init__(self, x, y, width, height):
		self.position = Position(x, y)
		self.height = height
		self.width = width
		self.image = pygame.Surface((width, height))
		self.image.fill((200, 200, 200))

	def updateImage(self):
		self.image = pygame.Surface((self.width, self.height))
		self.image.fill((200, 200, 200))

	def draw(self, screen, camera):
		screen.blit(self.image, (self.position.x - camera.position.x, self.position.y - camera.position.y))

	def rect(self):
		return pygame.Rect(self.position.x, self.position.y, self.width, self.height)

	def collideWall(self, x, y):
		return (x >= self.position.x and x <= self.position.x + self.width) and (y >= self.position.y and y <= self.position.y + self.height)


	def __str__(self):
		return "Wall: (" + str(self.position.x) + ", " + str(self.position.y) + ") (" + str(self.width) + ", " + str(self.height) + ")"
