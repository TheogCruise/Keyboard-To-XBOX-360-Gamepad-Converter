# Installation
This is a program in python that converts keyboard inputs into gamepad inputs for games that require a gamepad.\
\
It requires python along with the following libraries:\
    i.    keyboard\
    ii.   mouse\
    iii.  vgamepad\
    \
Currently I have not added any mappings for the right joystick, I am working on it as to convert the mouse movement into the right joystick.\
\
It uses VGIEM Bus Driver, which can be installed from here https://vigembusdriver.com \
\
*NOTE*: LEFT TRIGGER and RIGHT TRIGGER are currently right click and left click on the mouse.

# Left Stick Buttons:
LEFT_STICK_UP = "w"\
LEFT_STICK_DOWN = "s"\
LEFT_STICK_LEFT = "a"\
LEFT_STICK_RIGHT = "d"

# Gamepad Buttons (A B X Y):
GAMEPAD_A = "space"\
GAMEPAD_B = "left shift"\
GAMEPAD_X = "r"\
GAMEPAD_Y = "1"

# Gamepad Shoulders:
LEFT_SHOULDER = "q"\
RIGHT_SHOULDER = "e"

# Menu Buttons:
START = "p"\
BACK = "o"

# Thumbstick Buttons:
LEFT_THUMB = "k"\
RIGHT_THUMB = "l"

# DPAD Buttons
DPAD_UP = "up"\
DPAD_DOWN = "down"\
DPAD_LEFT = "left"\
DPAD_RIGHT = "right"
