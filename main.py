from PIL import Image, ImageEnhance, ImageFilter
import os


path = './img'
pathOut = './output'

for filename in os.listdir(path):
	img = Image.open(f"{path}/{filename}")
	edit = img.filter(ImageFilter.SHARPEN).convert('L')
	enhancer = ImageEnhance.Contrast(edit)
	edit = enhancer.enhance(1.5)
	print(f"Editing {filename}")
	clean_name = os.path.splitext(filename)[0]
	print(f"Cleaned name is {clean_name}")
	edit.save(f"{pathOut}/{clean_name}_edited.jpg")
