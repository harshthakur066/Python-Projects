from PIL import Image

img = Image.open('astro.jpg')
img.thumbnail((400, 400))
img.save('astro.jpg')
print(img.size)
