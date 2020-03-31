#!/usr/bin/env python3
# coding: utf8
import pyxel, random
class App:
    def __init__(self):
        self.window = Window()
        self.rect = RageRect()
        pyxel.run(self.update, self.draw)
    def update(self):
        self.rect.update()
    def draw(self):
        self.window.draw()
        self.rect.draw()

class Window:
    def __init__(self, width=128, height=96, border_width=0):
        pyxel.init(width, height, border_width=border_width)
    def draw(self): pyxel.cls(0)

class RageRect:
    def __init__(self, x=0, y=0, width=64, height=64, color=8):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.c = color
    def update(self):
        self.mx= random.randint(-4, 4)
        self.my= random.randint(-4, 4)
    def draw(self):
        pyxel.rect((pyxel.width / 2) - (self.w / 2) + self.mx, 
                   (pyxel.height/ 2) - (self.h / 2) + self.my,
                   self.w, self.h, self.c)


App()
