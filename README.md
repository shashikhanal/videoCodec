# Video Codec Development

This is a brief introduction to the working of the video codec.

The list of files are :
- core.py : Implements the various classes to perform the actual work
- FrameComparator.py : Accepts an array of matrices. Uses first matrix as reference and returns array of difference matrices between reference matrix and other matrices
- ImageArray.py : Accepts an image and returns its equivalent numpy array
- ImageArrayRev.py : Accepts a numpy array and returns its equivalent image
- VideoToImageArray.py : Accepts a video and returns a set of frames as images inside a folder named 'img_videoname'. If audio stream exists, outputs it as an aac audio file.
- ImageArrayToVideo.py : Accepts a set of image frames and returns a video slideshow. If aac audio file exists, attaches the audio to the output video.