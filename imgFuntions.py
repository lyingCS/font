BLACK = 100
WHITE = 200
def getStraightEdge(_raw, _col,direction,CheckArray,imgarray):
	startPoint = [_raw,_col]
	if direction == 'up':
		_col += 1
		while WhiteEdge(_raw,_col,CheckArray,imgarray) == 'up':
			CheckArray[_raw,_col] = 1
			_col += 1
		if _raw - startPoint[0] + _col - startPoint[1] < 3:
			return None
		return startPoint,[_raw,_col - 1]
	if direction == 'down':
		_col += 1
		while WhiteEdge(_raw, _col, CheckArray, imgarray) == 'down':
			CheckArray[_raw, _col] = 1
			_col += 1
		if _raw - startPoint[0] + _col - startPoint[1] < 3:
			return None
		return startPoint, [_raw, _col - 1]
	if direction == 'left':
		_raw += 1
		while WhiteEdge(_raw, _col, CheckArray, imgarray) == 'left':
			CheckArray[_raw, _col] = 1
			_raw += 1
		if _raw - startPoint[0] + _col - startPoint[1] < 3:
			return None
		return startPoint, [_raw - 1, _col]
	if direction == 'right':
		_raw += 1
		while WhiteEdge(_raw, _col, CheckArray, imgarray) == 'right':
			CheckArray[_raw, _col] = 1
			_raw += 1
		if _raw - startPoint[0] + _col - startPoint[1] < 3:
			return None
		return startPoint, [_raw - 1, _col]
	return None

#返回这个像素是否是只有一条白边，有就返回该白边方向，无则返回none
def WhiteEdge(_raw,_col,CheckArray,imgarray):
	upval = upDirection(_raw-1,_col,CheckArray,imgarray)
	downval = downDirection(_raw+1,_col,CheckArray,imgarray)
	leftval = leftDirection(_raw,_col-1,CheckArray,imgarray)
	rightval = rightDirection(_raw,_col+1,CheckArray,imgarray)
	if upval+downval+leftval+rightval == 1:
		if upval == 1:
			return 'up'
		if downval == 1:
			return 'down'
		if leftval == 1:
			return 'left'
		if rightval == 1:
			return 'right'
	else:
		return None

def upDirection(_raw,_col,CheckArray,imgarray):
	if _raw < 0 or imgarray[_raw,_col] == 255 and CheckArray[_raw,_col]!=1:
		return 1
	else:
		return 0

def downDirection(_raw, _col,CheckArray,imgarray):
	if _raw >= len(imgarray[:,1]) or imgarray[_raw,_col] == 255 and CheckArray[_raw,_col]!=1:
		return 1
	else:
		return 0

def leftDirection(_raw, _col,CheckArray,imgarray):
	if _col < 0 or imgarray[_raw,_col] == 255 and CheckArray[_raw,_col]!=1:
		return 1
	else:
		return 0

def rightDirection(_raw,_col,CheckArray,imgarray):
	if _col >= len(imgarray[1,:]) or imgarray[_raw,_col] == 255 and CheckArray[_raw,_col]!=1:
		return 1
	else:
		return 0

#todo 斜边或角的查找和修改
def getCorner():
	return 0



