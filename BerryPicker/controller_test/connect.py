from approxeng.input.selectbinder import ControllerResource

while True:
    try:
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            while joystick.connected:
                # Do stuff with your joystick here!
                # ....
                # Get a corrected value for the left stick x-axis
                left_x = joystick['lx']
                # We can also get values as attributes:
                left_y = joystick.ly
                # ....
        # Joystick disconnected...
        print('Connection to joystick lost')
    except IOError:
        # No joystick found, wait for a bit before trying again
        print('Unable to find any joysticks')
        # sleep(1.0)