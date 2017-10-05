import pygame
from room import Room
from position import Position

class Camera:

	def __init__(self, x, y, height, width, mapSize):
		self.position = Position(x, y)
		self.height = height
		self.width = width
		self.mapSize = mapSize

	def update(self, character):
		centerX = self.width/2 + self.position.x
		centerY = self.height/2 + self.position.y
		if character.position.x < centerX:
			self.move(1, centerX - character.position.x)
		elif character.position.x > centerX:
			self.move(2, character.position.x - centerX)

		if character.position.y < centerY:
			self.move(3, centerY - character.position.y)
		elif character.position.y > centerY:
			self.move(0, character.position.y - centerY)

	def move(self, direction, distance):
		if direction == 0:
			if self.position.y + self.height + distance > self.mapSize.y:
				self.position.y = self.mapSize.y - self.height
			else:
				self.position.y += distance
		elif direction == 1:
			if self.position.x - distance < 0:
				self.position.x = 0
			else:
				self.position.x -= distance
		elif direction == 2:
			if self.position.x + distance + self.width > self.mapSize.x:
				self.position.x = self.mapSize.x - self.width
			else:
				self.position.x += distance
		else:
			if self.position.y - distance < 0:
				self.position.y = 0
			else:
				self.position.y -= distance

	def rect(self):
		return pygame.Rect((self.position.x, self.position.y), (self.width, self.height))
