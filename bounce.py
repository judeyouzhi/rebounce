from Tkinter import *
import random
import time


class Ball:
    def __init__(self, cas, pad, color):
        self.canvas = cas
        self.paddle = pad
        self.id = cas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        # self.x = 0
        # self.y = -1

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
           self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_paddle(self, pos):
        global score
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.update_score(score+100)
                score = score+100
                return True
        return False

    def update_score(self, score):
        global mylabel
        self.canvas.delete(mylabel)
        mylabel=self.canvas.create_text((230, 20), text="Score: "+str(score))




class Paddle:
    def __init__(self, ca, color):
        self.canvas = ca
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)
        self.canvas.bind_all('<KeyPress-space>', self.stop)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <=0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def left(self, evt):
        print self.x
        if self.x < 0:
            self.x = self.x - 0.5
        else:
            self.x = -2

    def right(self, evt):
        print self.x
        if self.x > 0:
            self.x = self.x + 0.5
        else:
            self.x = 2

    def stop(self, evt):
        self.x = 0


tk = Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)

score= 100

mylabel = canvas.create_text((230, 20), text="Score: "+str(score))


canvas.pack()

tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, "red")



while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        mylabel = canvas.create_text((230, 200), text="GAME OVER")
        canvas.delete(paddle.id)
        canvas.delete(ball.id)
        canvas.pack()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

#mainloop()

