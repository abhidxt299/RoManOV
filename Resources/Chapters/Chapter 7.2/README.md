So, in chapter 7.1 we saw how to download multiple images from Google in a single go, using a few JavaScript functions. But what if we had a few duplicate images amongst them? Why are duplicate images not favourable while creating a dataset for Deep Learning? Well, let's find out.

Having duplicate images in your dataset creates a problem for two reasons:

    It introduces bias into your dataset, giving your deep neural network additional opportunities to learn patterns specific to the duplicates
    It hurts the ability of your model to generalize to new images outside of what it was trained on

While we often assume that data points in a dataset are independent and identically distributed, that’s rarely (if ever) the case when working with a real-world dataset. When training a Convolutional Neural Network, we typically want to remove those duplicate images before training the model.

Secondly, trying to manually detect duplicate images in a dataset is extremely time-consuming and error-prone — it also doesn’t scale to large image datasets. We therefore need a method to automatically detect and remove duplicate images from our deep learning dataset.

Is such a method possible?

It certainly is — and I’ll be covering it in the remainder of this sub-chapter.

# Detect and remove duplicate images from a dataset for deep learning

In the first part of this sub-chapter, you’ll learn why detecting and removing duplicate images from your dataset is typically a requirement before you attempt to train a deep neural network on top of your data.

From there, we’ll review the example dataset created so we can practice detecting duplicate images in a dataset.

We’ll then implement our image duplicate detector using a method called image hashing.

Finally, we’ll review the results of our work and:

    Perform a dry run to validate that our image duplicate detector is working properly
    Run our duplicate detector a second time, this time removing the actual duplicates from our dataset

# Why bother removing duplicate images from a dataset when training a deep neural network?

If you’ve ever attempted to build your own image dataset by hand, you know it’s a likely possibility (if not an inevitability) that you’ll have duplicate images in your dataset.

Typically, you end up with duplicate images in your dataset by:

    Scraping images from multiple sources (e.g., Google, Bing, etc.)
    Combining existing datasets (ex., combining ImageNet with Sun397 and Indoor Scenes)

When this happens you need a way to:

    Detect that there are duplicate images in your dataset
    Remove the duplicates

But that raises the question — why bother caring about duplicates in the first place?

The usual assumption for supervised machine learning methods is that:

    Data points are independent
    They are identically distributed
    Training and testing data are sampled from the same distribution

The problem is that these assumptions rarely (if ever) hold in practice.

What you really need to be afraid of is your model’s ability to generalize.

If you include multiple identical images in your dataset, your neural network is allowed to see and learn patterns from that image multiple times per epoch.

Your network could become biased toward patterns in those duplicate images, making it less likely to generalize to new images.

Bias and ability to generalize are a big deal in machine learning — they can be hard enough to combat when working with an “ideal” dataset.

Take the time to remove duplicates from your image dataset so you don’t accidentally introduce bias or hurt the ability of your model to generalize.

# Project structure

I’ve included the duplicate image dataset along with the code in this sub-chapter.

Once you extract the ```.zip```, you’ll be presented with the following directory structure:
```
$ tree --dirsfirst --filelimit 10
.
├── dataset [1000 entries]
└── detect_and_remove.py
1 directory, 1 file
```
As you can see, our project structure is quite simple. We have a ```dataset/``` of 1,000 images (duplicates included). Additionally, we have our ```detect_and_remove.py``` Python script, which is the basis of today’s tutorial.

# Implementing our image duplicate detector

We are now ready to implement our image duplicate detector.

Open up the ```detect_and_remove.py``` script in your project directory, and let’s get to work.

Running our image duplicate detector for our deep learning dataset

Let’s put our image duplicate detector to work.

Start by making sure you have downloaded the source code and example dataset.

From there, open up a terminal, and execute the following command just to verify there are 1,000 images in our ```dataset/``` directory:
```
$ ls -l dataset/*.jpg | wc -l
    1000
```

Let’s now perform a dry run, which will allow us to visualize the duplicates in our dataset:
```
$ python detect_and_remove.py --dataset dataset
[INFO] computing image hashes...
[INFO] hash: 7054210665732718398
[INFO] hash: 15443501585133582635
[INFO] hash: 13344784005636363614
```
To actually remove the duplicates from our system, we need to execute ```detect_and_remove.py``` again, this time supplying the ```--remove 1``` command line argument:
```
$ python detect_and_remove.py --dataset dataset --remove 1
[INFO] computing image hashes...
```

We can verify that the duplicates have been removed by counting the number of JPEG Images in the dataset directory:
```
$ ls -l dataset/*.jpg | wc -l
     993
```

Originally, there were 1,000 images in dataset, but now there are 993, implying that we removed the 7 duplicate images.

At this point, you could proceed to train a deep neural network on this dataset. 
