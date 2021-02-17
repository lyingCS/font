#conding=utf8  
import os 
from fontforge import *

g = os.walk("./fz_svg")  
font=font()

for path,dir_list,file_list in g:  
    for file_name in file_list:  
    	print(file_name)
    	[ucd,name]=file_name[:-4].split('_')
    	glyph=font.createChar(int(ucd),name)
    	glyph.importOutlines("./fz_svg/"+file_name)

font.generate("output.ttf")
