from ImgArrayRev import ImgArrayRev
from ImgArray import ImgArray
from FrameComparator import FrameComparator
from VideoToImageArray import VideoToImageArray
from ImageArrayToVideo import ImageArrayToVideo
import sys

'''args = sys.argv
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
array2Image = ImgArrayRev(arr,"img_g.jpg",imageMode)
array2Image.convertToImage()
'''

V2I = VideoToImageArray("input.mp4")
V2I.convert()

I2V = ImageArrayToVideo("output","input.mp4")
I2V.convert()