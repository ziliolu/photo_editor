from PIL import Image, ImageEnhance, ImageFilter 
import os 

path = './imgs'
path_out = '/edited_imgs'

for filename in os.listdir(path): 
    img = Image.open(f"{path}/{filename}")
    edited_img = img.convert("L")
    enhanced_img = ImageEnhance.Contrast(edited_img)
    enhanced_img = enhanced_img.enhance(1)
    clean_name = os.path.splitext(filename)[0]
    enhanced_img.save(f'.{path_out}/{clean_name}_edited.jpg')