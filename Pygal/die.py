from random import randint


class Die():
	def __init__(self,numsides=6):
		self.numsides = numsides


	def roll(self):
		return randint(1,self.numsides)

