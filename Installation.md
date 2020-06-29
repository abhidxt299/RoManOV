# Dependencies to install for this chapter

Today, I am going to demonstrate how to install dlib with Python bindings on both macOS and Ubuntu.

I highly encourage you to take the time to install dlib on your system.

Starting this chapter, we’ll be diving head first into one of dlib’s core computer vision implementations — facial landmark detection.

I’ll be demonstrating how to use facial landmarks for:

    Face part (i.e., eyes, nose, mouth, etc.) extraction
    Facial alignment
    Blink detection
    …and much more.

But it all starts with getting dlib installed!

To learn how to install dlib with Python bindings on your system, just keep reading.

## How to install dlib

Developed by Davis King, the dlib C++ library is a cross-platform package for threading, networking, numerical operations, machine learning, computer vision, and compression, placing a strong emphasis on extremely high-quality and portable code. The documentation for dlib is also quite fantastic.

From a computer vision perspective, dlib has a number of state-of-the-art implementations, including:

    Facial landmark detection
    Correlation tracking
    Deep metric learning

Over the next few weeks we’ll be exploring some of these techniques, so definitely take the time now to get dlib configured and installed on your system.

Step #1: Install dlib prerequisites

The dlib library only has four primary prerequisites:

    Boost: Boost is a collection of peer-reviewed (i.e., very high quality) C++ libraries that help programmers not get caught up in reinventing the wheel. Boost provides implementations for linear algebra, multithreading, basic image processing, and unit testing, just to name a few.
    Boost.Python: As the name of this library suggests, Boost.Python provides interoperability between the C++ and Python programming language.
    CMake: CMake is an open-source, cross-platform set of tools used to build, test, and package software. You might already be familiar with CMake if you have used it to compile OpenCV on your system.
    X11/XQuartx: Short for “X Window System”, X11 provides a basic framework for GUI development, common on Unix-like operating systems. The macOS/OSX version of X11 is called XQuartz.

### Ubuntu

Installing CMake, Boost, Boost.Python, and X11 can be accomplished easily with apt-get:
```
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libboost-all-dev
```

I assume you already have pip (for managing, installing, and upgrading Python packages) installed on your machine, but if not, you can install pip via:
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
```

After completing these steps, continue to Step #2.

### macOS

In order to install Boost, Boost.Python, and CMake on macOS, you’ll be using the Homebrew package manager. Think of Homebrew as a similar equivalent of Ubuntu’s apt-get only for macOS.

If you haven’t already installed Homebrew, you can do so by executing the following commands:
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew update
```
Hint: You can check if Homebrew is already installed on your machine by executing the brew command in your terminal. If you get a brew: command not found error, then Homebrew is not installed on your machine.

Now that Homebrew is installed, open up your ~/.bash_profile file (create it if it doesn’t exist):
```
$ nano ~/.bash_profile
```
And update your PATH variable to check for packages installed by Homebrew before checking the rest of your system:
```
# Homebrew
export PATH=/usr/local/bin:$PATH
```

We now need to reload the contents of the ~/.bash_profile file via the source command:
```
$ source ~/.bash_profile
```

This command only needs to be executed once. Alternatively, you can open up a new terminal window which will automatically source the ~/.bash_profile for you.

Next, let’s install Python 2.7 and Python 3:
```
$ brew install python
$ brew install python3
```

We can then install CMake, Boost, and Boost.Python:
```
$ brew install cmake
$ brew install boost
$ brew install boost-python --with-python3
```

The --with-python3 flag ensures that Python 3 bindings for Boost.Python are compiled as well — Python 2.7 bindings are compiled by default.

Once you start the boost-python install, the build can take a bit of time (10-15 minutes).

As a sanity check, I would suggest validating that you have both boost and boost-python installed before proceeding:
```
$ brew list | grep 'boost'
boost
boost-python
```

The last step is to install the XQuartz window manager so we can have access to X11. XQuartz is easy to install — just download the .dmg and run the install wizard. After installing, make sure you logout and log back in!

Fun Fact: XQuartz used to be installed by default on OSX 10.5-10.7. We now need to manually install it.

Now that we have our prerequisites installed, let’s continue to our next (optional) step.

Step #2: Access your Python virtual environment (optional)

Using Python’s virtualenv and virtualenvwrapper libraries, we can create separate, independent Python environments for each project we are working on — this is considered a best practice when developing software in the Python programming language.

If you would like to install dlib into a pre-existing Python virtual environment, use the workon command:
```
$ workon <your virtualenv name>
```

For example, if I wanted to access a Python virtual environment named cv, I would use the command:
```
$ workon cv
```

I can also create an entirely separate virtual environment using the mkvirtualenv command — the command below creates a Python 2.7 virtual environment named py2_dlib:
```
$ mkvirtualenv py2_dlib
```

While this command will create a Python 3 virtual environment named py3_dlib:
```
$ mkvirtualenv py3_dlib -p python3
```

Again, please keep in mind that using Python virtual environments are optional, but highly recommended if you are doing any type of Python development.

Step #3: Install dlib with Python bindings

The dlib library doesn’t have any real Python prerequisites, but if you plan on using dlib for any type of computer vision or image processing, I would recommend installing:

    NumPy
    SciPy
    scikit-image

These packages can be installed via pip:
```
$ pip install numpy
$ pip install scipy
$ pip install scikit-image
```
We can now use pip to install dlib as well:
```
$ pip install dlib
```
This command will download the dlib package from PyPI, automatically configure it via CMake, and then compile and install it on your system.

Provided you have the CMake, Boost, Boost.Python, and X11/XQuartz installed on your system, the command should exit without error (leaving you with a successful dlib install).

You should see that dlib has been successfully installed.

Step #4: Test out your dlib install

To test out your dlib installation, just open up a Python shell (making sure to access your virtual environment if you used them), and try to import the dlib library:
```
$ python
Python 3.6.0 (default, Mar  4 2017, 12:32:34) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import dlib
>>>
```
If you’ve installed dlib into the same Python virtual environment that you installed OpenCV, you can access OpenCV as well via your cv2 bindings. Here is an example on an Ubuntu machine:
```
$ python
Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import dlib
>>> import cv2
>>> cv2.__version__
'3.1.0'
>>>
```

Congratulations, you now have dlib installed on your system!
