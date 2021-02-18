# font

## Prepare
+ 安装fontforge, fontforge自带python环境(ffpython)，可以将ffpython.exe所在的目录位置加到PATH中，也可以使用fontforge自带的FontForge interactive console直接使用ffpython命令
+ 安装Python环境，另需第三方库cv，numpy，hashlib等等

```
pip install opencv-python
pip install numpy
pip install hashlib
```

## Steps
+ ./export.py用于把fz.ttf中的所有字的.bmp图片导入到./fz_bmp文件夹中
+ ./fontProcessing.py对./fz_bmp下的所有.bmp文件按照算法处理后图片导入到./fz_out文件夹下(./imgFunctions.py封装函数)
+ ./bmp2svg.py使用./potrace/potrace.exe工具把./fz_out下的所有.bmp文件转换为.svg格式放到./fz_svg文件夹下
+ ./import.py根据./fz_svg下的所有图片创造新的字体

## Usage

    ffpython export.py        
    python fontProcessing.py
    python bmp2svg.py
    ffpython import.py

## P.S.

+ Thanks to Dai dalao's algorithm (./introduction.txt里讲解了代大佬处理字形的想法)
+ 用户的邮箱信息在fontProcessing.py line6, 这里会有更改
+ ./potrace下的potrace.exe用于把.bmp文件转换为.svg文件 (fontforge.glyph.importOutlines()函数只能导入矢量图片)
