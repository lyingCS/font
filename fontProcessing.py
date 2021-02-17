import os
import cv2 as cv
import numpy as npy
import hashlib
import imgFuntions
keystr =b'540330016@qq.com'
key_md5 = hashlib.md5(keystr)
key_md5_str = str(key_md5.hexdigest())

def main():
	g = os.walk("./fz_bmp")  
	for path,dir_list,file_list in g:
		for file_name in file_list:
			img = cv.imread("./fz_bmp/"+file_name, 0)
			imgarray = img // 255
			imgarray = imgarray *255
			CheckArray = npy.zeros((len(imgarray[:,1]),len(imgarray[1,:])))
			moveCount = 0
			# print(len(imgarray[:,1]),len(imgarray[1,:]))
			print(file_name)
			for raw in range(len(imgarray[:,1])):
				for col in range(len(imgarray[1,:])):
					if imgarray[raw,col] != 255 and CheckArray[raw,col] != 1:
						CheckArray[raw,col] = 1
						direction = imgFuntions.WhiteEdge(raw,col,CheckArray,imgarray)
						path = imgFuntions.getStraightEdge(raw,col,direction,CheckArray,imgarray)
						if (direction != None and path != None):
							imgFuntions.straightEdgeChange(direction,path,key_md5_str,moveCount,imgarray,CheckArray)
							if moveCount+1 < len(key_md5_str):
								moveCount += 1
			cv.imwrite("./fz_out/"+file_name,imgarray)

main()






