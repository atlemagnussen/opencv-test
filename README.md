#Just testing open-cv

##test of opencv and ip cam
https://gist.github.com/thearn/5562029
##windows, ffmpeg and path and stuff
[http://kronoskoders.logdown.com/posts/256664-installing-opencv-and-ffmpeg-on-windows]

[http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/]

[http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/]

###Install OpenCV 3.0 and Python 3.4+ on UbuntuShell

$ cd ~/opencv
$ mkdir build
$ cd build

*git checkout 3.1.0 on both repos*

cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..

make -j4
sudo make install