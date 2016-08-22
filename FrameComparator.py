import numpy as np

class FrameComparator:
	def __init__(self, arrayList):
		self.lengthOfArray = len(arrayList)
		self.arrayList = arrayList
		self.diffArray = []

	
	def getDiff(self):
		reference = self.arrayList[0]
		self.diffArray.append(reference)
		for index in range(1,self.lengthOfArray):
			diff = reference - self.arrayList[index]
			self.diffArray.append(diff)
		return np.asarray(self.diffArray)

