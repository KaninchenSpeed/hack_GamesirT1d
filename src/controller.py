import vgamepad as vg
from T1D import T1D

gamepad = vg.VX360Gamepad()

controller = T1D('C6:86:A1:01:B7:90')

def map_joystick(val):
    scaled = val * 2 / 1023
    return scaled - 1

def set_btn(btn, state):
    if state:
        gamepad.press_button(button=btn)
    else:
        gamepad.release_button(button=btn)

print('running')
while True:
    if controller.get_state():
        print(controller)

        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, controller.A)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_B, controller.B)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_X, controller.X)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y, controller.Y)

        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP, controller.Up)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN, controller.Down)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT, controller.Left)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT, controller.Right)

        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK, controller.C1)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_START, controller.C2)
        # set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE, controller.MENU)

        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER, controller.L1)
        set_btn(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER, controller.R1)

        gamepad.left_trigger(controller.L2)
        gamepad.right_trigger(controller.R2)

        gamepad.left_joystick_float(map_joystick(controller.LX), map_joystick(controller.LY))
        gamepad.right_joystick_float(map_joystick(controller.RX), map_joystick(controller.RY))

        gamepad.update()