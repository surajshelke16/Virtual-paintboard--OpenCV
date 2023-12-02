# Ai_Virtual_Painter
Virtually painting on the screen canvas with your fingers

Language used:
Python

Libraries used:
OpenCV (Real time Computer Vision)
mediapipe (Hand Tracking)

Working:

Here the basic layout is when you run your program a canvas appears in front of you with color options on the top bar ( red , green and blue) along with a earser.

Index Finger Up + Middle Finger Up - Selection 

--you can navigate anywhere on the canvas. By pointing to the colors or the eraser that particular item will get selected.

Index Finger UP -Draw

-- after selecting a color you can lower your middle finger and with only the index finger raised you can move the finger around to draw patterns on the canvas

Logic for HandTracking:

Using the mediapipe library we have written a module name HandTracking.py

--In that module we are tracking one hand and detecting 21 landmarks on it.

--image of 21 hand landmarks -https://google.github.io/mediapipe/solutions/hands.html

--then we extract those landmarks in a list in the format [no of landmark,x-value,y-value]

--then with the help of these landmarks we identify when a finger is up and when it is down

Logic for Selection:

--While we are navigating we Index and Middle finger whenever we will be in the range of the image where red color is there we will overlay the header of the canvas 
  with a new header image depicting red color is selected. (Visually interactive display for the user)
  
--In the logic we will change the color value to red

--Similary for other elements on the header

Logic for Draw:

--When we are done selecting and ready to draw we keep a track of the Index finger position.

--To keep a track we will be using 2 pair of variables one to hold the previous position and other to hold current.

--We will keep drawing lines from previous to current then, update previous to current and calculate the new current.
