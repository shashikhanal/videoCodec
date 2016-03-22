import Image,numpy,sys,scipy
from itertools import izip

log_op=open("original_matrix.txt",'w')
log_diff=open("diff_matrix.txt",'w')
log_re=open("rec_matrix.txt",'w')

#construct array from image
img=Image.open("img1.jpg").convert("L")
#img.load()
original=numpy.asarray(img)

original_matrix=[]
diff_matrix=[]
reconstruct_matrix=[]

temp_array=[]

cp=0
#original matrix in LIST
for i,val in enumerate(original):
	original_matrix.append([x - y for x, y in izip(val, val-val)])

#difference matrix in LIST
for i in original:
	if(cp>0):
		current_array=i
		diff_matrix.append([x - y for x, y in izip(current_array, temp_array)])
	else:
		diff_matrix.append([x - y for x, y in izip(i, i-i)])
	temp_array = i
	cp=cp+1
	print >>log_op,original_matrix[cp-1]
	print >>log_diff,diff_matrix[cp-1]

#reconstruct original matrix from difference matrix
cp=0
for i,val in enumerate(diff_matrix):
	if(cp>0):
		reconstruct_matrix.append([x + y for x, y in izip(val, reconstruct_matrix[cp-1])])
	else: 
		reconstruct_matrix.append(val)
	cp=cp+1
	print >>log_re,reconstruct_matrix[cp-1]

#reconstruct image from array
rec_array=numpy.asarray(reconstruct_matrix)
im=Image.fromarray(rec_array)
im.save("reconstruct_img.jpg")