import pygame
from position import Position

class Button:

	def __init__(self, x, y, color, doors=[]):
		self.position = Position(x, y)
		self.size = 32
		self.hit = False
		self.surface = pygame.Surface((self.size, self.size))
		self.surface.fill(color)
		self.color = color
		self.doors = doors
		for door in doors:
			door.color = color
			door.image.fill(door.color)

	def checkButton(self, collider):
		if (not self.hit) and self.rect().colliderect(collider):
			self.hit = True
			for door in self.doors:
				door.toggleDoor()
		elif self.hit and not self.rect().colliderect(collider):
			self.hit = False

	def addDoor(self, door):
		self.doors.append(door)
		door.color = self.color
		door.image.fill(door.color)
			
	def draw(self, screen, camera):
		screen.blit(self.surface, (self.position.x - camera.position.x, self.position.y - camera.position.y))

	def rect(self):
		return pygame.Rect((self.position.x, self.position.y), (self.size, self.size))

	def __str__(self):
		return "Button: " + str(self.position) + " pressed: " + str(self.hit)
