# Raw Split
## Overview

Raw Split is a wired 36 key split keyboard made with 3 PCB layers and powered by an RP pico 2040 on each side. I'm using the Miryoku ZMK as the layout and  I decided to go for a smaller split keyboard for two main reasons: I want it to be portable, mainly so I can use it in class, and I wanted to be under (or very close to) the 50$ mark.


## Motivation
After finishing my design for Hackpad, which was an introduction to PCB Design and 3D modelling, I was confident I could go build a bigger project in a more efficient manner but I was completely wrong. I got sent to the Valley of Stupidity earlier than expected. 

I had an initial idea with a Split Keyboard that would have magnetic sides but I wasn't proud of the design I came up with (and it wasnt printable) so I decided to scrap it up and do it again with a different idea. The change was mainly on the fact that I abhorred 3D modelling of the top/side and bottom so on the Raw Split I decided to only use PCBs for the full design; the raw aesthetic of the build is where the name comes from -- I'm not very creative with names.

## PCBs

### Center

![Center](https://github.com/FabioCastroMorffi/Raw-Split/blob/main/assets/Screenshot%20from%202025-07-04%2020-38-26.png)
![3d center](https://github.com/FabioCastroMorffi/Raw-Split/blob/main/assets/Screenshot%20from%202025-07-04%2020-37-54.png)

### Top
![Top](https://github.com/FabioCastroMorffi/Raw-Split/blob/main/assets/Screenshot%20from%202025-07-04%2020-39-09.png)


### Bottom

![Bottom](https://github.com/FabioCastroMorffi/Raw-Split/blob/main/assets/Screenshot%20from%202025-07-04%2020-36-35.png)

## CAD
[Direct link on Onshape](https://cad.onshape.com/documents/60adbd5316aad71d4d3bcb16/w/73c77201f5fbc04cf68d7350/e/32bb371216fb4a7634cbbee2?renderMode=0&uiState=686715ac173d9866c8e98733)

Thank you Onshape for being so easy to work with (shame on the horrible experience that is Fusion360's online services for students). I really need to emphasize how much better OnShape is on web, because the initial horrible experience I had with Fusion Online or trying to install a Linux version of Fusion was horrible and made me waste a lot of time. 

Here's the overview of the right split:

![Overview](https://github.com/FabioCastroMorffi/Raw-Split/blob/main/assets/Screenshot%20from%202025-07-04%2020-41-31.png)

![Side View](https://github.com/FabioCastroMorffi/Raw-Split/blob/main/assets/Screenshot%20from%202025-07-04%2020-40-52.png)

The total height of the keyboard will be 24.8 mm. The three PCBs measure 1.6 mm in height, the small standoff will have a height of 4 mm while the big one will have a size 6 mm. Finally the height from the top plate to the top of the keycap is approximally 10 mm. 


## BOM

| Quantity | Item                                 | Price (CAD) | Vendor         | Link                                                                 |
|----------|--------------------------------------|-------------|----------------|----------------------------------------------------------------------|
| 2        | RP Pico 2040 Green with Pin          | 6.42        | Aliexpress     | [Link](https://shorturl.at/I2swX)       |
| 1        | 40 PCS kailh box V2 (linear switches)| 1.38(with welcome deal)      | Aliexpress     | [Link](https://www.aliexpress.com/item/1005005704076690.html) |                                                  
| 1        | 100 PCS Through Hole Diodes (1N4148) | 2.80        | Aliexpress     | [Link](https://shorturl.at/UQSGh)     |
| 2        | 0.91 Inch 128x32 Oled Display        | 5.00        | Aliexpress     | [Link](https://www.aliexpress.com/item/32709141534.html)            |
| 2        | 20 pcs Blank DSA Keycaps             | 12.5        | Aliexpress     | [link](https://shorturl.at/4GHxS)                                   |
| 1        | 10 PCS PJ-320A Jack Receptacle       | 1.58        | Aliexpress     | [Link](https://www.aliexpress.com/item/1005004960903273.html)       |
| 1        | 20 pcs SW-Push 6x6x4.3mm             | 0.26        | Aliexpress     | [Link](https://shorturl.at/fNnse) |
| 1        | 50 pcs Brass Female to Female Standoffs M2x3mm | 2.72        | Aliexpress     | [Link](https://shorturl.at/DMM1S)|
| 1        | 50 pcs Nylon Female to Female Standoffs M2x6mm | 1.28        | Aliexpress     | [Link](https://shorturl.at/DEXHc)
| 2        | 50 pcs M2 5mm and M2 10 mm           | 4.5         | Aliexpress | [Link](https://shorturl.at/Y6ADS) |
| 1        | Antislip Circular Pads 2mm           | 2.97        | Aliexpress | [Link](https://shorturl.at/uavc9)
| 1        | PCB Manufacturing Center             | 13.04  (without coupon)     | JLCPCB         | 
| 1        | PCB Manufacturing Top                | 12.64  (without coupon)     | JLCPCB         |
| 1        | PCB Manufacturing Bottom             | 12.50  (without coupon)     | JLCPCB         |

|Total (CAD, after taxes and after 20$ JLcPCB Coupon)| Total (USD, after taxes and after 20$ JLcPCB Coupon)|
|---------------|--|
|69|50.69|
