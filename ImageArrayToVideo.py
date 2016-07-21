import os
class ImageArrayToVideo:
	def __init__(self, videoName, original):
		self.videoName = videoName
		self.original = original;

	def convert(self):
		os.system("rm -rf "+self.videoName+".mp4")
		os.system("rm -rf "+self.videoName+".mkv")
		#os.system("ffmpeg -framerate 24 -i img_"+self.original+"/output_%d.png -c:v libx264 -profile:v main -r 24 -pix_fmt yuv420p "+self.videoName+".mp4")
		if(os.path.isfile("audio_"+self.original+".aac") ):
			print("Audio Detected")
			print("--------------################--------------------")
			os.system("ffmpeg -i img_"+self.original+"/output_%d.jpg -i audio_"+self.original+".aac -c:v libx265 -crf 30 -r 25 -pix_fmt yuv420p "+self.videoName+".mkv")
		else:
			print("No Audio")
			print("______________###############-------------")
			os.system("ffmpeg -i img_"+self.original+"/output_%d.jpg -c:v libx265 -crf 30 -r 25 -pix_fmt yuv420p "+self.videoName+".mkv")
		os.system("rm -rf img_"+self.original+"/")
		os.system("rm -rf audio_"+self.original+".aac")

