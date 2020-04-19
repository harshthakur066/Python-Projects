from PIL import Image, ImageFilter

img = Image.open('./Pokemons/pikachu.jpg')
filterd_img = img.filter(ImageFilter.SHARPEN).crop((100, 100, 400, 400))
filterd_img.save('./Edit/pickachu.png', 'png')
filterd_img_2 = img.convert('L').resize((200, 200))
filterd_img_2.save('./Edit/pickachu_bw.png', 'png')
crooked = img.rotate(180)
crooked.save('./Edit/upside_down.png', 'png')
print(img)
