#Created by Bradley Arnot
import pygame
from monster import Monster
from position import Position

class Goblin(Monster):
	
	def __init__(self, x, y, nodeList=[]):
		#Calls parent class to set up state of object
		Monster.__init__(self, x, y, nodeList)
		#Load sprite sheet
		self.spriteSheet = pygame.image.load("img/monsters.png")
		#How much damage is dealt to player
		self.damage = 20

	#draw proper sprite from sprite sheet
	def draw(self, screen, camera):
		screen.blit(self.spriteSheet, (self.position.x - camera.position.x, self.position.y - camera.position.y), (((self.animationStage * 32) + (self.direction * 96), 64), (32, 32)))

	def __str__(self):
		return "Goblin: " + str(self.position) + " next node " + str(self.nodeList[self.nextIndex])
