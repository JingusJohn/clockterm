from display import Display
import keyboard
from config import controls, display_settings

d = Display(display_settings["text_color"])

def main():
    while True:
        if keyboard.is_pressed(controls["quit"]):
            d.clear()
            break

        d.draw()




if __name__ == "__main__":
    main()
