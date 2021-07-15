from tkinter import *
from PIL import Image, ImageTk

from algorithm import solve


class Display(Frame):
    def __init__(self, master=None, dim=64, n=8, speed=40):
        super().__init__(master)
        self.master = master
        self.pack()

        self.n = n
        self.dim = dim
        self.speed = speed

        self.make_widgets()
        self.make_state()
        self.play_state()

    def make_widgets(self):
        C = Canvas(master=self,
                   width=self.dim*self.n,
                   height=self.dim*self.n)

        lines = []
        for i in range(1, self.n):
            hline = C.create_line(self.dim*i, 0, self.dim*i, self.dim*self.n)
            vline = C.create_line(0, self.dim*i, self.dim*self.n, self.dim*i)
            lines.append(hline)
            lines.append(vline)

        C.pack()
        self.C = C

    def make_state(self):
        self.solution_steps = list(solve(self.n))
        self.state_num = 0

    def play_state(self):
        self.images = []

        for i in range(len(self.solution_steps)-1):
            self.C.after(self.speed*i, self.change_state)

    def change_state(self):
        self.state_num += 1
        self.display_state()

    def display_state(self):
        solution = self.solution_steps[self.state_num]

        for image_id in self.images:
            self.C.delete(image_id)

        self.images = []

        for row, col in enumerate(solution):
            image = self.C.create_oval(
                self.dim*col, self.dim*row,
                self.dim*(col+1), self.dim*(row+1),
                fill='black')
            self.images.append(image)


if __name__=='__main__':
    root = Tk()
    display = Display(master=root)
    display.mainloop()
