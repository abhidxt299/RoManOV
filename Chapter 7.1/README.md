Our job today is to create a Deep Learning data-set from Google Images which will help in the project. Let's get started.

# Using Google Images for training data and machine learning models

The first step in using Google Images to gather training data for our Convolutional Neural Network is to head to Google Images and enter a query.

In this case we’ll be using the query term “chess pawns”.
The next step is to use a tiny bit of JavaScript to gather the image URLs (which we can then download using Python later in this chapter).

Fire up the JavaScript console (I’ll assume you are using the Chrome web browser, but you can use Firefox as well) by clicking View => Developer => JavaScriptv Console.

From there, we manually intervene with JavaScript. Switch back to the JavaScript console and copy + paste the ```functions.js``` function into the console to simulate a right click on an image.

Each of our URLs will be in the ```contents``` parameter passed to our ```createDownload``` function. Here we first create a ```hiddenElement```. We then populate it with the contents, create a destination link with a filename of ```urls.txt```, and simulate a click of the element.

Ultimately when the ```createDownload``` function runs, your browser will trigger a download. Depending on your browser settings, your download may go to your default download location or you may be prompted to select a name and location for your image URLs file download.

# Downloading Google Images using Python

Now that we have our ```urls.txt``` file, we need to download each of the individual images.

Using Python and the requests library, this is quite easy.

If you don’t already have requests installed on your machine you’ll want to install it now (taking care to use the ```workon``` command first if you are using Python virtual environments):
```
$ workon cv
$ pip install requests
```

From there, run the ```download_images.py``` code.

To download our example images, make sure you download the script and the ```urls.txt``` file in a single folder.

From there, open up a terminal and execute the following command:
```
$ python download_images.py --urls urls.txt --output images/chess_pawns
```
The error you see in the output is normal — you should expect these. You should also expect some images to be corrupt and unable to open — these images get deleted from our dataset.

# Pruning irrelevant images from our dataset

Of course, not every image we downloaded is relevant.

To resolve this, we need to do a bit of manual inspection.

