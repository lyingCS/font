# font

thanks to Dai dalao's algorithm
用户的信息在fontProcessing.py里
在fz.ttf字库基础上更改
potrace用于把.bmp文件转换为.svg文件(fontforge.glyph.importOutlines只能导入矢量图片)

## Usage

    //export .bmp files from fz.ttf to ./fz_bmp
    ffpython export.py        
    
    //fontProcessing from ./fz_bmp/*.bmp to ./fz_out/*.bmp
    python fontProcessing.py
    
    //convert from ./fz_out/*.bmp to ./fz_svg/*.svg
    python bmp2svg.py
    
    //import from ./fz_svg/*svg to out.ttf
    ffpython import.py
