#批量转换png至jpg
import os
from PIL import Image
dirname_read="JPEF Images/"
dirname_write="new JPEF Images/"
if os.path.exists(dirname_write) ==False:
    os.mkdir(dirname_write)
names=os.listdir(dirname_read)
count=0
for name in names:
    img=Image.open(dirname_read+name)
    name=name.split(".")
    if name[-1] == "png":
        name[-1] = "jpg"
        name = str.join(".", name)
        r,g,b,a=img.split()
        img=Image.merge("RGB",(r,g,b))
        to_save_path = dirname_write + name
        img.save(to_save_path)
        count+=1
        print(to_save_path, "------conut：",count)
    else:
        continue

