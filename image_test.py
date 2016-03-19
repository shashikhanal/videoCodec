import Image,numpy,sys
from itertools import izip
output=numpy.asarray(Image.open("img1.jpg").convert('L'))
#print output
#f=open("output.txt","w")
#f.write(output)
diff_matrix=[]
temp_arr=[]
for i in output:
	print i
print output
count=0
for i in output[0]:
	count=count+1
print count
first_frame=output[0]
temp_arr=output[0]
diff_matrix.append(output[0])
for i in output:
	current_array=i;
	diff_matrix.append([x - y for x, y in izip(current_array, temp_arr)])
	temp_arr = i;
	#print diff_matrix
	#print "###################"
print diff_matrix
print output