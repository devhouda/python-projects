#15
from PIL import Image

def resize_image(dim1, dim2):

    image = Image.open("image_with_face.jpg")

    print(f"Current size: {image.size}")

    resized_image = image.resize((dim1, dim2))

    resized_image.save("image_with_face_resized.jpg")

dim1 = int(input("Enter width: "))
dim2 = int(input("Enter height: "))

resize_image(dim1, dim2)
print("Image Resized.")