# Video Codec Development

This is a brief introduction to the working of the video codec.

The list of files are :
- core.py : Implements the various classes to perform the actual work
- FrameComparator.py : Accepts an array of matrices. Uses first matrix as reference and returns array of difference matrices between reference matrix and other matrices
- ImageArray.py : Accepts an image and returns its equivalent numpy array
- ImageArrayRev.py : Accepts a numpy array and returns its equivalent image
- VideoToImageArray.py : Accepts a video and returns a set of frames as images inside a folder named 'img_*videoname*'. If audio stream exists, outputs it as an aac audio file.
- ImageArrayToVideo.py : Accepts a set of image frames and returns a video slideshow. If aac audio file exists, attaches the audio to the output video.

## How to run

To run, place a video in the project directory and rename it to '_input.mp4_'. Only '_input.mp4_' is supported for now. It will be changed later. Then to run, type '''python3 core.py''' in the terminal. This will output a video named '_output.mkv_'.
