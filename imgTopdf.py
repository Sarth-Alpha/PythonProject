import os
from PIL import Image

output_in = './pdf'
source_is = './images'

for file in os.listdir(source_is):
    if file.split('.')[-1] in ('png','jpg','jpeg'):
        image = Image.open(os.path.join(source_is,file))
        image_converted = image.convert('RGB')
        image_converted.save(os.path.join(output_in,'{0}.pdf'.format(file.split('.')[-2])))