# An autofocus algorithm by finding the frame with max sum of squared Laplacian

import cv2

def var_abs_laplacian(image):
    kernelSize = 3
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=kernelSize)
    
    laplacian_square = laplacian * laplacian
    measure = laplacian_square.sum()
    return measure


if __name__ == '__main__':
    # Read input video filename
    filename = 'focus-test.mp4'

    # Create a VideoCapture object
    cap = cv2.VideoCapture(filename)

    # Read first frame from the video
    ret, frame = cap.read()

    # Display total number of frames in the video
    print("Total number of frames : {}".format(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    # Max measure of focus
    maxV = 0

    # Frame with maximum measure of focus
    bestFrame = 0 

    # Frame ID of frame with maximum measure of focus
    bestFrameId = 0 

    # Get measures of focus from both methods
    val = var_abs_laplacian(frame)

    # Specify the ROI for the flower in the frame
    top = 50
    bottom = 150
    left = 200
    right = 300

    # Iterate over all the frames present in the video
    while(ret):
        # Crop the flower region out of the frame
        flower = frame[top:bottom, left:right]
        # Get measures of focus
        val = var_abs_laplacian(frame)
        
        # If the current measure of focus is greater than the current maximum
        if val > maxV :
            # Revise the current maximum
            maxV = val
            # Get frame ID of the new best frame
            bestFrameId = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            # Revise the new best frame
            bestFrame = frame.copy()
            
        # Read a new frame
        ret, frame = cap.read()

    print("================================================")
    print("Frame ID of the best frame: {}".format(bestFrameId))

    cap.release()

    cv2.namedWindow("Best Frame", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Best Frame", bestFrame)
    cv2.waitKey()