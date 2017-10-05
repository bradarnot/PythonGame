#Created by Bradley Arnot
#Just a simple class to store the x and y of a position
class Position:
	
	#Store x, and y
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	#Swap one position with another
	def swap(self, other):
		xtemp = self.x
		ytemp = self.y
		self.x = other.x
		self.y = other.y
		other.x = xtemp
		other.y = ytemp

	#Returns true if one position is exactly the same as the other
	def equals(self, other):
		return (self.x == other.x) and (self.y == other.y)

	#Adds two positions together
	def add(self, other):
		return Position(other.x + self.x, other.y + self.y)

	#Return the position as a string for printing and debuggging
	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"
