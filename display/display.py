import os
from datetime import datetime

class Display:

    def __init__(self, text_color: str) -> None:
        self.text_color = text_color

    def generate(self) -> str:
        output = ""
        output += f"{datetime.now()}\n"

        return output

    def draw(self) -> None:
        self.clear()
        print(self.generate())


    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
