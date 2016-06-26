import numpy as np
from PIL import Image

class ImgArrayRev:
	def __init__(self, arrayName, imgName, imgMode):
		self.arrayName = arrayName
		self.imgMode = imgMode
		self.imgName = imgName
		if(self.imgMode == "-r"):
			self.mode = "RGB"
		elif(self.imgMode == "-g"):
			self.mode = "L"
		elif(self.imgMode == "-y"):
			self.mode = "YCbCr"
		else :
			self.mode = "L"

	def convertToImage(self):
		image = Image.fromarray( self.arrayName, self.mode )
		image.save(self.imgName +".jpg")
