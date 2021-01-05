#FINDING THE AREA OF THE CIRCLE

import math
radius=float(input("Input the radius of the circle:"))
print("The area of the circle with radius",radius,"is",round((math.pi*radius*radius),16))


#PRINTING THE EXTENSION OF THE FILE

filename=list(input("Input the Filename:").split("."))
print("The extension of the file is:",repr(filename[1]))
             
