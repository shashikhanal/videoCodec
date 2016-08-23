import os
import subprocess

class VideoToImageArray:
	def __init__(self, videoName):
		self.videoName = videoName
		self.audioName = ""
		self.bitrateVideo = "";
		self.bitrateAudio = "";
		self.framerate = "";

	def convert(self):
		os.system("rm -rf img_"+self.videoName+"/")
		os.system("rm -rf audio_"+self.videoName+".aac")
		os.system("mkdir img_"+ self.videoName)
		os.system("ffmpeg -i "+self.videoName+" -r 25 img_"+self.videoName+"/output_%d.jpg")
		os.system("ffmpeg -i "+self.videoName+" -vn -acodec copy audio_"+self.videoName+".aac")