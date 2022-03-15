import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio
import supervisor


class button:
    def __init__(self, pin, keycode):
        self.keycode = keycode
        self.lastpressed = False
        self.btn = digitalio.DigitalInOut(pin)
        self.btn.direction = digitalio.Direction.INPUT
        self.btn.pull = digitalio.Pull.DOWN

    def update(self):
        if not self.lastpressed and self.btn.value:
            keyboard.send(self.keycode)
        self.lastpressed = self.btn.value


class switch:
    def __init__(self, pin, keycode):
        self.keycode = keycode
        self.switch = digitalio.DigitalInOut(pin)
        self.switch.direction = digitalio.Direction.INPUT
        self.switch.pull = digitalio.Pull.DOWN

    def update(self):
        keyboard.send(self.keycode)


keyboard = Keyboard(usb_hid.devices)

supervisor.disable_autoreload()


buttons = [
    button(board.GP10, Keycode.KEYPAD_ONE),
    button(board.GP11, Keycode.KEYPAD_TWO),
    button(board.GP12, Keycode.KEYPAD_THREE),
    button(board.GP19, Keycode.KEYPAD_FOUR),
    button(board.GP20, Keycode.KEYPAD_FIVE),
    button(board.GP21, Keycode.KEYPAD_SIX),
]

switches = []

while True:
    for b in buttons:
        b.update()
    # for s in switches:
    #    s.update()
    time.sleep(0.001)
