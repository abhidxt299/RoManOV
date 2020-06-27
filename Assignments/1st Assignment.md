I hope you've went through the previous chapters. This assignment might catch you slightly off-guard but neveretheless, do attempt it! Here we go...


# Question

Here, you've to design an object tracker using Computer Vision techniques. You can use the following example case, although you're free to use any other example you  wish. 

    Step #1: Detect the presence of a colored ball using computer vision techniques.
    Step #2: Track the ball as it moves around in the video frames, drawing its previous positions as it moves.
    
# Clues and Hints

Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. Use deque to take in the coordinates of the object over a period of time. 

While capturing the video, do try to downscale the ```frame``` to have a greater FPS. You can then blur the frame to reduce high frequency noise which will allow you to focus on the structural objects inside the frame.

# Submission Rubric

Submit the raw code, commented out on this folder. File name should be your name_A1.py or name_A1.ipynb
Since this is a pretty small assignment, I expect you guys to be done by tonight.




That's it. Have fun solving :)
