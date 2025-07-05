import board
import displayio
import terminalio
import busio

from kb import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType

from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

keyboard = KMKKeyboard()

# Pins
keyboard.col_pins = (board.GPIO12, board.board.GPIO11, board.GPIO10, board.GPIO9, board.GPIO8, board.GPIO7)
keyboard.row_pins = (board.GPIO6, board.GPIO5, board.GPIO4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#Oled for text display

displayio.release_displays()
i2c = busio.I2C(board.GPIO1, board.GPIO2)  # might reverse SDA and SCL if incorrect

display = SSD1306_I2C(38, 12, i2c)
splash = displayio.Group()

text_area = label.Label(terminalio.FONT, text="RAW SPLIT", x=2, y=10)
splash.append(text_area)
display.show(splash)


# Split Side
split_side = SplitSide.LEFT #RIGHT


split = Split(split_type=SplitType.UART, split_side=split_side)

layers = Layers()

keyboard.modules = [layers, split]

# Key's reassignment

_______ = KC.TRNS



LOWER = KC.MO(2)
RAISE = KC.MO(1)


# fmt:off
keyboard.keymap = [
    [  #QWERTY
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH,
                                    KC.LCTL,   LOWER,  KC.SPC,     KC.BSPC,    RAISE,  KC.ENT,
    ],
    [  #RAISE
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                        KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.TAB,  KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,                      KC.NO, KC.MINS, KC.EQL,  KC.LBRC, KC.RBRC,
        KC.LCTL, KC.GRV,  KC.LGUI, KC.LALT, KC.NO,                      KC.NO, KC.NO, KC.NO, KC.BSLS, KC.QUOT,
                                    KC.NO, KC.NO, KC.NO,      KC.NO, KC.NO, KC.NO,
    ],
    [  #LOWER
        KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,      KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
        KC.ESC,  KC.NO, KC.NO, KC.NO, KC.NO,      KC.NO, KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR,
        KC.CAPS, KC.TILD, KC.NO, KC.NO, KC.NO,      KC.NO, KC.NO, KC.NO, KC.PIPE,  KC.DQT,
                            KC.NO, KC.NO, KC.NO,      KC.ENT,  KC.NO, KC.DEL
    ]
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
