from controller import controllerButton
from gpiozero import Button

# Controller Button Initialization - Temp Button Configuration for Dragon Ball Fighterz
button_A = controllerButton("A Button", "Special", 0, Button(2))
button_B = controllerButton("B Button", "Heavy", 0, Button(3))
button_X = controllerButton("X Button", "Light", 0, Button(4))
button_Y = controllerButton("Y Button", "Medium", 0, Button(17))
button_LB = controllerButton("LB Button", "Assist 1", 0, Button(27))
button_RB = controllerButton("RB Button", "Dragon Rush", 0, Button(22))
button_LT = controllerButton("LT Button", "Assist 2", 0, Button(10))
button_RT = controllerButton("RT Button", "Super Dash", 0, Button(9))
button_Start = controllerButton("Start Button", "None", 0, Button(11))
button_Select = controllerButton("Select Button", "None", 0, Button(0, hold_time = 2))
button_Up = controllerButton("Up", "Directional", 0, Button(14))
button_Down = controllerButton("Down", "Directional", 0, Button(15))
button_Left = controllerButton("Left", "Directional", 0, Button(18))
button_Right = controllerButton("Right", "Directional", 0, Button(23))

# List of Buttons to Track
buttonList = [ button_A, button_B, button_X, button_Y, button_LB, button_RB, button_LT, button_RT, button_Up, button_Down, button_Left, button_Right ]
buttonSpecialList = [ button_Start, button_Select ]

print("Controller Init Loaded")
print("----------------------")
print("{} Buttons ready to be tracked".format(len(buttonList)))
for button in buttonList:
    button.showStats()
print("----------------------")



