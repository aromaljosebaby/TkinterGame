import tkinter as tk
import random

class Player:
    
    objects = {(-1,-1)}

    def __init__(this, color):
        this.x, this.y = -1, -1
        while (this.x, this.y) in Player.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x, this.y))
        this.color = color
        this.draw()

    def draw(this):
        this.body = canvas.create_oval((this.x, this.y),
                             (this.x+step, this.y+step),
                              fill=this.color)

    def randomPoz(this, top):
        return random.randint(1, top-1)*step

    def repaint(this, x, y):
        old_x, old_y = this.x, this.y
        this.x = (this.x + x)%(step*N_X)
        this.y = (this.y + y)%(step*N_Y)
        canvas.move(this.body, (this.x - old_x), (this.y - old_y))

class Exit(Player):
    def __init__(this):
        super().__init__("yellow")

class Enemy(Player):
    def __init__(this, color = "red"):
        super().__init__(color)

class EnemyD(Enemy):

    def __init__(this):
        super().__init__("pink")

    def randomStep(this):
        r = random.randint(1, 4)
        if r == 1:
            super().repaint(step, 0)
        elif r == 2:
            super().repaint(-step, 0)
        elif r == 3:
            super().repaint(0,step)
        else:
            super().repaint(0,-step)

class Hero(Player):
    
    def __init__(this, canvas):
        this.x, this.y = -1, -1
        while (this.x, this.y) in Player.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x, this.y))
        this.body = canvas.create_image((this.x, this.y),
                                        image=player_image, anchor="nw")


    def checkPos(this, other):
        return ((this.x == other.x) and (this.y == other.y))

def keyPress(event):
    print(event)
    keys = {37, 38, 39, 40}
    if event.keycode in keys:
        keyListener(event.keycode)
        enemiesStep()
        endGame()

def keyListener(key):
    if key == 37:     #left
        player.repaint(-step, 0)
    elif key == 38:   #up
        player.repaint(0, -step)
    elif key == 39:   #right
        player.repaint(step, 0)
    elif key == 40:   #down
        player.repaint(0, step)
    
def enemiesStep():
    for enemy in enemies_d:
        enemy.randomStep()


def endGame():
    if player.checkPos(exit_g):
        print("Game over")
        print("You won!!!")
    enemies = enemies_d + enemies_s
    for enemy in enemies:
        if player.checkPos(enemy):
            print("Game over")
            print("You lose!!!")
            break

def addEnemies():
    for i in range(6):
        enemy = Enemy()
        enemies_s.append(enemy)
    for i in range(3):
        enemy = EnemyD()
        enemies_d.append(enemy)


master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
enemies_s = []
enemies_d = []
canvas = tk.Canvas(master, bg="blue", height = step*N_X, width=step*N_Y)
player_image = tk.PhotoImage(file="images/catcher.png")

addEnemies()
exit_g = Exit()
player = Hero(canvas)

        

canvas.pack()
master.bind("<KeyPress>", keyPress)
master.mainloop()








