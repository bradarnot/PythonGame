#Created by Bradley Arnot
import pygame
from monster import Monster
from position import Position

class Skeleton(Monster):
	
	def __init__(self, x, y, nodeList=[]):
		#Set up state of object from parent class constructor
		Monster.__init__(self, x, y, nodeList)
		#load sprite sheet
		self.spriteSheet = pygame.image.load("img/monsters.png")
		#How much damage is dealt to the player
		self.damage = 15

	#Draw proper sprite from sprite sheet based on animation information from parent class
	def draw(self, screen, camera):
		screen.blit(self.spriteSheet, (self.position.x - camera.position.x, self.position.y - camera.position.y), (((self.animationStage * 32) + (self.direction * 96), 32), (32, 32)))

	def __str__(self):
		return "Skeleton: " + str(self.position) + " next node " + str(self.nodeList[self.nextIndex])
