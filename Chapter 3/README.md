If you’ve taken other programming courses, the first app you built was probably kind of useless. You built it in order to learn some key elements of syntax or to understand certain programming concepts — loops, conditional statements, and classes, anyone? —  and maybe it even had a bit of a cool factor to it. But it wasn’t something you were going to actually use. 

Well, the app you’re going to build today is one that is definitely useful: a computer vision-powered document scanner.

Building a document scanner with OpenCV can be accomplished in just three simple steps:

    Step 1: Detect edges.
    Step 2: Use the edges in the image to find the contour (outline) representing the piece of paper being scanned.
    Step 3: Apply a perspective transform to obtain the top-down view of the document.

Really. That’s it.

# How to build a mobile document scanner using OpenCV

Let's get started. Open and run the ```scan.py``` file.

## Step 1: Edge Detection

Use the image given in this folder. Run the code. Have a look at the result.

On the left you can see my receipt from Whole Foods. Notice how the picture is captured at an angle. It is definitely not a 90-degree, top-down view of the page. Furthermore, there is also my desk in the image. Certainly this is not a “scan” of any means. We have our work cut out for us.

However, on the right you can see the image after performing edge detection. We can clearly see the outline of the receipt.
Let's get on with Step 2.

## Step 2: Finding Contours

Contour detection doesn’t have to be hard. In fact, when building a document scanner, you actually have a serious advantage…

Take a second to consider what we’re actually building. A document scanner simply scans in a piece of paper. A piece of paper is assumed to be a rectangle. And a rectangle has four edges. Therefore, we can create a simple heuristic to help us build our document scanner.

The heuristic goes something like this: we’ll assume that the largest contour in the image with exactly four points is our piece of paper to be scanned.

This is also a reasonably safe assumption — the scanner app simply assumes that the document you want to scan is the main focus of our image. And it’s also safe to assume (or at least should be) that the piece of paper has four edges.

And that’s exactly what the code above does. Run the code and analyse the results.

As you can see, we have successfully utilized the edge detected image to find the contour (outline) of the document, illustrated by the green rectangle surrounding my receipt.

Lastly, let’s move on to Step 3, which will be a snap using a four_point_transform function.

## Step 3: Apply a perspective transform and threshold

The last step in building a mobile document scanner is to take the four points representing the outline of the document and apply a perspective transform to obtain a top-down, “birds eye view” of the image.

We’ll pass two arguments into four_point_transform: the first is our original image we loaded off disk (not the resized one), and the second argument is the contour representing the document, multiplied by the resized ratio.

So, you may be wondering, why are we multiplying by the resized ratio?

We multiply by the resized ratio because we performed edge detection and found contours on the resized image of height=500 pixels. However, we want to perform the scan on the original image, not the resized image, thus we multiply the contour points by the resized ratio. To obtain the black and white feel to the image, we then take the warped image, convert it to grayscale and apply adaptive thresholding.

Finally, we display our output.

# Python + OpenCV document scanning results

And speaking of output, take a look at our example document by running the script:
```
$ python scan.py --image images/receipt.jpg
```
On the left we have the original image we loaded off disk. And on the right, we have the scanned image!

Notice how the perspective of the scanned image has changed — we have a top-down, 90-degree view of the image.

And thanks to our adaptive thresholding, we also have a nice, clean black and white feel to the document as well.

We have successfully built our document scanner!

All in less than 5 minutes and under 75 lines of code (most of which are comments anyway).
