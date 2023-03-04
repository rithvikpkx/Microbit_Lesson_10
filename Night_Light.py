#10.2
#Import microbit module
from microbit import *

#10.2
#Create new blank image and assign it to variable all_on
all_on = Image() # ← New

#10.2
#Set all pixels in all_on image to max brightness, 9
all_on.fill(9) # ← New

#10.4
#Read digital data from pin 0 on the microbit
#The returned data value can either be 0 or 1
#This is to set up pin 0 for later
pin0.read_digital() # ← New


#10.4
#Infinitely loop indented code
while True:
    
    #10.4
    #Read analog data from pin 0 on the microbit
    #The returned data value can be between 0 and 1024
    #Store this data value in variable value
    value = pin0.read_analog() # ← New
    
    #10.5
    #Divide value by 113 and converts the resultant value to integer
    #Store this divided integer in variable light_level
    light_level = int(value / 113)
    
    #10.5
    #Subtract value of light_level from integer 9
    #Store this subtracted value in variable lamp_level
    lamp_level = 9 - light_level
    
    #10.5
    #Sets pixels in image all_on to brightness corresponding to value of lamp_level
    all_on.fill(lamp_level) # ← New
    
    
    #10.4
    #Conditional if statement
    #If value is less than integer 500 is True, then run indented code
    #If False, then run code under else statement
    if value < 500:
        
        #10.4
        #Show image all_on on the microbit display
        display.show(all_on)
        
    
   
    else:
        
        #10.4
        #Clear display of all pixels
        display.clear()
