Whether you’re interested in learning how to apply facial recognition to video streams, building a complete deep learning pipeline for image classification, or simply want to tinker with your Raspberry Pi and add image recognition to a hobby project, you’ll need to learn OpenCV somewhere along the way.
Let’s go ahead and get started learning the basics of OpenCV and image processing.

# OpenCV project structure

Download this chapter. From there, navigate to where you downloaded the ```.zip``` in your terminal (```cd```). And then unzip the archive, change working directories (```cd```) into the project folder, and analyze the project structure via ```tree```:
```
$ cd ~/Downloads
$ unzip opencv-tutorial.zip
$ cd opencv-tutorial
$ tree
.
├── jpark.png
├── cv_tut_01.py
├── cv_tut_02.py
└── tetris.png
0 directories, 4 files
```

In this tutorial we’ll be creating two Python scripts to help you learn OpenCV basics

 1. Our first script, ```cv_tut_01.py``` will cover basic image processing operations using an image from the movie, Jurassic Park (```jpark.png```).
 2. From there, ```cv_tut_02.py``` will show you how to use these image processing building blocks to create an OpenCV application to count the number of objects in a Tetris image (```tetris.png```).

Note:
I've tried to comment the code out wherever possible. If you still have any doubts, feel free to ask me.
Also, you can try using your own images here.
