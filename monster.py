#Created by Bradley Arnot
import pygame
from position import Position

class Monster:
	
	def __init__(self, x, y, nodeList=[]):
		self.position = Position(x, y)
		self.animationStage = 0
		#Direction monster is walking
		#0=down, 1=left, 2=up, 3=right
		self.direction = 0	
		#list of position will monster will travel in order
		#Move index 0 then index 1 then ...
		#Current position is first node
		self.nodeList = [Position(x, y)] + nodeList
		#Holds index of next node in list
		self.nextIndex = 0
		#how many pixels the monster moves at a time
		self.speed = 1
		#Speed animation runs
		#0.1 = 1 animation frame every 10 seconds
		self.animationSpeed = 0.1
		#Position in animation frame
		self.animationCount = 0

	def iterateAnimation(self):
		#if the animation timer has reached 1, iterate to next animation frame
		if self.animationCount >= 1:
			self.animationStage = (self.animationStage + 1) % 3
			self.animationCount -= 1
		#If timere not complete, count timer up based on speed
		else:
			self.animationCount += self.animationSpeed

	#add node to path
	def addNode(self, node):
		nodeList.append(node)

	#move towards next node
	def move(self):
		#change sprite to next frame in animation
		self.iterateAnimation()
		#If no nodes in nodeList, stay put
		if len(self.nodeList) == 0:
			return

		#If at the next node, then we need to turn in the right direction towards the next node
		if self.position.x == self.nodeList[self.nextIndex].x and self.position.y == self.nodeList[self.nextIndex].y:
			#change the next node index
			self.nextIndex = (self.nextIndex + 1) % len(self.nodeList)
			#If the next node is above or below the monster
			if self.nodeList[self.nextIndex].y != self.position.y:
				#Calculate direction
				self.direction = ((self.position.y - self.nodeList[self.nextIndex].y)/abs(self.nodeList[self.nextIndex].y - self.position.y)) + 1
			#If the next node is to the right or left of the monster
			if self.nodeList[self.nextIndex].x != self.position.x:
				#Calculate direction
				self.direction = ((self.position.x - self.nodeList[self.nextIndex].x)/ abs(self.nodeList[self.nextIndex].x - self.position.x)) + 2
		#if not at the next node,  move towards the next node
		else:
			#if we the next node is within the next step, move to it
			#This is so we do not pass it which would break this code
			if abs((self.position.y - self.nodeList[self.nextIndex].y) + (self.position.x - self.nodeList[self.nextIndex].x)) < self.speed:
				self.position = self.nodeList[self.nextIndex]
			#If moving up or down i.e. direction == 0 or 2
			#Move up or down depending on direction
			elif self.direction % 2 == 0:
				#Gets -1 or 1 from direction
				self.position.y += self.speed * (-self.direction + 1)
			#If moving left or right i.e. direction == 1 or 3
			#Move left or right depending on the direction
			else: 
				self.position.x += self.speed * (-self.direction + 2)

	#Return rectangle for collision
	def rect(self):
		return pygame.Rect((self.position.x, self.position.y), (32, 32))

	def __str__(self):
		return "Monster: " + str(self.position) + " next node " + str(self.nodeList[self.nextIndex])
