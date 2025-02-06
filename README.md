# BerryPick

This is a repo for recreating and hopefully extending: https://github.com/lboloni/BerryPicker 

The current setup contains the following:
    * AL5D robot
    * Monocular camera
    * Logitech Gamepad F710 ( added with the help of current version of approxeng.input==2.6.4)


## Cloning
If you are interested in tring out yourself you can clone this repo also using:

```shell
git clone https://github.com/KonievicRobert/BerryPick.git
```
Follow the next explanations for a streamlined install

## Libraries needed
    * approxeng.input == 2.6.4
    * torch, torchvision, pandas, numpy
    * matplotlib
    * tqdm
    * pyyaml
    * tensorboardX
    * pyserial
    * opencv-python, opencv-contrib-python

All of this was done on a conda env with python 3.10

```shell
conda create -n berrypick python=3.10
```

In order to connect a new gamepad [approxeng](https://approxeng.github.io/approxeng.input/index.html) site was used 

A [table](https://approxeng.github.io/approxeng.input/simpleusage.html#button-names) of the names for each button found on a simple controller is presented to ease the method of [connecting](https://approxeng.github.io/approxeng.input/profiling.html#profiling) a new controller. 

Don't forget to move the '.yaml' file created to '~/.approxeng.input/' then begin [testing](https://approxeng.github.io/approxeng.input/profiling.html#testing) in order to ensure the steps were done correctly.

For a more streamlined intall of the libraries the following code can be run from the linux terminal inside the git project:

```shell
pip install -r requirements.txt
```
Currently more info can be seen on the [original git](https://github.com/lboloni/BerryPicker)