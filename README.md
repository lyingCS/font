# font

## Usage

    //export .bmp files from fz.ttf to ./fz_bmp
    ffpython export.py        
    
    //fontProcessing from ./fz_bmp/*.bmp to ./fz_out/*.bmp
    python fontProcessing.py
    
    //convert from ./fz_out/*.bmp to ./fz_svg/*.svg
    python bmp2svg.py
    
    //import from ./fz_svg/*svg to .ttf
    ffpython import.py
