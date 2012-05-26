# ------------------------------------------------------------
# Filename: grid.py
#
# Author: Shawn Wilkinson
# Author Website: http://super3.org/
# Author Email: me@super3.org
#
# Project: WarCon
# Website: http://super3.org/warcon
# Github Page: https://github.com/super3/warcon
# 
# Creative Commons Attribution 3.0 Unported License
# http://creativecommons.org/licenses/by/3.0/
# ------------------------------------------------------------

# System Imports
import pygame, os
from model.helper import *

class Block(pygame.sprite.Sprite):
	"""
	Basic PyGame Sprite Class.
	Pretty much every sprite should be derived from this.
	Static/immovable objects should use this class directly.
	
	Data members:
	image -- Contains the sprite image (usually imported as a .PNG)
			 Will later be expanded as an array with multiple image
			 so it can support animation
	rect -- Contains the bounds of the loaded image
	rect.x -- Coordinate X of the sprite (measured from the left edge)
	rect.y -- Coordinate Y of the sprite (measured from the bottom edge initially and then as PyGame )
	"""
	def __init__(self, locX, locY, img, worldDim):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		
		# Load the image, if it does not exist try to load the error image. 
		if fileExists( img, "Block Class Image"):
			# Create an image and remove background
			tmpImage = pygame.image.load(img)
		else:
			tmpImage = pygame.image.load('view/tiles/error.png')

		# Takes World Dimentions
		worldX = worldDim[0]
		worldY = worldDim[1]
		groundHeight = worldDim[2]

		# Sets .PNG transparency to PyGame transparency
		self.image = tmpImage.convert_alpha() 
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = locX
		self.rect.y = worldY - (locY + self.rect.height) - groundHeight
	def render(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])

	def Tile(pygame.sprite.Sprite):
		pass

	def Grid(pygame.sprite.Sprite):
		pass