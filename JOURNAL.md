---
title: "Raw Split"
author: "Fabio"
description: "36 Key Split Keyboard with three layers of PCB"
created_at: "2025-06-05"
---
[Jump to Current Design](#july-4th-2025---big-change)
## Total Time: 25h
## June 6th 2025 - Initial idea

I've wanted to build a split keyboard for some time but with an additional twist, something (slightly) unique to it. After brainstorming a for a little while, I found I wanted an original design that had something to do with magnets (Love magnets!). Watching projects such as this one ![Split Keebs that could be joined](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/78c3c8f0-ee08-11ee-b7f7-2fbf0d57bb96.jpeg)

I thought about a split keyboard that could become a single one with magnets and perhaps trigger something on OLED screens with the use of Hall Effect Sensors(not sure at all about this but we'll see as we progress).

Most of the time today was me thinking about this idea, but I also started doing the schematics of the pcb. I'm thinking of going for a wired build using RP Pico 2040 as the microcontrollers and using TRRS Jack for the communitcation between the two sides. The rest of the components are the 2 OLED screens 0.91, some cheap **CLICKY** switches and the diodes that go with them.

![PCB Schematics](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-06%2023-25-01.png)

### Futur Challenges

- The design of the case to best fit the magnets will probably prove to be difficult(not to talk about type of magnet, shape, etc)
- Using the Hall Effect Sensors to check whether the two halfs are connected is something I'm not even sure at the moment that could work

### <span style="color:green">Time Spent</span>: 5h(Again, today was mostly research)



## June 10th 2025 - Draft PCB layout

Had to take a break but today I'm back on the grind. I downsized the splitkeyboard to have a total of 36 keys rather than 48. The main reason behind this is that I feel the extra keys wouldn't really make a difference since the intention is to mainly write text with this keyboard. 

![PCB Draft .pcb file](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-10%2022-08-07.png)

Taking ideas from examples online(such as the [Lily58](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/84393842-13960900-ac37-11ea-811e-65db2948ca73.jpg)), I decided to go with the layout where the OLED Screen stands on top of the MCU to help with space management (and cause it also looks cool). This could cause problems if I ever need access to what's covered by the OLED screen but, since I didn't cover the main buttons, I don't think it's something to really worry about. 

### Time Spent: 1 hour (Tomorrow big update for sure!)


## June 11th 2025 - Finished PCB Layout

Today was a 'getting things done session'. I settled on the asymetric design for the split (Hopefully it fits budget, fingers crossed)and spent some time working on the size of the PCB as well on the routing (god the routing was insane). I also added the 3d models for all components and some art as well.

![Finished PCB](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-11%2021-23-56.png)

![3d Models and Art](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-11%2022-03-46.png)

Crazy to think that in 1 paragraph I resumed 5 hours of work (rounding down) so here are some of the taks that took a lot of time to get through:

- Changing the 3D model of an existing footprint (with the objective of saving time with the switches) and applying said footprint to all switches at one (ended up having to apply it one by one in schematics)
- Adjusting arc length when doing round lines in EdgeCuts; It is hard for me to believe that using the arc tool is the best way to do this.
- Adding art to my PCB. This one is completely on me. It took me a lot of time to catch that the Bit2MapConverter was already featured in the main menu of KiCad. I spent most of my time looking for inexistent plugin or software to do this until I found it.
- Last but not least, Routing. This one is one everyone can agree in. At the start, the space between my the edge of my PCBs and the components was too small so I couldn't get around with a track. Had to change the lines in EdgeCuts twice before finishing routing.

### Time Spent: 5 hours (Starting Designs on CAD Tomorrowww)

## June 14th 2025 - The CAD

Finally working on the keebs again!! Today was a rough session cause of Fusion 360. It is infuriating that this software is only available natively in Windows and Mac. Yes, there are some workarounds for Linux users, but I can assure you I tried the main ones and they didnt work at all. So yeah, today I had the long overdue change from the HORRIBLE Fusion 360 browser experience to Onshape. Even though it took me some time to get the hang of it, the transition is not that bad. 

Here are some pictures of the top of my case with the STEP file of my PCB which are the main parts that I worked on today.

![CAD Top case](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-14%2021-32-16.png)

![CAd top with 3d pcb](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-14%2021-33-00.png)

Quite bad right? Keep in my mind it's my second ever hardware project; We all start somewhere. Now on a more serious manner, these are some of the points that I need to improve or start working on for the following session. 

- Holes' alignment. The holes for the jack receptor, the mounting holes and the switches are not perfectly aligned with the pcb (If i've learned something from using KiCad is not 100% trust the exported DXF images cause the measurements are not exact, maybe im doing it wrong)
- The top case has ugly sharp corners. I could use the chamfer tool to improve that part and fillet for like the microusb entrance for the RPs
- Add the holes for the magnets to fit in. Since the keyboards will be pretty light, I believe 10x3 mm cylindrical Neodyum Magnets will do the trick (3 of them in each keyboard)
- Create a bottom case for the keyboard (I'm starting to panic with the amount of plastic for these two splits with the budget)
- Duplicate this with the second one (work on the puzzle feeling between the right one and the left one)

Thinking it through, the magnet is nothing but a gimmick, snake oil, on a project that is actually just a split wired keyboard, but well we've come this far I guess we'll keep going. 

### Time spent: 6 hours 

## June 17th 2025- The CAD (Part 2)

I spent the last three days both fixing( and breaking) stuff; in fact, the reason I didn't separate today's journal into two parts is because I was furious yesterday thinking I had lost some very important changes. This is a great opportunity to say: 'God bless **Version Control**'. Due to an involontary change I made that I only caught later on, I had to restore my build to a much older version. This unfortunately implied I had to lose some of the progress I had made (or not??, if theres a way, I didnt find it) in order to fix that error (still better than having to fix all of it). This made me lose some time, but, in retrospective, it was a great learning experience.

## Main improvements:

- [x] Holes are alligned.
- [x] Used chamfer and fillet on some edges to diminish sharp, ugly corners.
- [x] Added a male/female receptacles as well as the magnets holes (4 Neodyum Magnets will be used with dimensions 5x2mm, due to the small weight of the case it should be enough).
- [x] Created the bottom case for the keyboard.
- [x] Made the right half(mainly with the mirroring tool).

![Joining CAD splits](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-17%2018-49-36.png)

![With 3d PCB](https://github.com/FabioCastroMorffi/Magnetic-Split/blob/main/assets/Screenshot%20from%202025-06-17%2018-48-53.png)

## What's missing?

- Finishing GitHub (uploading files, updating README and BOM, etc)
- Make post on #highway-pitstop and complete form
- Maybe have to change it because its not complex enough, maybe(I think its the 3d design is not that bad)

### Time Spent: 8 hours (Getting ready to ship tomorrowww)


## July 4th 2025 - Big Change

After a long break, I went and took a look at were I left the project a couple of weeks ago and I was .... disappointed with how it turned out. The top of the 3D model had to be changed because it wasn't printable, the design looked bland and the key layout didn't appear as appealing as the first day. What did I do to improve that? I spent the last three days redesigning everything (basically started a new project) and I told myself I would attempt not to use 3D modeling because of how **miserable** 3D modeling felt (manually changing the svg files, once imported, because measurements were off was an aboslute nightmare).

But here we are! with a design a kinda like were I basically replaced the 3d printed top and bottom for PCB plates which gives it more of a raw appearance.

## PCBs

PCBs for the top, bottom as well as the center of the Split Keyboard 

![]()
![]()
![]()

## Assembled 3D Model (imported everything into Onshape)
### Overview

![]()

### Side View

For the 3 plates to be connected, I'll use 8 standoffs(4x M2 3mm and 4x M2 6mm). The small ones are for connecting the top and the center and the big ones are for connecting the bottom and the center. In addition, the M2 screws I'll use are 4 M2 10mm and 4 M2 4mm.

![]()






