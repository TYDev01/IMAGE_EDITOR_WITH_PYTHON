from PIL import Image, ImageEnhance, ImageFilter
import os


# os.mkdir('img')
# os.mkdir('editedImg')
in_paths = './img'
out_path = './editedImg'

for filename in os.listdir(in_paths):
    img = Image.open(f"{in_paths}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert("L")
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{out_path}/{clean_name}_edited.jpg")
