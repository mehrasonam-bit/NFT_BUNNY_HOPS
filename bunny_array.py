# module imports
import random
import numpy as np

# universal colors
bg = (255, 255, 255)  # color 'white'
ln = (0, 0, 0)        # color 'black'
tg = (255, 0, 127)    # color 'red' variant

# Random face color applying to the arrays. 
rf = random.randint(50, 255)
gf = random.randint(50, 255)
bf = random.randint(50, 255)
face_random = [rf, gf, bf]
ce = face_random

# Random body color based on RGB value range
rb = random.randint(0, 255)
gb = random.randint(0, 255)
bb = random.randint(0, 255)
body_random = [rb, gb, bb]
dy = body_random

# value array where bunny are drawn with pixel value

# sassy bunny array
sassy_bun = np.array([
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	dy,	ce,	ce,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	bg,	bg,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	dy,	ce,	bg,	tg,	tg,	tg,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	tg,	tg,	tg,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	tg,	tg,	ln,	tg,	tg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	tg,	tg,	tg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	tg,	tg,	tg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	bg, bg, ce,	ce,	ce,	bg, bg, ce, bg, bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	bg, ln,	ce,	ce,	ce,	ln,	bg, ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	dy,	ce,	tg,	tg,	tg,	ce,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	dy,	dy,	dy,	dy,	dy,	dy,	tg,	dy,	dy,	dy,	dy,	dy,	dy,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	dy,	dy,	dy,	dy,	ln,	dy,	dy,	dy,	ln,	dy,	dy,	dy,	dy,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	dy,	dy,	dy,	dy,	ln,	ln,	ln,	dy,	dy,	dy,	dy,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg]])

# cute bunny array table
cute_bun =np.array([
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	ce,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	ce,	ce,	dy,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ln,	ce,	ce,	ce,	ln,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	tg,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	ce,	dy,	ce,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	bg,	ce,	dy,	ce,	bg,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	ce,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg]])

#pirate Bunny

eyepatch_bun=np.array([
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	ce,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	ce,	ce,	dy,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ln,	ln,	ln,	ln,	ln,	ln,	ln,	ln,	ln,	ln,	ln,	ln,	ln,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ln,	ln,	ln,	ln,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ln,	ln,	ln,	ln,	ce,	ce,	ce,	ln,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ln,	ln,	ce,	ce,	tg,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	ce,	dy,	ce,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	bg,	ce,	dy,	ce,	bg,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	ce,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
])        

# basic bunny array 
basic_bun = np.array([
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ln,ln,ln,bg,ln,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ln,ln,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,dy,dy,ce,ln,dy,ce,dy,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,dy,dy,dy,ce,ln,dy,ce,dy,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,dy,dy,dy,dy,ce,ln,dy,ce,dy,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,dy,dy,dy,dy,ce,ln,dy,ce,dy,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,dy,dy,dy,ce,ln,ce,dy,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,dy,dy,ce,ce,ln,ce,dy,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ln,ln,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg],[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ln,ln,ln,ln,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ln,ce,ce,dy,dy,ln,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,dy,dy,ln,ce,ce,ce,ce,ce,ce,dy,dy,dy,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,dy,dy,ln,ce,ce,ce,ce,ce,ce,dy,bg,bg,dy,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,dy,dy,ln,ce,ce,ce,ce,ce,ce,dy,bg,ln,dy,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,dy,dy,ln,ce,ce,ce,ce,ce,ce,ce,dy,dy,ce,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,tg,tg,ce,ln,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,tg,tg,ln,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,dy,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,dy,ln,ln,ce,ce,ce,ce,ce,ce,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,dy,dy,dy,ln,ln,ln,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,dy,dy,dy,dy,dy,dy,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,dy,dy,dy,ln,ln,dy,dy,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,dy,dy,dy,dy,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,ln,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,dy,dy,dy,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ln,ln,ln,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,dy,dy,dy,ce,ce,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ln,ln,ln,ln,ln,ln,ln,ln,ln,ln,ln,ln,ln,ln,ln,ln,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
[bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg]])

#mask Bunny
mask_bun=np.array([
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	ce,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	ce,	ce,	dy,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ln,	ce,	ce,	ce,	ln,	ce,	ce,	ce,	bg,	bg,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	ce,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	dy,	ce,	ce,	dy,	dy,	dy,	dy,	dy,	ce,	ce,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	dy,	ce,	dy,	dy,	dy,	dy,	dy,	ce,	dy,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	dy,	dy,	dy,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	ce,	dy,	ce,	bg,	bg,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	bg,	ce,	dy,	ce,	bg,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	ce,	dy,	dy,	ce,	ce,	ce,	ce,	ce,	dy,	dy,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	ce,	ce,	ce,	ce,	bg,	ce,	ce,	ce,	ce,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg],
[bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg,	bg]
])
# this file is pulled into the main file where the body type is rolled and different bunnies are generated