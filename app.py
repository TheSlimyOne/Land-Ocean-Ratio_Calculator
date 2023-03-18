import cv2
import math

def calculate(ocean=True):
    try:
        img = cv2.imread(input("\nEnter the path to the file: "), 0)
        rows, cols = img.shape
    except Exception:
        print("\n--- Image was invalid ---\n")
        return
    
    img_size = rows * cols

    land_pixels = cv2.countNonZero(img) # Counts all pixels that are not black
    ocean_pixels = img_size - land_pixels

    print(f"Image size is {rows}px x {cols}px or {img_size}px")
    print(f"There are {land_pixels} pixels of land, {ocean_pixels} pixels of ocean")

    dividend = ocean_pixels if ocean else land_pixels
    name = "Ocean" if ocean else "Land"

    print(f"This map is comprised of {round(dividend/img_size * 100, 2)}% {name}")

if __name__ == "__main__":
    while True:
        print("-----------------------------")
        print("1. Calculate ocean percentage")
        print("2. Calculate land percentage")
        print("3. Quit")
        print("-----------------------------")
        selection = input("Choose a number: ")


        if selection == "1":
            calculate()
        elif selection == "2":
            calculate(False)
        elif selection == "3":
            exit()
        else:
            print("invalid input try again!")