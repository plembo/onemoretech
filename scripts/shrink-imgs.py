# Resize all images in a folder
import os
from PIL import Image

HOME = os.environ['HOME']
source = os.path.join(HOME, 'data', 'import')
target = os.path.join(HOME, 'data', 'export')

size = (640, 480)

for f in os.listdir(source):
    if f.endswith('.jpg'):
        print(f)

        fullPath = os.path.join(source, f)
        i = Image.open(fullPath)

        i.resize(size, resample=5)
        i.save(os.path.join(target, f), quality=100)
