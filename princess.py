#Created by Bradley Arnot
import pygame
from character import Character
from position import Position
from camera import Camera

class Princess:

	def __init__(self, x, y):
		#Store position
		self.position = Position(x, y)
		#Load sprite sheet for princess
		self.sprite = pygame.image.load("img/people.png")

	#draw the princess sprite from the sprite sheet
	def draw(self, screen, camera):
		screen.blit(self.sprite, (self.position.x - camera.position.x, self.position.y - camera.position.y), ((128, 128), (32, 32)))

	#Returns true if the character has found(collided with) the princess
	def checkWin(self, character):
		return character.collider.colliderect(pygame.Rect((self.position.x, self.position.y), (32, 32)))
