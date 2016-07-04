#python 2.x had PIL library. Python3.x uses Pillow, a fork of PIL compatible with both python 2.x and 3.x
from PIL import Image
#numpy module is needed to use image as numerical array.
import numpy as np
import sys

#from itertools import izip ; izip was needed in python2.x. python3.x has zip as default
#np.seterr(over='ignore') Enable to ignore runtime overflow warning

#Open Log Files
log_op=open("rgb_original_matrix.txt",'w')
log_diff=open("rgb_diff_matrix.txt",'w')
log_re=open("rgb_rec_matrix.txt",'w')

#construct array from image
img=Image.open("img.jpg")
img.load()
original=np.asarray(img)

#skeleton for temporary matrices
original_matrix=[]
diff_matrix=[]
reconstruct_matrix=[]

cp=0

for i,val in enumerate(original):
	print("constructing "+str(i))
	original_matrix.append([x - y for x, y in zip(val, val-val)])

#difference matrix in LIST
for i in original:
	print("differences "+str(cp))
	if(cp>0):
		current_array=i
		diff_matrix.append([x - y for x, y in zip(current_array, temp_array)])
	else:
		diff_matrix.append([x - y for x, y in zip(i, i-i)])
	temp_array = i
	cp=cp+1
	#print >>log_op,original_matrix[cp-1] ; '>>' operator was used in python 2.x 
	#print >>log_diff,diff_matrix[cp-1] ; '>>' operator was used in python 2.x
	print(original_matrix[cp-1], end="", file=log_op)
	print(diff_matrix[cp-1], end="", file=log_diff)

#reconstruct original matrix from difference matrix
cp=0
for i,val in enumerate(diff_matrix):
	print("reconstructing "+str(i))
	if(cp>0):
		reconstruct_matrix.append([x + y for x, y in zip(val, reconstruct_matrix[cp-1])])
	else: 
		reconstruct_matrix.append(val)
	cp=cp+1
	#print >>log_re,reconstruct_matrix[cp-1] ; '>>' operator was used in python 2.x 
	print(reconstruct_matrix[cp-1], end="", file=log_re)


#reconstruct image from array
rec_array=np.asarray(reconstruct_matrix)
im=Image.fromarray(rec_array)
im.save("reconstruct_img_rgb.jpg")