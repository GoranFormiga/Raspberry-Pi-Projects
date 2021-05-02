from picamera import PiCamera
import numpy as np
from PIL import Image

Camera = PiCamera()                                                                      # Initialize Camera
ImageSize = (1920, 1080)                                                                 # Define Full HD
CameraResolution = (int(16*np.floor(ImageSize[1]/32)),int(16*np.floor(ImageSize[0]/32))) # Adjust Resolution
Camera.resolution = (CameraResolution[1],CameraResolution[0])                            # Define Resolution
Camera.zoom = (0.3, 0.7, 0.3, 0.3)                                                       # Zoom in Object
input("Press enter to capture a Test Image <<cameratest.png>>")
Camera.start_preview()
Camera.capture('cameratest.png')                                                         # Capture RGB Image 
TestImage = Image.open('cameratest.png')
TestImage.show()                                                                         # Show Test Image
Camera.stop_preview()