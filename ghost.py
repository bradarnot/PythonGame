#Created by Bradley Arnot
import pygame
from monster import Monster
from position import Position

class Ghost(Monster):
	
	def __init__(self, x, y, nodeList=[]):
		#Set up state of object with call to parent class
		Monster.__init__(self, x, y, nodeList)
		#Load sprite sheet
		self.spriteSheet = pygame.image.load("img/monsters.png")
		#How much damage is dealt to the player
		self.damage = 10

	#Draw the proper sprite from sprite sheet based on animation information
	def draw(self, screen, camera):
		screen.blit(self.spriteSheet, (self.position.x - camera.position.x, self.position.y - camera.position.y), (((self.animationStage * 32) + (self.direction * 96), 0), (32, 32)))


	def __str__(self):
		return "Ghost: " + str(self.position) + " next node " + str(self.nodeList[self.nextIndex])
