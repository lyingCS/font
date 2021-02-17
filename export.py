import os
from fontforge import *

# font = open(os.sys.argv[1])
font = open('./fz.ttf')
for glyph in font:
    if font[glyph].isWorthOutputting():
    	font[glyph].export("./fz_bmp/"+str(font[glyph].unicode)+"_"+font[glyph].glyphname + ".bmp")