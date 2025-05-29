import tkinter as tk
import time

class Canvas:
    def __init__(self, width, height):
        self.window = tk.Tk()
        self.window.title("Canvas")
        self.canvas = tk.Canvas(self.window, width=width, height=height)
        self.canvas.pack()
        self.objects = {}
        self.last_click = None
        self.mouse_x = 0
        self.mouse_y = 0
        self.canvas.bind('<Motion>', self._on_mouse_move)
        self.canvas.bind('<Button-1>', self._on_click)
        
    def _on_mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        
    def _on_click(self, event):
        self.last_click = (event.x, event.y)
        
    def create_rectangle(self, x1, y1, x2, y2, color):
        obj = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.objects[obj] = {'color': color}
        return obj
        
    def moveto(self, obj, x, y):
        self.canvas.coords(obj, x, y, x + 20, y + 20)
        
    def get_mouse_x(self):
        return self.mouse_x
        
    def get_mouse_y(self):
        return self.mouse_y
        
    def get_last_click(self):
        return self.last_click if self.last_click else (0, 0)
        
    def wait_for_click(self):
        self.last_click = None
        while self.last_click is None:
            self.window.update()
            time.sleep(0.1)
            
    def find_overlapping(self, x1, y1, x2, y2):
        overlapping = []
        for obj in self.objects:
            coords = self.canvas.coords(obj)
            if (x1 < coords[2] and x2 > coords[0] and 
                y1 < coords[3] and y2 > coords[1]):
                overlapping.append(obj)
        return overlapping
        
    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)
        self.objects[obj]['color'] = color 