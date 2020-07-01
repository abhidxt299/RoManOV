# A simple neural network with Python and Keras

Keras is a super powerful, easy to use Python library for building neural networks and deep learning networks.

In the remainder of this chapter, I’ll demonstrate how to build a simple neural network using Python and Keras, and then apply it to the task of image classification.

To start this chapter, we’ll quickly review the most common neural network architecture — feedforward networks.

We’ll then discuss our project structure followed by writing some Python code to define our feedforward neural network and specifically apply it to the Kaggle Dogs vs. Cats classification challenge. The goal of this challenge is to correctly classify whether a given image contains a dog or a cat.

We’ll review the results of our simple neural network architecture and discuss methods to improve it.

Our final step will be to build a test script that will load images and classify them with OpenCV, Keras, and our trained model. Your work would be to apply this concept to classify the chess pawns and chessboard's squares and upload the results in the assignments folder.

# Feedforward neural networks

While there are many, many different neural network architectures, the most common architecture is the feedforward network:

In this type of architecture, a connection between two nodes is only permitted from nodes in layer i to nodes in layer i + 1 (hence the term feedforward; there are no backwards or inter-layer connections allowed).

Furthermore, the nodes in layer i are fully connected to the nodes in layer i + 1. This implies that every node in layer i connects to every node in layer i + 1. For example, in the figure above, there are a total of 2 x 3 = 6 connections between layer 0 and layer 1 — this is where the term “fully connected” or “FC” for short, comes from.

We normally use a sequence of integers to quickly and concisely describe the number of nodes in each layer.

For example, the example network uploaded in this folder is a 3-2-3-2 feedforward neural network:

    Layer 0 contains 3 inputs, our x_{i} values. These could be raw pixel intensities or entries from a feature vector.
    Layers 1 and 2 are hidden layers, containing 2 and 3 nodes, respectively.
    Layer 3 is the output layer or the visible layer — this is where we obtain the overall output classification from our network. The output layer normally has as many nodes as class labels; one node for each potential output. In our Kaggle Dogs vs. Cats example, we have two output nodes — one for “dog” and another for “cat”.

# Project directory structure

Before we begin, download the files and data. From there you’ll be able to follow along as we work through today’s examples.

Once your zip is downloaded, extract the files.

From within the directory, let’s run the tree command with two command line arguments to list our project structure:
```
$ tree --filelimit 10 --dirsfirst
.
├── kaggle_dogs_vs_cats
│ └── train [25000 entries exceeds filelimit, not opening dir]
├── test_images [50 entries exceeds filelimit, not opening dir]
├── output
│ └── simple_neural_network.hdf5
├── simple_neural_network.py
└── test_network.py
4 directories, 4 files
```

# Implementing our own neural network with Python and Keras

Now that we understand the basics of feedforward neural networks, let’s implement one for image classification using Python and Keras.
Run the ```simple_neural_network.py``` code. Comments will guide you through the different functions used.

To train our model, we’ll set the learning rate parameter of SGD to 0.01. We’ll use the ```binary_crossentropy``` loss function for the network as well.

In most cases, you’ll want to use just ```crossentropy```, but since there are only two class labels, we use ```binary_crossentropy```. For > 2 class labels, make sure you use ```crossentropy```.

The network is then allowed to train for a total of 50 epochs, meaning that the model “sees” each individual training example 50 times in an attempt to learn an underlying pattern.

# Classifying images using neural networks with Python and Keras

Execute the simple_neural_network.py script.

The following command can be used to train our neural network using Python and Keras.
```
$ python simple_neural_network.py --dataset kaggle_dogs_vs_cats \
    --model output/simple_neural_network.hdf5
```

At the end of the 50th epoch, we see that we are getting ~76% accuracy on the training data and 67% accuracy on the testing data.

This ~9% difference in accuracy implies that our network is overfitting a bit; however, it is very common to see ~10% gaps in training versus testing accuracy, especially if you have limited training data.

You should start to become very worried regarding overfitting when your training accuracy reaches 90%+ and your testing accuracy is substantially lower than that.

In either case, this 67.376% is the highest accuracy we’ve obtained thus far in this series of tutorials. As we’ll find out later on, we can easily obtain > 95% accuracy by utilizing Convolutional Neural Networks.

# Classifying images using our Keras model

We’re going to build a test script to verify our results visually.

So let’s go ahead and run the ```test_network.py``` code.

# Testing our neural network with Keras

Now that we’re finished implementing our test script, let’s run it and see our hard work in action.

When you have the files extracted, to run our ```test_network.py``` we simply execute it in the terminal and provide two command line arguments:
```
$ python test_network.py --model output/simple_neural_network.hdf5 \
	--test-images test_images
Using TensorFlow backend.
[INFO] loading network architecture and weights...
[INFO] testing on images in test_images
[INFO] classifying 48.jpg
[INFO] classifying 49.jpg
[INFO] classifying 8.jpg
[INFO] classifying 9.jpg
[INFO] classifying 14.jpg
[INFO] classifying 28.jpg
```

Did you see the following error message?
```
Using TensorFlow backend.
usage: test_network.py [-h] -m MODEL -t TEST_IMAGES [-b BATCH_SIZE]
test_network.py: error: the following arguments are required: -m/--model, -t/--test-images
```
This message describes how to use the script with command line arguments.

If everything works out correctly, then you can see the results. There will be a few misclassifications along the way, but that's okay. It's the first neural network you've developed.
