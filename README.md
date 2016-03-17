# AutoCam
A program that takes a video from your webcam, puts it through a random function, then shows the resulting video.

This program is like [AutoArt](http://github.com/pommicket/AutoArt), but it takes a video from your webcam and turns it into AutoArt.

AutoCam requires:
 - Python
 - OpenCV
 - Numpy

On Ubuntu/Debian, these can be installed using:
```bash
sudo apt-get install python python-opencv python-numpy
```

On other platforms, you can use pip to install the dependencies.

To run AutoCam:
```bash
cd the/directory/where/AutoCam/is
python rgbautocam.py
```

You can replace rgbautocam with autocam if you want the R, G, and B functions to be the same.
