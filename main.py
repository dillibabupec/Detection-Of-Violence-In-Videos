import cv2

# Load the video
cap=cv2.VideoCapture('Clash.mp4')

# Create a Haar cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initialize the frame counter
frame_count = 0

# Initialize the violence detection flag
violence_detected = False
Detected = False

# Loop through each frame of the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # If there are no more frames, break out of the loop
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through each face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # Increment the frame counter
        frame_count += 1
        
        # If the frame counter exceeds a threshold, set the violence detection flag
        if frame_count > 120:
            violence_detected = True
    
    # Display the frame
    cv2.imshow("frame", frame)
     
    # If the 'q' key is pressed, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break
    
    # If violence is detected, print a message and break out of the loop
    if violence_detected:
        Detected = True

# Release the video and close the window
if Detected:
    print("Violence detected!")
else:
    print("No Violence detected!")
cap.release()
cv2.destroyAllWindows()
