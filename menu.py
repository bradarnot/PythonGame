#Created by Bradley Arnot
import pygame

class Menu:

	def __init__(self, screenSize):
		self.screenSize = screenSize
		#The different selections on the screen the player can choose from
		self.highScores = []
		self.highPlayers = []
		self.selectionsMain = ["Play Game!", "High Scores","How to Play"]
		self.selectionsInitials = ['a', 'a', 'a']
		#The index of the selection in main that is active
		self.active = 0
		#The index of active selection, initial, in the high scores that is active
		self.activeInitial = 0
		#The screen being drawn
		#0 - main menu
		#1 - high scores
		self.screen = 0;
		self.nextScore = 0;
		#background to menu screen
		self.background = pygame.Surface((self.screenSize[0], self.screenSize[1]))
		self.background.fill((200, 200, 200))
		self.font = pygame.font.Font(None, 30)
		self.fontTitle = pygame.font.Font(None, 40)
		self.characterSprite = pygame.image.load("img/charactersheet.png")
		self.princessSprite = pygame.image.load("img/people.png")

	def draw(self, screen):
		screen.blit(self.background, (0, 0))
		if self.screen == 0:
			screen.blit(self.fontTitle.render("Animated Dungeon", False, (0, 0, 0)), (self.screenSize[0]/2 - 100, 50))
			i = 0
			for selection in self.selectionsMain:
				if self.selectionsMain[self.active] == selection:
					screen.blit(self.font.render(selection, False, (255, 0, 0)), (self.screenSize[0]*3/4, self.screenSize[1]/2 + (i * self.font.get_height())))
				else:
					screen.blit(self.font.render(selection, False, (0, 0, 0)), (self.screenSize[0]*3/4, self.screenSize[1]/2 + (i * self.font.get_height())))
				i+=1
		elif self.screen == 1:
			screen.blit(self.fontTitle.render("High Scores", False, (0, 0, 0)), (self.screenSize[0]/2 - 75, 50))
			if len(self.highScores) == 0:
				screen.blit(self.font.render("No High Scores", False, (0, 0, 0)), (self.screenSize[0]/2 - 80, 100))
			else:
				screen.blit(self.font.render("Place", False, (0, 0, 0)), (self.screenSize[0]/2 - 140, 100))
				screen.blit(self.font.render("Initials", False, (0, 0, 0)), (self.screenSize[0]/2 - 50, 100))
				screen.blit(self.font.render("Score", False, (0, 0, 0)), (self.screenSize[0]/2 + 70, 100))
				for i in range(0, len(self.highScores)):
					#screen.blit(self.font.render(str(i) + "\t" + self.highPlayers[i] + "\t" + str(self.highScores[i]), False, (0, 0, 0)), (self.size[0]/8, 100 + i * self.font.get_height()))
					screen.blit(self.font.render(str(i + 1), False, (0, 0, 0)), (self.screenSize[0]/2 - 140, 140 + i*self.font.get_height()))
					screen.blit(self.font.render(self.highPlayers[i], False, (0, 0, 0)), (self.screenSize[0]/2 - 50, 140 + i*self.font.get_height()))
					screen.blit(self.font.render(str(self.highScores[i]), False, (0, 0, 0)), (self.screenSize[0]/2 + 70, 140 + i*self.font.get_height()))
		elif self.screen == 2:
			screen.blit(self.font.render("You Win!!!", False, (0, 0, 0)), (self.screenSize[0]/2 - 90, 50))
			screen.blit(self.font.render("Your score is " + str(self.nextScore), False, (0, 0, 0)), (self.screenSize[0]/2 - 100, 50 + self.font.get_height()))
			screen.blit(self.font.render("Please enter your initals below", False, (0, 0, 0)), (self.screenSize[0]/2 - 140, 50 + 2*self.font.get_height()))
			screen.blit(self.font.render("Place", False, (0, 0, 0)), (self.screenSize[0]/2 - 140, self.screenSize[1]/2))
			screen.blit(self.font.render("Initials", False, (0, 0, 0)), (self.screenSize[0]/2 - 50, self.screenSize[1]/2))
			screen.blit(self.font.render("Score", False, (0, 0, 0)), (self.screenSize[0]/2 + 70, self.screenSize[1]/2))
			screen.blit(self.characterSprite, (self.screenSize[0]/2 - 36, self.screenSize[1]/2 - 100), ((32, 64), (32, 32)))
			screen.blit(self.princessSprite, (self.screenSize[0]/2 + 4, self.screenSize[1]/2 - 100), ((128, 160), (32, 32)))
			place = self.findPlace()
			screen.blit(self.font.render(str(place + 1), False, (0, 0, 0)), (self.screenSize[0]/2 - 140, self.screenSize[1]/2 + self.font.get_height()))
			for i in range(0, len(self.selectionsInitials)):
				if i == self.activeInitial:
					screen.blit(self.font.render(str(self.selectionsInitials[i]), False, (255, 0, 0)), (self.screenSize[0]/2 - 50 + 30*i, self.screenSize[1]/2 + self.font.get_height()))
				else:
					screen.blit(self.font.render(str(self.selectionsInitials[i]), False, (0, 0, 0)), (self.screenSize[0]/2 - 50 + 30*i, self.screenSize[1]/2 + self.font.get_height()))
			screen.blit(self.font.render(str(self.nextScore), False, (0, 0, 0)), (self.screenSize[0]/2 + 70, self.screenSize[1]/2 + self.font.get_height()))
			

	#Go to win screen and take in the players score
	def win(self, score):
		self.screen = 2
		self.nextScore = score

	#Adds the next high score into the array and resets
	def addHighScore(self):
		if len(self.highScores) == 0:
			self.highScores.append(self.nextScore)
			self.highPlayers.append(self.selectionsInitials[0] + self.selectionsInitials[1] + self.selectionsInitials[2])
		else:
			i = self.findPlace()
			self.highScores.insert(i, self.nextScore)
			self.highPlayers.insert(i, self.selectionsInitials[0] + self.selectionsInitials[1] + self.selectionsInitials[2])
		self.selectionsInitials[0] = 'a'
		self.selectionsInitials[1] = 'a'
		self.selectionsInitials[2] = 'a'

	#returns the index of where the next High Score fits 
	def findPlace(self):
		i = 0
		while i < len(self.highScores) and self.nextScore < self.highScores[i]:
			i+=1
		return i;

	def chooseSelection(self):
		if self.screen == 1 or self.screen == 2:
			self.screen = 0
			return ""
		elif self.active == 1:
			self.screen = 1
		return self.selectionsMain[self.active]

	def update(self, event):
		if self.screen == 0:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				self.active = (self.active + 1) % len(self.selectionsMain)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
				self.active = (self.active - 1) % len(self.selectionsMain)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				if self.selectionsMain[self.active] == "High Scores":
					self.screen = 1
				return self.selectionsMain[self.active]
		elif self.screen == 2:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				self.selectionsInitials[self.activeInitial] = chr(((ord(self.selectionsInitials[self.activeInitial]) - ord('a') + 1) % 26) + ord('a'))
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
				self.selectionsInitials[self.activeInitial] = chr(((ord(self.selectionsInitials[self.activeInitial]) - ord('a') - 1) % 26) + ord('a'))
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
				self.activeInitial = (self.activeInitial + 1) % len(self.selectionsInitials)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
				self.activeInitial = (self.activeInitial - 1) % len(self.selectionsInitials)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				self.addHighScore()
				self.screen = 0
				self.active = 0
				return 1;
			return 0;
				
		elif self.screen == 1:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				self.screen = 0
			

