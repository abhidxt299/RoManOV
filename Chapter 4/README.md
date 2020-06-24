You’ve already seen how you can use computer vision effectively to scan documents in the previous chapter, but why stop there?

Wouldn’t it be more useful if you could actually do something with the information you scanned?

For example, remember those “achievement tests” back in elementary school? How about JEE, BITSAT and all the rest of the standardized tests you had to go through to get to where you are today? 

Knowing that your entire future rests on the circles you fill in during three hours of testing, trying to remember strategies for when you don’t know the answer to a question (Always choose C? Never choose C? Skip it? Never skip it? ) — okay, I may have a bit of residual testing anxiety.

And did you ever even give any thought to how these exams were actually graded? 

You probably wouldn’t want to grade all those exams by hand. Instead, you’d want to build a system that can automatically grade the exams. But how do you go about building such a system? And is it possible to create such a system using computer vision?

We’re going to start with the techniques we covered in yesterday’s document scanner lesson and add some new techniques to create a functional bubble sheet scanner and test grader. Let's dive right into it.

# Bubble sheet scanner and test grader using OMR, Python, and OpenCV

The goal here is to build a bubble sheet scanner and test grader using Python and OpenCV.

To accomplish this, our implementation will need to satisfy the following 7 steps:

    Step #1: Detect the exam in an image.
    Step #2: Apply a perspective transform to extract the top-down, birds-eye-view of the exam.
    Step #3: Extract the set of bubbles (i.e., the possible answer choices) from the perspective transformed exam.
    Step #4: Sort the questions/bubbles into rows.
    Step #5: Determine the marked (i.e., “bubbled in”) answer for each row.
    Step #6: Lookup the correct answer in our answer key to determine if the user was correct in their choice.
    Step #7: Repeat for all questions in the exam.

## The bubble sheet scanner implementation with Python and OpenCV

To get started, open and run the ```test_grader.py``` file.

We make the assumption that our exam will be the main focal point of the image, and thus be larger than other objects in the image. This assumption allows us to “filter” our contours, simply by investigating their area and knowing that the contour that corresponds to the exam should be near the front of the list.

However, contour area and size is not enough — we should also check the number of vertices on the contour. The code takes care of this issue.

Now that we have used contours to find the outline of the exam, we can apply a perspective transform to obtain a top-down, birds-eye-view of the document.
In this case, we’ll be using the previous implementation of the four_point_transform function which:

  1. Orders the (x, y)-coordinates of our contours in a specific, reproducible manner.
  2. Applies a perspective transform to the region.
  
Now the question arises as to how the grading is done.
This step starts with binarization, or the process of thresholding/segmenting the foreground from the background of the image. After applying Otsu’s thresholding method, our exam is now a binary image.

In order for a contour area to be considered a bubble, the region should:

  1. Be sufficiently wide and tall (in this case, at least 20 pixels in both dimensions).
  2. Have an aspect ratio that is approximately equal to 1.

As long as these checks hold, we can update our ```questionCnts``` list and mark the region as a bubble.

We can now move on to the “grading” portion of our OMR system.

Since each question has 5 possible answers, we’ll apply NumPy array slicing and contour sorting to to sort the current set of contours from left to right.

The reason this methodology works is because we have already sorted our contours from top-to-bottom. We know that the 5 bubbles for each question will appear sequentially in our list — but we do not know whether these bubbles will be sorted from left-to-right. The sort contour call takes care of this issue and ensures each row of contours are sorted into rows, from left-to-right.

Given a row of bubbles, the next step is to determine which bubble is filled in.

We can accomplish this by using our ```thresh``` image and counting the number of non-zero pixels (i.e., foreground pixels) in each bubble region.

Based on whether the test taker was correct or incorrect yields which color is drawn on the exam. If the test taker is correct, we’ll highlight their answer in green. However, if the test taker made a mistake and marked an incorrect answer, we’ll let them know by highlighting the correct answer in red.

# Extension of the chapter

Since we determine if a particular bubble is “filled in” simply by counting the number of thresholded pixels in a row and then sorting in descending order, this can lead to two problems:

  1. What happens if a user does not bubble in an answer for a particular question?
  2. What if the user is nefarious and marks multiple bubbles as “correct” in the same row?
 
For issue #1, if a reader chooses not to bubble in an answer for a particular row, then we can place a minimum threshold on Line 108 of the code I've uploaded where we compute ```cv2.countNonZero```. If this value is sufficiently large, then we can mark the bubble as “filled in”. Conversely, if total is too small, then we can skip that particular bubble. If at the end of the row there are no bubbles with sufficiently large threshold counts, we can mark the question as “skipped” by the test taker.

A similar set of steps can be applied to issue #2, where a user marks multiple bubbles as correct for a single question.

Again, all we need to do is apply our thresholding and count step, this time keeping track if there are multiple bubbles that have a total that exceeds some pre-defined value. If so, we can invalidate the question and mark the question as incorrect.
