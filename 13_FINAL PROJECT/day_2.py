import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 600
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg)        
        self.canvas.pack()
        self.pack()

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)
    
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the ball
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10
        x1 = x - self.radius
        y1 = y - self.radius
        x2 = x + self.radius
        y2 = y + self.radius
        color = "white"
        item = canvas.create_oval(x1,y1,y2, fill = color)
        super(Ball, self).__init__(canvas, item)

class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        

        super(Paddle, self).__init__(canvas, item)


if __name__ == "__main__":    
    root = tk.Tk()
    game = Game(root)
    root.title("BREAKOUT")
    root.mainloop()