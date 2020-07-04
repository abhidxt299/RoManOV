Today’s post is about measuring the size of objects in an image and computing the distances between them.

In the assignment, you learnt an important technique: how reliably order a set of rotated bounding box coordinates in a top-left, top-right, bottom-right, and bottom-left arrangement.

Today you are going to utilize this technique to aid us in computing the size of objects in an image. Be sure to read the entire chapter to see how it’s done!

# Measuring the size of objects in an image using OpenCV

Measuring the size of objects in an image is similar to computing the distance from our camera to an object — in both cases, we need to define a ratio that measures the number of pixels per a given metric.

We can call this the “pixels per metric” ratio, which has more formally defined in the following section.

## The “pixels per metric” ratio

In order to determine the size of an object in an image, we first need to perform a “calibration” (not to be confused with intrinsic/extrinsic calibration) using a reference object. Our reference object should have two important properties:

    Property #1: We should know the dimensions of this object (in terms of width or height) in a measurable unit (such as millimeters, inches, etc.).
    Property #2: We should be able to easily find this reference object in an image, either based on the placement of the object (such as the reference object always being placed in the top-left corner of an image) or via appearances (like being a distinctive color or shape, unique and different from all other objects in the image). In either case, our reference should should be uniquely identifiable in some manner.

In this example, we ensure it is always the left-most object in our image. You can first try the given image in the chapter, then switch to different images.

By guaranteeing the coin is the left-most object, we can sort our object contours from left-to-right, grab the coin (which will always be the first contour in the sorted list), and use it to define our pixels_per_metric, which we define as:

pixels_per_metric = object_width / know_width

The given coin's known_width is 0.955 inches. Now, suppose that our object_width (measured in pixels) is computed be 150 pixels wide (based on its associated bounding box).

The pixels_per_metric is therefore:

pixels_per_metric = 150px / 0.955in = 157px

Thus implying there are approximately 157 pixels per every 0.955 inches in our image. Using this ratio, we can compute the size of objects in an image.

## Measuring the size of objects with Computer Vision

Now that we understand the “pixels per metric” ratio, we can implement the Python driver script used to measure the size of objects in an image.
Run the ```object_size.py``` code.

We arrange our rotated bounding ```box``` coordinates in top-left, top-right, bottom-right, and bottom-left order, as done in Assignment A1.

## Possible errors

Not all the results are perfect.

So why is this? How come the object measurements are not 100% accurate?

The reason is two-fold:

    1. The angle might most certainly not be a perfect 90-degree angle “looking down” (like a birds-eye-view) at the objects. Without a perfect 90-degree view (or as close to it as possible), the dimensions of the objects can appear distorted.
    2. The camera might not be calibrated using the intrinsic and extrinsic parameters of the camera. Without determining these parameters, photos can be prone to radial and tangential lens distortion. Performing an extra calibration step to find these parameters can “un-distort” our image and lead to a better object size approximation.

In the meantime, strive to obtain as close to a 90-degree viewing angle as possible when taking photos of your objects — this will help increase the accuracy of your object size estimation.

