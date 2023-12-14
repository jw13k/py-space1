import tkinter as tk
import random

class DodgingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("회피 게임")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.user = self.canvas.create_rectangle(190, 190, 210, 210, fill="blue")
        self.enemy = self.canvas.create_rectangle(0, 0, 20, 20, fill="red")

        self.score = 0
        self.score_label = tk.Label(master, text="점수: 0", font=("Helvetica", 12))
        self.score_label.pack()

        self.master.bind("<W>", self.move_up)
        self.master.bind("<A>", self.move_left)
        self.master.bind("<S>", self.move_down)
        self.master.bind("<D>", self.move_right)

        self.spawn_enemy()

    def move_up(self, event):
        self.canvas.move(self.user, 0, -10)
        self.check_collision()

    def move_left(self, event):
        self.canvas.move(self.user, -10, 0)
        self.check_collision()

    def move_down(self, event):
        self.canvas.move(self.user, 0, 10)
        self.check_collision()

    def move_right(self, event):
        self.canvas.move(self.user, 10, 0)
        self.check_collision()

    def spawn_enemy(self):
        # 적을 화면의 가장자리에서 생성
        side = random.choice(["top", "bottom", "left", "right"])

        if side == "top":
            x1 = random.randint(0, 380)
            y1 = 0
            x2 = x1 + 20  # 적의 가로 폭이 20이라고 가정
            y2 = 20  # 적의 세로 높이가 20이라고 가정
        elif side == "bottom":
            x1 = random.randint(0, 380)
            y1 = 380
            x2 = x1 + 20
            y2 = 400
        elif side == "left":
            x1 = 0
            y1 = random.randint(0, 380)
            x2 = 20
            y2 = y1 + 20
        else:  # side == "right"
            x1 = 380
            y1 = random.randint(0, 380)
            x2 = 400
            y2 = y1 + 20

        self.canvas.coords(self.enemy, x1, y1, x2, y2)
        self.move_enemy()
