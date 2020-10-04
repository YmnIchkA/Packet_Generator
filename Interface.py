import tkinter
from Generator import Generator


class Interface:

    gen_obj = None

    def __init__(self):
        print('start_Interface')
        self.gen_obj = Generator()

    def print(self):
        print('Jopa')
