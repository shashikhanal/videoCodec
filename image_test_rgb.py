import Image,numpy,sys,scipy
from itertools import izip

log_op=open("rgb_original_matrix.txt",'w')
log_diff=open("rgb_diff_matrix.txt",'w')
log_re=open("rgb_rec_matrix.txt",'w')

#construct array from image
img=Image.open("img1.jpg")
img.load()
original=numpy.asarray(img)

original_matrix=[]
diff_matrix=[]
reconstruct_matrix=[]

cp=0

for i,val in enumerate(original):
	print "constructing "+str(i)
	original_matrix.append([x - y for x, y in izip(val, val-val)])

#difference matrix in LIST
for i in original:
	print "differences "+str(cp)
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
	print "reconstructing "+str(i)
	if(cp>0):
		reconstruct_matrix.append([x + y for x, y in izip(val, reconstruct_matrix[cp-1])])
	else: 
		reconstruct_matrix.append(val)
	cp=cp+1
	print >>log_re,reconstruct_matrix[cp-1]


#reconstruct image from array
rec_array=numpy.asarray(reconstruct_matrix)
im=Image.fromarray(rec_array)
im.save("reconstruct_img_rgb.jpg")