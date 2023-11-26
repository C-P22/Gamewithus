from PIL import Image, ImageDraw
import math
import random
import os  # Import the os module for directory operations

from config import *
# Create a new image with a white background
class Light():
    def __init__(self, ON, RANGE,count):
        self.ON = ON
        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.range = RANGE
        self.count = count
        self.create_image()
        

    def create_image(self):
        img = Image.new("RGBA", (self.width, self.height), color=(255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        # Image size and center coordinates
        width, height = img.size
        center_x, center_y = width // 2, height // 2

        farthest_point = self.range
        # Iterate through each pixel in the image
        for x in range(width):
            for y in range(height):
                # Calculate the distance from the center
                distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)

                # If the distance is greater than the threshold, set the pixel to black with transparency
                probatility = distance / farthest_point
                random_number = random.random()
                if probatility > random_number:
                    draw.point((x, y), fill=(0, 0, 0, 255))
        self.img = img
        self.save_imgae(f'Code/img/light/{self.count}.png')
    def save_imgae(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        self.img.save(filename)
for i in range(10):
    lin = f"i"
    print(i,lin)
    lin = Light(True,LIGHT_RANGE,i)
#light.img.show()