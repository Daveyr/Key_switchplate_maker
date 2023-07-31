# From Hackspace magazine 68 Bluechord keyboard, page 73.

import pcbnew
file = "C:\\Users\\rsmil\\Blue Chord\\pcbKeyboard.
KiCad_pcb"
board = pcbnew.LoadBoard(file)
l = []
for f in board.GetFootprints():
b = f.GetBoundingBox()
ref = f.GetReference()
p = f.GetPosition()
px = (p[0] / 1000000.0)
py = (p[1] / 1000000.0)
height = b.GetHeight() / 1000000.0
width = b.GetWidth() / 1000000.0
t = '{0} = ["{0}",{1:.2f},{2:.2f},{3:.2f},{3:
.2f}]'.format(ref,px,py,height,width)
l.append(t)
l.sort()
for t in l:
print(t)