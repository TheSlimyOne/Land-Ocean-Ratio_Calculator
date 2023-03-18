import cv2
import math

# Make sure to put the image in the Maps Folder
img = cv2.imread("Maps\\" + input("Enter the name of the file (make sure the file is in the Maps folder): "), 0)

rows, cols = img.shape
img_size = rows * cols

land_pixels = cv2.countNonZero(img) # Counts all pixels that are not black
ocean_pixels = img_size - land_pixels

print(f"Image size is {rows}px x {cols}px or {img_size}px")
print(f"There are {land_pixels} pixels of land, {ocean_pixels} pixels of ocean")
print(f"This map is comprised of {round(ocean_pixels/img_size * 100, 2)}% Ocean")