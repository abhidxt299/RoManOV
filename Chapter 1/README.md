# How does the OpenCV deep learning face detector work?

OpenCV’s deep learning face detector is based on the Single Shot Detector (SSD) framework with a ResNet base network (unlike other OpenCV SSDs that you may have seen which typically use MobileNet as the base network).

# Face detection in images with OpenCV and deep learning

In this first example we’ll learn how to apply face detection with OpenCV to single input images. In the next section we’ll learn how to modify this code and apply face detection with OpenCV to videos, video streams, and webcams.
For now, run the detect_faces.py file in this folder.

# Face detection in images with OpenCV results

Let’s try out the OpenCV deep learning face detector.

First, run the following:

    The source code uploaded
    The Caffe prototxt files for deep learning face detection
    The Caffe weight files used for deep learning face detection

From there, open up a terminal and execute the following command (Use your own images here):
```
$ python detect_faces.py --image rooster.jpg --prototxt deploy.prototxt.txt \
	--model res10_300x300_ssd_iter_140000.caffemodel
```

# Face detection in video and webcam with OpenCV and deep learning

Now that we have learned how to apply face detection with OpenCV to single images, let’s also apply face detection to videos, video streams, and webcams.

Luckily for us, most of our code in the previous section on face detection with OpenCV in single images can be reused here!

Run detect_faces_video.py 

A few quick notes here:

 1. Raspberry Pi + picamera users can replace Line 25 with 
 ```
 vs = VideoStream(usePiCamera=True).start()
 ```
 if you wish to use the Raspberry Pi camera module.
 
 2. If you to parse a video file (rather than a video stream) swap out the 
 ```
 VideoStream
 ``` 
 class for 
 ```
 FileVideoStream
 ```

# Face detection in video and webcam with OpenCV results

Use the following:

   The source code uploaded
   The Caffe prototxt files for deep learning face detection
   The Caffe weight files used for deep learning face detection

Once you have these files, running the deep learning OpenCV face detector with a webcam feed is easy with this simple command (Use your own images here):
```
$ python detect_faces_video.py --prototxt deploy.prototxt.txt \
	--model res10_300x300_ssd_iter_140000.caffemodel
```

For additional info on caffemodels, follow this link:
https://shengshuyang.github.io/A-step-by-step-guide-to-Caffe.html
