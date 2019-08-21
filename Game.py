import tkinter as tk
import random

class Player:

    def __init__(this, color):
        this.x = this.randomPoz(N_X)
        this.y = this.randomPoz(N_Y)
        this.color = color

    def draw(this):
        this.body = canvas.create_oval((this.x, this.y),
                             (this.x+step, this.y+step),
                              fill=this.color)

    def randomPoz(this, top):
        return random.randint(1, top-1)*step

    def repaint(this, x, y):
        canvas.move(this.body, x, y)

    def checkPos(this, other):
        return ((this.x == other.x) and (this.y == other.y))

def keyPress(event):
    print(event)
    if event.keycode == 37:     #left
        player.x -= step
        player.repaint(-step, 0)
    elif event.keycode == 38:   #up
        player.y -= step
        player.repaint(0, -step)
    elif event.keycode == 39:   #right
        player.x += step
        player.repaint(step, 0)
    elif event.keycode == 40:   #down
        player.y += step
        player.repaint(0, step)
    endGame()

def endGame():
    print("player:",player.x, player.y)
    print("exit_g:",exit_g.x, exit_g.y)
    if player.checkPos(exit_g):
        print("Game over")
        print("You won!!!")



master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg="blue", height = step*N_X, width=step*N_Y)

player = Player("green")
player.draw()
exit_g = Player("yellow")
exit_g.draw()

canvas.pack()
master.bind("<KeyPress>", keyPress)
master.mainloop()








