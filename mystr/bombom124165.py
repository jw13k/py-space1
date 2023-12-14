import tkinter as tk
import random


class BombDodgerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("폭탄 피하기 게임")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.character = self.canvas.create_rectangle(180, 380, 220, 400, fill="blue")
        self.bombs = []
        self.score = 0

        self.score_label = tk.Label(master, text="점수: 0", font=("Helvetica", 12))
        self.score_label.pack()

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

        self.spawn_bomb()

    def move_left(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.character)
        if x1 > 0:
            self.canvas.move(self.character, -20, 0)

    def move_right(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.character)
        if x2 < 400:
            self.canvas.move(self.character, 20, 0)

    def spawn_bomb(self):
        x = random.randint(0, 380)
        bomb = self.canvas.create_oval(x, 0, x + 20, 20, fill="red")
        self.bombs.append(bomb)
        self.move_bombs()

    def move_bombs(self):
        self.check_collision()

        for bomb in self.bombs:
            self.canvas.move(bomb, 0, 10)
            x1, y1, x2, y2 = self.canvas.coords(bomb)
            if y2 > 400:
                self.bombs.remove(bomb)
                self.canvas.delete(bomb)
                self.score += 1
                self.score_label.config(text="점수: {}".format(self.score))
                self.spawn_bomb()

        self.canvas.after(100, self.move_bombs)

    def check_collision(self):
        x1, y1, x2, y2 = self.canvas.coords(self.character)
        for bomb in self.bombs:
            bx1, by1, bx2, by2 = self.canvas.coords(bomb)
            if (x1 < bx2 and x2 > bx1) and (y1 < by2 and y2 > by1):
                self.bombs.remove(bomb)
                self.canvas.delete(bomb)
                self.score -= 1
                self.score_label.config(text="점수: {}".format(self.score))
                self.spawn_bomb()


if __name__ == "__main__":
    root = tk.Tk()
    game = BombDodgerGame(root)
    root.mainloop()
