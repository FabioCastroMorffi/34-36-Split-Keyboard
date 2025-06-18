# main.py

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB, AnimationModes

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())



# Pin configuration
keyboard.row_pins = (board.GPIO8, board.GPIO9, board.GPIO10)
keyboard.col_pins = (board.GPIO2, board.GPIO3, board.GPIO4, board.GPIO5, board.GPIO6, board.GPIO7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Using drive names (MGSPL, MGSPR) to recognize sides; use split_side arg if you're not doing it
split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
#split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

_______ = KC.TRNS
XXXXXXX = KC.NO
FnKey = KC.MO(1)

keyboard.keymap = [
    # Layer 0
    [
        KC.ESC,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,
        KC.Y,     KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC,

        KC.TAB,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,
        KC.H,     KC.J,    KC.K,    KC.L,    KC.SCLN, KC.ENT,

        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,
        KC.N,     KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT
    ],

    # Layer 1
    [
        KC.GRV,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,
        KC.F6,    KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.DEL,

        _______,  KC.F11,  KC.F12,  XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,

        _______,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, _______
    ]
]

if __name__ == '__main__':
    keyboard.go()
