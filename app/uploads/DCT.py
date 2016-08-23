import numpy as np
from scipy import fftpack

class DCT:
	def __init__(self,matrix):
		self.matrix = matrix
		self.dct_matrix = []

	def dct(self):
		dct_matrix = fftpack.dct(self.matrix,norm='ortho')
		return dct_matrix