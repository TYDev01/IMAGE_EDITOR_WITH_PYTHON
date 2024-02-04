from PIL import Image, ImageEnhance, ImageFilter
import os


# os.mkdir('img')
# os.mkdir('editedImg')
in_paths = './img'
out_path = './editedImg'

for filename in os.listdir(in_paths):
    img = Image.open(f"{in_paths}/{filename}")
