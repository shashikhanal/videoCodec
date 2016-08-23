import numpy as np

class MatrixToBlock:
	def __init__(self,matrix):
		self.matrix = matrix
		self.blocks = []

	def block(self):
		windowsize_r = 8
		windowsize_c = 8

		for r in range(0,self.matrix.shape[0] - windowsize_r, windowsize_r):
			for c in range(0,self.matrix.shape[1] - windowsize_c, windowsize_c):
				self.blocks.append(self.matrix[r:r+windowsize_r,c:c+windowsize_c])

		return self.blocks
