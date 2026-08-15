import cv2
import picamera2

cap = picamera2.Picamera2()
config = cap.create_video_configuration(main={"format":'RGB888',"size":(820,616)})
cap.configure(config)
cap.set_controls({"ExposureTime": 100000, "AnalogueGain": 1.0, "ColourGains": (1.4,1.5)})

cap.start()
frame = cap.capture_array()

cap.close()

frame = cap.capture_array()
frame = cv2.resize(frame, (320, 240))
frame = cv2.rotate(frame, cv2.ROTATE_180)

cv2.imshow("CameraImage", frame)     # Display the obtained frame in a window called "CameraImage"
cv2.waitKey(0)			     # Make the program wait until you press a key before continuing.

# Please note: cv2.waitKey() must be called for cv2.imshow to display. 
# The input parameter to the cv2.waitKey() function is the wait time delay in milliseconds. 
# If you do not want infinite delays (0 = wait forever), simply put a 1 or other millisecond
# value in the brackets instead.

cap.close()                     # Release the camera object (if using picamera2)
cv2.destroyAllWindows()		# Close all opencv pop-up windows

# if you're reading this, the github connection worked!!!