from PIL import Image

img = Image.open('photo.jpg')
img = img.resize((200, 200))
img.show()
img.save('resized.jpg')
