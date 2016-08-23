from ImgArrayRev import ImgArrayRev
from ImgArray import ImgArray
from FrameComparator import FrameComparator
from VideoToImageArray import VideoToImageArray
from ImageArrayToVideo import ImageArrayToVideo
from DCT import DCT
from MatrixToBlock import MatrixToBlock
import sys
import os
isfile = os.path.isfile
join = os.path.join
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import numpy as np

args = sys.argv
source = args[1]

'''
args = sys.argv
imageName = args[1]
try:
	imageMode = args[2]
except:
	imageMode = "L"
	'''
'''
	refimg = ImgArray("ref.png","-r")
	arrimg = ImgArray("arr.png","-r")

	refarray = refimg.convertToArray()
	arrarray = arrimg.convertToArray()

	frameDiff = FrameComparator([refarray,arrarray])
	print(frameDiff.getDiff())
'''

'''
	image2Array = ImgArray(imageName, imageMode)
	#print(image2Array.convertToArray())
	arr = image2Array.convertToArray()
	print(arr)
	array2Image = ImgArrayRev(arr,"img_g.png",imageMode)
	array2Image.convertToImage()
'''
try:
	V2I = VideoToImageArray(source)
	V2I.convert()

	directory = 'img_'+source
	number_of_files = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))

	print("Print Any Key To Continue")
	#sys.stdin.read(1)
	os.system('cls' if os.name == 'nt' else 'clear')

	os.chdir("./"+directory)
	print("Progress")
	for index in range(1,number_of_files-1):
		if(index % 10 == 0):
			print(str(round((index-1)/number_of_files * 100,2))+"%", end="\r", flush=True)
			#print(index)
			#print("Get Image")
			imgA = ImgArray("output_"+str(index)+".jpg","-r")
			#print("Convert to Array")
			arr = imgA.convertToArray()
			#print("Convert to Image")
			arrI = ImgArrayRev(arr,"output_"+str(index)+".jpg","-r")
			#print("Save Image")
			arrI.convertToImage()

	print("100.00%", end="\r", flush=True)

	os.chdir("..")
	opVName = source.split(".")[0]
	print(" ")
	print("Print Any Key To Continue")
	#sys.stdin.read(1)
	os.system('cls' if os.name == 'nt' else 'clear')
	I2V = ImageArrayToVideo("output",source)
	I2V.convert()
	outputVideo = opVName+".mkv"
	os.system('mv output.mkv '+outputVideo)
	os.system('mv '+outputVideo+" ./min/")
except:
	print("ERROR")
'''
V2I = VideoToImageArray("input.mp4")
#V2I.convert()

directory = 'img_input.mp4'
number_of_files = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))

print("Print Any Key To Continue")
#sys.stdin.read(1)
os.system('cls' if os.name == 'nt' else 'clear')

os.chdir("./"+directory)
print("Progress")

all_arrays = []
for index in range(1,number_of_files-1):
	if(index % 10 == 0):
		print(str(round((index-1)/number_of_files * 100,2))+"%", end="\r", flush=True)
	#print(index)
	#print("Get Image")
	imgA = ImgArray("output_"+str(index)+".jpg","-g")
	#print("Convert to Array")
	arr = imgA.convertToArray()
	print("Array")
	print(arr)

	all_arrays.append(arr)

	print("Print Any Key To Continue")
	#sys.stdin.read(1)


	'''
'''
	mat2block = MatrixToBlock(arr)
	blocks = mat2block.block()
	print("Blocks")
	print(blocks)
	#single = blocks[0]
	#DCTAnalyzer = DCT(single)
	#print(DCTAnalyzer.dct())
	print("Print Any Key To Continue")
	sys.stdin.read(1)
	'''
'''
print("VAR")
for i,val in enumerate(all_arrays):
	print(val)
'''
