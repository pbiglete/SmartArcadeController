import cInit
from time import sleep
import time
import datetime
import asyncio
from recorderSession import session

async def main():
    buttonList = cInit.buttonList
    start_Time = time.time()
    
    print("Asynchronous Button Presses")
    print("---------------------------")

    while True:
        await asyncio.gather(checkButtonInput(buttonList, start_Time))
        await asyncio.sleep(0.01)

async def checkButtonInput(buttonList, start_Time):
    time_Pressed = time.time() - start_Time
    
    for button in buttonList:
        if button.gpioPin.is_pressed:
            button.gpioPin.wait_for_release()
            print("{} Pressed @ {:.3f} sec".format(button.name, time_Pressed))
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())