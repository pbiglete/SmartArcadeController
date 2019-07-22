from controller import controllerButton
from gpiozero import Button

# Controller Button Initalization
button_A = controllerButton("A Button", 0, Button(2))
button_B = controllerButton("B Button", 0, Button(3))
button_X = controllerButton("X Button", 0, Button(4))
button_Y = controllerButton("Y Button", 0, Button(17))
button_LB = controllerButton("LB Button", 0, Button(27))
button_RB = controllerButton("RB Button", 0, Button(22))
button_LT = controllerButton("LT Button", 0, Button(10))
button_RT = controllerButton("RT Button", 0, Button(9))
button_Start = controllerButton("Start Button", 0, Button(11))
button_Select = controllerButton("Select Button", 0, Button(0, hold_time = 2))
button_Up = controllerButton("Up", 0, Button(14))
button_Down = controllerButton("Down", 0, Button(15))
button_Left = controllerButton("Left", 0, Button(18))
button_Right = controllerButton("Right", 0, Button(23))


print("Controller Init Loaded")
print("----------------------")
button_A.showStats()
button_B.showStats()
button_X.showStats()
button_Y.showStats()
button_LB.showStats()
button_RB.showStats()
button_LT.showStats()
button_RT.showStats()
button_Select.showStats()
button_Start.showStats()
print("----------------------")



