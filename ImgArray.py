import numpy as np
from PIL import Image

class ImgArray:
	def __init__(self, imgName, imgMode):
		self.imgName = imgName
		self.imgMode = imgMode
		if(self.imgMode == "-r"):
			self.mode = "RGB"
		elif(self.imgMode == "-g"):
			self.mode = "L"
		elif(self.imgMode == "-y"):
			self.mode = "YCbCr"
		else:
			self.mode = "L"

	def convertToArray(self):
		image = Image.open(self.imgName).convert(self.mode)
		image.load()
		#print(self.imgName)
		#print(np.asarray(image))
		return np.asarray(image)
