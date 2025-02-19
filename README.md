# BerryPick

This is a repo for recreating and hopefully extending: https://github.com/lboloni/BerryPicker 

The current setup contains the following:

* AL5D robot
* Monocular camera
* Logitech Gamepad F710 (added with the help of current version of approxeng.input==2.6.4)


## Cloning
If you are interested in trying out yourself you can clone this repo also using:

```
git clone https://github.com/KonievicRobert/BerryPick.git
```
Follow the next explanations for a streamlined install.

## Libraries needed
* approxeng.input == 2.6.4
* torch, torchvision, pandas, numpy
* matplotlib
* tqdm
* pyyaml
* tensorboardX
* pyserial
* opencv-python, opencv-contrib-python

All of this was done on a conda env with python 3.10:

```
conda create -n berrypick python=3.10
```

In order to connect a new gamepad [approxeng](https://approxeng.github.io/approxeng.input/index.html) site was used 

A [table](https://approxeng.github.io/approxeng.input/simpleusage.html#button-names) of the names for each button found on a simple controller is presented to ease the method of [connecting](https://approxeng.github.io/approxeng.input/profiling.html#profiling) a new controller. 

Do not forget to move the '.yaml' file created to '~/.approxeng.input/' then begin [testing](https://approxeng.github.io/approxeng.input/profiling.html#testing) in order to ensure the steps were done correctly.

For a more streamlined install of the libraries the following code can be run from the linux terminal inside the git project:

```
pip install -r requirements.txt # it will take around 5 minutes to complete
```

## Initial setup

There are two '.yaml' files for configuration, the original ones are denoted '*-sample.yaml' while the modified ones are named:

* 'mainsettings.yaml' which contains the absolute path to the 'settings.yaml' file within the project directory and needs to be placed at 'HOMEDIR/.config/BerryPicker/mainsettings.yaml'
* 'settings.yaml' is completed with paths according to the explanations from the sample file

Details on 'settings.yaml':

* After connecting the robot and camera in terminal type the following:

    1. ```ls \dev\ttyUSB*``` # to see which port is for the robot
    2. ```sudo chmod a+rw /dev/ttyUSBx``` # where x is the port number
    3. ```ls /dev/video*``` # to see which video port is used by the camera, generally it is an even number
    4. Optionally to check camera feed use: ```sudo apt install ffmpeg``` 
    5. ```ffplay /dev/videoX``` # where X is the video port number
* Add found ports to settings.yaml file
* For demo directory create a folder called demos and write the path to it without the folder name
* Same for training folder
* Clone [this git](https://github.com/julian-8897/Conv-VAE-PyTorch) and add paths in the conv_vae part of the file

### Testing setup

In exploratory_experiments [this file verifies the robot setup](BerryPicker/src/exploratory_experiments/VerifyRobotSetup.ipynb). Test that the robot turns on and off, camera feed is live and that you can see values from the controller.


## Collect demonstrations

After the camera is set in a good position to watch the robot, in the demos folder create a task:

```
mkdir random-uncluttered
```

Run the app in the [src](BerryPicker/src/main.py) folder using:
```
python main.py
```


## Task list
- [ ] GitIgnore setup
- [x] AL5D robot setup
- [x] Collect demonstrations
- [ ] Annotate demonstrations
- [ ] Learn policy
- [ ] Run robot
- [ ] Add a new robot

Currently more info can be seen on the [original git](https://github.com/lboloni/BerryPicker)