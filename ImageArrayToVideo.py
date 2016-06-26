import os
class ImageArrayToVideo:
	def __init__(self, videoName, original):
		self.videoName = videoName
		self.original = original;

	def convert(self):
		os.system("rm -rf "+self.videoName+".mp4")
		#os.system("ffmpeg -framerate 24 -i img_"+self.original+"/output_%d.png -c:v libx264 -profile:v main -r 24 -pix_fmt yuv420p "+self.videoName+".mp4")
		if(os.path.isfile("audio_"+self.videoName+".aac") ):
			os.system("ffmpeg -i img_"+self.original+"/output_%d.tiff -i audio_"+self.videoName+".aac -c:v libx264 -profile:v main -r 25 -pix_fmt yuv420p "+self.videoName+".mp4")
		else:
			os.system("ffmpeg -i img_"+self.original+"/output_%d.tiff -c:v libx264 -profile:v main -r 25 -pix_fmt yuv420p "+self.videoName+".mp4")
		os.system("rm -rf img_"+self.original+"/")
		os.system("rm -rf audio_"+self.original+".aac")

