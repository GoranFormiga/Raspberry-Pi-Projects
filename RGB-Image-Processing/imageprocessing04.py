import time
from picamera import PiCamera
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

Camera = PiCamera()                                                                      # Initialize Camera
ImageSize = (1920, 1080)                                                                 # Full HD
CameraResolution = (int(16*np.floor(ImageSize[1]/32)),int(16*np.floor(ImageSize[0]/32))) # Adjust resolution
Camera.resolution = (CameraResolution[1],CameraResolution[0])                            # Define Resolution
Camera.zoom = (0.35, 0.75, 0.2, 0.2)                                                     # Object Zoom
RGBImageRaw = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)       # Preallocate Image
RGBImage = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)          # Preallocate Image
Camera.framerate = 30                                                                    # Fix Framerate
time.sleep(2)                                                                            # Settle Camera
Camera.iso = 200                                                                         # Fix ISO value
Camera.shutter_speed = Camera.exposure_speed                                             # Fix shutter speed
Camera.exposure_mode = 'off'                                                             # Fix White Balance
gain_set = Camera.awb_gains                                                              # AWB Query
Camera.awb_mode = 'off'                                                                  # Fix exposure gains
Camera.awb_gains = gain_set                                                              # Set AWB
Noise = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)             # Preallocate Image
x,y = np.meshgrid(np.arange(np.shape(RGBImage)[1]),np.arange(0,np.shape(RGBImage)[0]))   # Create Rectangular grid
rgb_text = ['Red','Green','Blue']                                                        # Array for naming color
input("Press enter to capture background noise image (Remove Background Noise)")
Camera.capture(Noise,'rgb')                                                              # Capture Background Noise
RGBImage = cv.subtract(RGBImageRaw, Noise)
while True:
    try:
        print('===========================')
        input("Press enter to capture an RGB Image or press CTRL+C to exit")
        Camera.capture(RGBImage,'rgb')                                                   # Capture RGB image
        mean = []                                                                        # Define Mean Vector
        std = []                                                                         # Define STDev Vector
        for c in range(0,3):                                                             # Calculate Mean and STDev
          mean.append(np.mean(RGBImage[:,:,c]-np.mean(RGBImage)))                        # Append Mean value
          std.append(np.std(RGBImage[:,:,c]-np.mean(RGBImage)))                          # Append STDev valie
          print(rgb_text[c]+'---mean: {0:2.2f}, stdev: {1:2.2f}'.format(mean[c],std[c]))
        print('The Object is: {}'.format(rgb_text[np.argmax(mean)]))
        plt.imshow(RGBImage)                                                             # Plot image
        RGBImage = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)  # Clear Memory
        plt.show()                                                                       # Show the image
    except KeyboardInterrupt:                                                            # Press CTRL+C to exit
        break