from picamera import PiCamera
import numpy as np
import matplotlib.pyplot as plt

Camera = PiCamera()                                                                      # Initialize Camera
ImageSize = (1920, 1080)                                                                 # Define Full HD 
CameraResolution = (int(16*np.floor(ImageSize[1]/32)),int(16*np.floor(ImageSize[0]/32))) # Adjust resolution
Camera.resolution = (CameraResolution[1],CameraResolution[0])                            # Define Resolution
RGBImage = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)          # Preallocate image

while True:
    try:
        input("Press enter to capture an RGB Image or press CTRL+C to exit")
        Camera.zoom = (0.3, 0.7, 0.3, 0.3)                                               # Zoom in Object
        Camera.capture(RGBImage,'rgb')                                                   # Capture RGB image
        plt.imshow(RGBImage)                                                             # Display as Image
        RGBImage = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)  # Clear Memory
        plt.show()                                                                       # Show RGB Image
    except KeyboardInterrupt:                                                            # Press CTRL+C to exit
        break