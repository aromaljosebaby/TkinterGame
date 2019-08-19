import tkinter as tk
import random

class Player:

    def __init__(this, color):
        this.x = this.randomPoz(N_X)
        this.y = this.randomPoz(N_Y)
        this.color = color

    def draw(this):
        canvas.create_oval((this.x, this.y),
                           (this.x+step, this.y+step),
                           fill=this.color)

    def randomPoz(this, top):
        return random.randint(1, top-1)*step

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg="blue", height = step*N_X, width=step*N_Y)

player = Player("green")
player.draw();
exit_g = Player("yellow")
exit_g.draw();

canvas.pack()
master.mainloop()
