from picamera import PiCamera
import numpy as np
import matplotlib.pyplot as plt

Camera = PiCamera()                                                                      # Initialize Camera
ImageSize = (1920, 1080)                                                                 # Full HD
CameraResolution = (int(16*np.floor(ImageSize[1]/32)),int(16*np.floor(ImageSize[0]/32))) # Adjust resolution
Camera.resolution = (CameraResolution[1],CameraResolution[0])                            # Define Resolution
Camera.zoom = (0.3, 0.7, 0.3, 0.3)                                                       # Zoom in Object
RGBImage = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)          # Preallocate Image
x,y = np.meshgrid(np.arange(np.shape(RGBImage)[1]),np.arange(0,np.shape(RGBImage)[0]))   # Setup 2x2
while True:
    try:
        input("Press enter to capture a RGB Component Plot or press CTRL+C to exit'")
        Camera.capture(RGBImage,'rgb')                                                   # Capture RGB image
        fig,axn = plt.subplots(2,2,sharex=True,sharey=True)                              # Setup 2x2 plot grid
        fig.set_size_inches(9,7)                                                         # Set plot size
        axn[0,0].pcolormesh(x,y,RGBImage[:,:,0],cmap='gray')                             # Get R Image Data
        axn[0,1].pcolormesh(x,y,RGBImage[:,:,1],cmap='gray')                             # Get G Image Data
        axn[1,0].pcolormesh(x,y,RGBImage[:,:,2],cmap='gray')                             # Get B Image Data
        axn[1,1].imshow(RGBImage,label='Full Color')                                     # Get RGB Image Data
        axn[0,0].title.set_text('Red')                                                   # Set plot 1 Title
        axn[0,1].title.set_text('Green')                                                 # Set plot 2 Title
        axn[1,0].title.set_text('Blue')                                                  # Set plot 3 Title
        axn[1,1].title.set_text('All')                                                   # Set plot 4 Title
        print('Plotting images...')
        plt.imshow(RGBImage)                                                             # Display as Image
        RGBImage = np.empty((CameraResolution[0],CameraResolution[1],3),dtype=np.uint8)  # Clear Memory
        plt.savefig('Component_plot.png',dpi=150)                                        # Save Component Plot
        plt.show()                                                                       # Show Image
        plt.close()
    except KeyboardInterrupt:                                                            # Press CTRL+C to exit
        break