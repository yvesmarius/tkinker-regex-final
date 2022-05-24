from tkinter import *

DELAY = 100

root = Tk()


cnv = Canvas(root, width=400, height=100, bg='ivory')
cnv.pack()
message = StringVar()
w = Label(root, textvariable=message, font=('Arial',30,'bold'))
w.pack()


W = 300


period_s = 10
period_ms = period_s * 1000
DELAY_BAR = int(round(period_ms / W))


A = (50, 50)
B = (50 + W , 30)
bg = cnv.create_rectangle(A, B, outline="gray", fill="white")
bar = cnv.create_rectangle(A, B, outline="gray", fill="gray", width=0 )


def animate(L, bar):
    if L >= 0:
        cnv.delete(bar)
        newbar = cnv.create_rectangle(
    50, 50, 50 + L, 30, outline="gray", fill="gray", width=0)
        L -= 1
        cnv.after(DELAY_BAR, animate, L, newbar)

def chrono(s, message):
    if s >= 0:
        message.set(str(s))
        root.after(1000, chrono, s - 1, message)
animate(W, bar)
chrono(period_s, message)

root.mainloop()