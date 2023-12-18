from tkinter import *


class WinTpl:
    def make(self, ele):
        # print(f"###{ele}")
        root = Tk()
        root.title(ele['text'])
        width = int(ele['width'])
        height = int(ele['height'])
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False, height=False)
        return root