def straightEdgeChange(direction,path,keyInfo,keyCount,imgArray,CheckArray):
	keyNumic = eval('0x'+keyInfo[keyCount])
	keyCount = (keyCount + 1)%len(keyInfo)
	offset = keyNumic % 3
	diff = 0
	start = keyNumic + 2 * offset
	if direction == 'up':
		pathLen = path[1][1] - path[0][1]
		if keyNumic < pathLen:
			diff = pathLen - keyNumic - offset
			#向外填充黑色
		if path[0][0] - 1 >= 0:
			lineFill([path[0][0] - 1,path[0][1] + offset],[keyNumic,pathLen-offset],['H',BLACK],imgArray,CheckArray)
		#向内填充白色
		while diff >= 3 and keyNumic < diff - offset:
			[keyNumic, keyCount, keyInfo] = updateKeynumic([keyNumic, keyCount, keyInfo])
			pathLen = diff - offset
			diff = diff - keyNumic - offset
			if keyNumic%2 == 0 and path[0][0] - 1 >= 0:
				lineFill([path[0][0] - 1,path[0][1] + start],[keyNumic,pathLen],['H', BLACK],imgArray,CheckArray)
			elif keyNumic%2 == 1:
				lineFill([path[0][0],path[0][1] + start],[keyNumic,pathLen],['H',WHITE],imgArray,CheckArray)
			if keyNumic != 0:
				start = keyNumic + offset + start
	if direction == 'down':
		pathLen = path[1][1] - path[0][1]
		if keyNumic < pathLen:
			diff = pathLen - keyNumic - offset
			#向外填充黑色
		if path[0][0] + 1  < len(imgArray[:,1]):
			lineFill([path[0][0] + 1, path[0][1] + offset], [keyNumic, pathLen-offset], ['H', BLACK], imgArray, CheckArray)
		while diff >= 3 and keyNumic < diff - offset:
			[keyNumic, keyCount, keyInfo] = updateKeynumic([keyNumic, keyCount, keyInfo])
			pathLen = diff - offset
			diff = diff - keyNumic - offset
			if keyNumic%2 == 0 and path[0][0] + 1  < len(imgArray[:,1]):
				lineFill([path[0][0] + 1,path[0][1] + start],[keyNumic,pathLen],['H', BLACK],imgArray,CheckArray)
			elif keyNumic%2 == 1:
				lineFill([path[0][0],path[0][1] + start],[keyNumic,pathLen],['H', WHITE],imgArray,CheckArray)
			if keyNumic != 0:
				start = keyNumic + offset + start
	if direction == 'left':
		pathLen = path[1][0] - path[0][0]
		if keyNumic < pathLen:
			diff = pathLen - keyNumic - offset
			#向外填充黑色
		if path[0][1] - 1 >= 0:
			lineFill([path[0][0] + offset, path[0][1] - 1], [keyNumic, pathLen-offset], ['V', BLACK], imgArray, CheckArray)
		while diff >= 3 and keyNumic < diff - offset:
			[keyNumic, keyCount, keyInfo] = updateKeynumic([keyNumic, keyCount, keyInfo])
			pathLen = diff - offset
			diff = diff - keyNumic - offset
			if keyNumic%2 == 0 and path[0][1] - 1 >= 0:
				lineFill([path[0][0]+start ,path[0][1] - 1],[keyNumic,pathLen],['V', BLACK],imgArray,CheckArray)
			elif keyNumic%2 == 1:
				lineFill([path[0][0]+start ,path[0][1]],[keyNumic,pathLen],['V', WHITE],imgArray,CheckArray)
			if keyNumic != 0:
				start = keyNumic + offset + start
	if direction == 'right':
		pathLen = path[1][0] - path[0][0]
		if keyNumic < pathLen:
			diff = pathLen - keyNumic - offset
			#向外填充黑色
		if path[0][1] + 1 < len(imgArray[1,:]):
			lineFill([path[0][0] + offset, path[0][1] + 1], [keyNumic, pathLen-offset], ['V', BLACK], imgArray, CheckArray)
		while diff >= 3 and keyNumic < diff - offset:
			[keyNumic, keyCount, keyInfo] = updateKeynumic([keyNumic, keyCount, keyInfo])
			pathLen = diff - offset
			diff = diff - keyNumic - offset
			if keyNumic % 2 == 0 and path[0][1] + 1 < len(imgArray[1,:]):
				lineFill([path[0][0] + start, path[0][1] + 1], [keyNumic, pathLen], ['V', BLACK], imgArray, CheckArray)
			elif keyNumic % 2 == 1:
				lineFill([path[0][0] + start, path[0][1]], [keyNumic, pathLen], ['V', WHITE], imgArray, CheckArray)
			if keyNumic != 0:
				start = keyNumic + offset + start
	[keyNumic, keyCount, keyInfo] = updateKeynumic([keyNumic, keyCount, keyInfo])
	return keyCount

#填充
def lineFill(startPoint,len,type,imgArray,CheckArray):
	for i in range(len[0]):
		if i >= len[1]:
			break
		if type[0] == 'H':#水平
			if startPoint[0] == 102:
				print('error,102')
			imgArray[startPoint[0],startPoint[1]+i] = type[1]
			CheckArray[startPoint[0],startPoint[1]+i] = 1
		if type[0] == 'V':#垂直
			imgArray[startPoint[0]+i,startPoint[1]] = type[1]
			CheckArray[startPoint[0]+i,startPoint[1]] = 1

def updateKeynumic(key):
	key[0] = eval('0x' + key[2][key[1]])
	key[1] = (key[1] + 1) % len(key[2])
	return key