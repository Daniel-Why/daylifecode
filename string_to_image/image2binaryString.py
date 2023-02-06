from PIL import Image

def image_to_string(image: Image) -> str:
    data = image.getdata()
    data = [1 if p > 127 else 0 for p in data]
    return ''.join(str(d) for d in data)

# Open an image file
image = Image.open('image2.png')

# Convert the image to a string
s = image_to_string(image)
print(s)