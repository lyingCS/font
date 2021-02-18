import os
from fontforge import *

oldFont = open('./fz.ttf')
newFont=font()

for glyph in oldFont:
    if oldFont[glyph].isWorthOutputting():
    	newGlyph=newFont.createChar(oldFont[glyph].unicode,oldFont[glyph].glyphname)
    	newGlyph.importOutlines("./fz_svg/"+str(oldFont[glyph].unicode)+"_"+oldFont[glyph].glyphname+".svg")
    	newGlyph.width=oldFont[glyph].width
newFont.familyname="DaiJinXiang"
newFont.fullname="DaiJinXiang"
newFont.generate("out.ttf")
