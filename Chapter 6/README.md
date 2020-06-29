Today we are going to use dlib and OpenCV to detect facial landmarks in an image.

Facial landmarks are used to localize and represent salient regions of the face, such as:

    Eyes
    Eyebrows
    Nose
    Mouth
    Jawline

In today’s chapter we’ll be focusing on the basics of facial landmarks, including:

    Exactly what facial landmarks are and how they work.
    How to detect and extract facial landmarks from an image using dlib, OpenCV, and Python.

# What are facial landmarks?

Detecting facial landmarks is a subset of the shape prediction problem. Given an input image (and normally an ROI that specifies the object of interest), a shape predictor attempts to localize key points of interest along the shape.

In the context of facial landmarks, our goal is detect important facial structures on the face using shape prediction methods.

Detecting facial landmarks is therefore a two step process:

    Step #1: Localize the face in the image.
    Step #2: Detect the key facial structures on the face ROI.

Face detection (Step #1) can be achieved in a number of ways.

We could use OpenCV’s built-in Haar cascades.

We might apply a pre-trained HOG + Linear SVM object detector specifically for the task of face detection.

Or we might even use deep learning-based algorithms for face localization.

In either case, the actual algorithm used to detect the face in the image doesn’t matter. Instead, what’s important is that through some method we obtain the face bounding box (i.e., the (x, y)-coordinates of the face in the image).

Given the face region we can then apply Step #2: detecting key facial structures in the face region.

There are a variety of facial landmark detectors, but all methods essentially try to localize and label the following facial regions:

    Mouth
    Right eyebrow
    Left eyebrow
    Right eye
    Left eye
    Nose
    Jaw

The facial landmark detector included in the dlib library is an implementation of the One Millisecond Face Alignment with an Ensemble of Regression Trees paper by Kazemi and Sullivan (2014).

This method starts by using:

    A training set of labeled facial landmarks on an image. These images are manually labeled, specifying specific (x, y)-coordinates of regions surrounding each facial structure.
    Priors, of more specifically, the probability on distance between pairs of input pixels.

Given this training data, an ensemble of regression trees are trained to estimate the facial landmark positions directly from the pixel intensities themselves (i.e., no “feature extraction” is taking place).

The end result is a facial landmark detector that can be used to detect facial landmarks in real-time with high quality predictions.

# Understanding dlib’s facial landmark detector

The pre-trained facial landmark detector inside the dlib library is used to estimate the location of 68 (x, y)-coordinates that map to facial structures on the face.

These annotations are part of the 68 point iBUG 300-W dataset which the dlib facial landmark predictor was trained on.

It’s important to note that other flavors of facial landmark detectors exist, including the 194 point model that can be trained on the HELEN dataset.

Regardless of which dataset is used, the same dlib framework can be leveraged to train a shape predictor on the input training data — this is useful if you would like to train facial landmark detectors or custom shape predictors of your own.

In the remaining of this chapter I’ll demonstrate how to detect these facial landmarks in images.

# Detecting facial landmarks with dlib, OpenCV, and Python

In order to prepare for this chapter on facial landmarks, I’ve added a few convenience functions to my imutils library, specifically inside face_utils.py.

We’ll be reviewing two of these functions inside ```face_utils.py``` now.

The first utility function is ```rect_to_bb```, short for “rectangle to bounding box".

Secondly, we have the ```shape_to_np``` function.

Using the shape_to_np
  function, we cam convert this object to a NumPy array, allowing it to “play nicer” with our Python code.

Given these two helper functions, we are now ready to detect facial landmarks in images.

Run the ```facial_landmarks.py``` code.

The first parameter to the ```detector``` is our grayscale image (although this method can work with color images as well).

The second parameter is the number of image pyramid layers to apply when upscaling the image prior to applying the detector (this it the equivalent of computing ```cv2.pyrUp``` N number of times on the image).

The benefit of increasing the resolution of the input image prior to face detection is that it may allow us to detect more faces in the image — the downside is that the larger the input image, the more computaitonally expensive the detection process is.

# Facial landmark visualizations

Before we test our facial landmark detector, make sure you have upgraded to the latest version of ```imutils``` which includes the ```face_utils.py``` file:
```
$ pip install --upgrade imutils
```
Note: If you are using Python virtual environments, make sure you upgrade the imutils inside the virtual environment.

Once you’ve downloaded the .zip archive, unzip it, change directory to ```facial-landmarks```, and execute the following command:
```
$ python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat \
	--image images/example_01.jpg
```

Here, example_01.jpg can mean any image. You can try this code out with your selfies also :)
