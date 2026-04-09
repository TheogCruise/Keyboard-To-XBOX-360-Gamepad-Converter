import keyboard
import mouse
import vgamepad as vg


# Left Stick Buttons:
LEFT_STICK_UP = "w"
LEFT_STICK_DOWN = "s"
LEFT_STICK_LEFT = "a"
LEFT_STICK_RIGHT = "d"

# Gamepad Buttons (A B X Y):
GAMEPAD_A = "space"
GAMEPAD_B = "left shift"
GAMEPAD_X = "r"
GAMEPAD_Y = "1"

# Gamepad Shoulders:
LEFT_SHOULDER = "q"
RIGHT_SHOULDER = "e"

# Menu Buttons:
START = "p"
BACK = "o"

# Thumbstick Buttons:
LEFT_THUMB = "k"
RIGHT_THUMB = "l"

# DPAD Buttons
DPAD_UP = "up"
DPAD_DOWN = "down"
DPAD_LEFT = "left"
DPAD_RIGHT = "right"

gamepad = vg.VX360Gamepad()
print("Press CTRL + SHIFT + ALT + Z to stop the script")

def calculate_left_stick_value():

    xaxis = 0.0
    yaxis = 0.0

    if keyboard.is_pressed(LEFT_STICK_UP):
        yaxis = 1.0
    if keyboard.is_pressed(LEFT_STICK_LEFT):
        xaxis = -1.0
    if keyboard.is_pressed(LEFT_STICK_DOWN):
        yaxis = -1.0
    if keyboard.is_pressed(LEFT_STICK_RIGHT):
        xaxis = 1.0
    
    # print(str(xaxis) + " " + str(yaxis))
    gamepad.left_joystick_float(xaxis,yaxis)

def check_for_triggers():
    
    if mouse.is_pressed("left"):
        gamepad.right_trigger_float(1)
    else:
        gamepad.right_trigger_float(0)

    if mouse.is_pressed("right"):
        gamepad.left_trigger_float(1)
    else:
        gamepad.left_trigger_float(0)

def check_for_buttons():

    # X Y A B Buttons

    if keyboard.is_pressed(GAMEPAD_A):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    if keyboard.is_pressed(GAMEPAD_B):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    if keyboard.is_pressed(GAMEPAD_X):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    if keyboard.is_pressed(GAMEPAD_Y):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)


    # Shoulder Buttons

    if keyboard.is_pressed(RIGHT_SHOULDER):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

    if keyboard.is_pressed(LEFT_SHOULDER):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)


    # Menu Buttons

    if keyboard.is_pressed(START):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

    if keyboard.is_pressed(BACK):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

    #Thumb Buttons

    if keyboard.is_pressed(LEFT_THUMB):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

    if keyboard.is_pressed(RIGHT_THUMB):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

    # Dpad Buttons

    if keyboard.is_pressed(DPAD_UP):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

    if keyboard.is_pressed(DPAD_DOWN):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    
    if keyboard.is_pressed(DPAD_LEFT):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

    if keyboard.is_pressed(DPAD_RIGHT):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)


runing = True
while runing:

    calculate_left_stick_value()
    check_for_triggers()
    check_for_buttons()
    gamepad.update()

    if keyboard.is_pressed("ctrl+shift+alt+z"):
        runing = False
        print("Stopping script")
