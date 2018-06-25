import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import urllib
import json

import pandas as pd
import numpy as np
from collections import namedtuple

# dataLink = r"http://maps.googleapis.com/maps/api/geocode/json?address=1301%20lombard%20street%20philadelphia"
# data = urllib.request.urlopen(dataLink)
# data = data.read()
# data = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
# print(data.results)

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animateEx(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split("\n")
    xList = []
    yList = []

    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)

def animate(i):
    dataLink = r"http://maps.googleapis.com/maps/api/geocode/json?address=1301%20lombard%20street%20philadelphia"
    data = urllib.request.urlopen(dataLink)
    data = data.read()
    data = json.loads(data.decode("utf-8"))
    data = data["results"]
    data = pd.DataFrame(data)
    print(data)

class SeaoBtcApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="./gradjevinski (1).ico")
        tk.Tk.wm_title(self, "Sea of BTC client")
        container = ttk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Frame in (StartPage, PageOne, PageTwo, BTCe_page):
            frame = Frame(container, self)

            self.frames[Frame] = frame

            frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=("ALPHA Bitcoin trading application use at your own risk. There is no promise of warranity"), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree",
                            command=lambda: controller.show_frame(BTCe_page))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",
                            command=quit)
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="page 1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="visit page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="page 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="visit page 1",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


class BTCe_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Graph page !!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaoBtcApp()
anim = animation.FuncAnimation(f, animateEx, interval=1000)
app.mainloop()
