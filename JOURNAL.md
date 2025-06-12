---
title: "Magnetic Split"
author: "Fabio"
description: "4x6 Split Keyboard with magnets that can join to become a single unit"
created_at: "2025-06-05"
---
## Total Time: 11h
## June 6th 2025 - Initial idea

I've wanted to build a split keyboard for some time but with an additional twist, something unique to it. After brainstorming a for a little while, I found I wanted an original design that had something to do with magnets (Love magnets!). Watching projects such as this one ![Split Keebs that could be joined](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/78c3c8f0-ee08-11ee-b7f7-2fbf0d57bb96.jpeg)

I thought about a split keyboard that could become a single one with magnets and perhaps trigger something on OLED screens with the use of Hall Effect Sensors(not sure at all about this but we'll see as we progress).

Most of the time today was me thinking about this idea, but I also started doing the schematics of the pcb. I'm thinking of going for a wired build using RP Pico 2040 as the microcontrollers and using TRRS Jack for the communitcation between the two sides. The rest of the components are the 2 OLED screens 0.91, some cheap **CLICKY** switches and the diodes that go with them.

![PCB Schematics](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-06%2023-25-01.png)

### Futur Challenges

- The design of the case to best fit the magnets will probably prove to be difficult(not to talk about type of magnet, shape, etc)
- Using the Hall Effect Sensors to check whether the two halfs are connected is something I'm not even sure at the moment that could work

### <span style="color:green">Time Spent</span>: 5h(Again, today was mostly research)



## June 10th 2025 - Draft PCB layout

Had to take a break but today I'm back on the grind. I downsized the splitkeyboard to have a total of 36 keys rather than 48. The main reason behind this is that I feel the extra keys will make a difference since the intention is to mainly write text with this keyboard. 

![PCB Draft .pcb file](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-10%2022-08-07.png)

Taking ideas from examples online(such as the [Lily58](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/84393842-13960900-ac37-11ea-811e-65db2948ca73.jpg)), I decided to go with the layout where the OLED Screen stands on top of the MCU to help with space management (and cause it also looks cool). This could cause problems if I ever need access to what's covered by the OLED screen but, since I didn't cover the main buttons, I don't think it's something to really worry about. 

### Time Spent: 1 hour (Tomorrow big update for sure!)


## June 11th 2025 - Finished PCB Layout

Today was a 'getting things done session'. I settled on the asymetric design for the split and spent some time working on the size of the PCB as well on the routing (god the routing was insane). I also added the 3d models for all components and some art as well.

![Finished PCB](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-11%2021-23-56.png)

![3d Models and Art](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-11%2022-03-46.png)

Crazy to think that in 1 paragraph I resumed 5 hours of work (rounding down) so here are some of the taks that took a lot of time to get through:

- Changing the 3D model of an existing footprint (with the objective of saving time with the switches) and applying said footprint to all switches at one (ended up having to apply it one by one in schematics)
- Adjusting arc length when doing round lines in EdgeCuts; It is hard for me to believe that using the arc tool is the best way to do this.
- Adding art to my PCB. This one is completely on me. It took me a lot of time to catch that the Bit2MapConverter was already featured in the main menu of KiCad. I spent most of my time looking for inexistent plugin or software to do this until I found it.
- Last but not least, Routing. This one is one everyone can agree in. At the start, the space between my the edge of my PCBs and the components was too small so I couldn't get around with a track. Had to change the lines in EdgeCuts twice before finishing routing.

### Time Spent: 5 hours (Starting Designs on CAD Tomorrowww)

