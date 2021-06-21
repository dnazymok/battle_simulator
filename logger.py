from abc import ABC, abstractmethod
import time
import os


class BaseLogger(ABC):
    @abstractmethod
    def write(self, text):
        pass

    @abstractmethod
    def close(self):
        pass


class TxtLogger(BaseLogger):
    def __init__(self):
        self.text = []

    def write(self, text):
        self.text.append(text)

    def close(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        os.makedirs(os.path.dirname("logs/"), exist_ok=True)
        with open(f"logs/{timestr}", "a") as log:
            for row in self.text:
                log.write(row + "\n")
