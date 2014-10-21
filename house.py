##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#house outline
walls = drawpad.create_rectangle(300,400,500,200,fill = "red")
#roof
left = drawpad.create_line(300,200,400,100)
right = drawpad.create_line(500,200,400,100)
#windos
leftWind = drawpad.create_rectangle(325,300,375,250,fill = "white")
leftWind = drawpad.create_rectangle(425,300,475,250,fill = "white")
#door
dFrame = leftWind = drawpad.create_rectangle(375,400,425,325,fill = "white")
#chimney
leftSide = drawpad.create_line(350,150,350,50)
rightSide = drawpad.create_line(375,125,375,50)
top = drawpad.create_line(350,50,375,50)
#door handle
handle = drawpad.create_oval(419,370,424,375)
#grass
ground = drawpad.create_rectangle(0,400,800,600,fill = "green")
root.mainloop()
